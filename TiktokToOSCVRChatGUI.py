import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import asyncio
import threading
import logging
from aioudp import UDPServer
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent, CommentEvent
import socket
import os

# Configuration options
UDP_IP = "127.0.0.1"
UDP_PORT = 9000
USERNAME = os.getenv('@username')  # Get username from environment variables
SLEEP_DURATION = 2  # Duration to sleep after sending a gift or boop
RETRIES = 5  # Number of retry attempts

def is_udp_server_running(ip, port):
    # Check if the UDP server is running.
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        sock.bind((ip, port))
    except socket.error:
        return True
    sock.close()
    return False

async def send_request(parameter, value):
    # Send a request to the IP address with the current state of a parameter.
    if is_udp_server_running(UDP_IP, UDP_PORT):
        async with UDPServer(UDP_IP, UDP_PORT) as server:
            await server.send_message(f"/avatar/parameters/{parameter}", value)
    else:
        logging.error(f"UDP server is not running on {UDP_IP}:{UDP_PORT}")

async def handle_gift(event: GiftEvent):
    # Handle gift events.
    allowed_events = ["Rose", "Galaxy"]
    event_name = event.gift.name
    if event_name in allowed_events:
        await send_request(event_name.lower(), 1)
        await asyncio.sleep(SLEEP_DURATION)
        await send_request(event_name.lower(), 0)

async def handle_comment(event: CommentEvent):
    # Handle comment events.
    logging.info(f"{event.user.nickname}: {event.comment}")
    if event.comment.lower() == "boop":
        await send_request("BoopToggle", 1)
        await asyncio.sleep(SLEEP_DURATION)
        await send_request("BoopToggle", 0)

async def check_gifts_and_comments():
    # Check for gifts and comments.
    client = TikTokLiveClient(unique_id=USERNAME)
    client.on("gift", handle_gift)
    client.on("comment", handle_comment)

    for attempt in range(RETRIES):
        try:
            await client.connect()
            break
        except TikTokLiveClient.ConnectionError as e:  # Catch specific exception
            logging.error(f"Connection attempt {attempt + 1} failed: {e}")
            if attempt < RETRIES - 1:
                await asyncio.sleep(5)
            else:
                logging.error("All retry attempts failed.")
                raise

async def start_event_handling():
    # Start event handling.
    try:
        await check_gifts_and_comments()
    except Exception as e:
        logging.error(f"An unexpected error occurred : {e}")

def run_asyncio_task(loop, task):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(task)

def start_button_click():
    loop = asyncio.new_event_loop()
    threading.Thread(target=run_asyncio_task, args=(loop, start_event_handling())).start()

def send_toggle_request(parameter, value):
    loop = asyncio.new_event_loop()
    threading.Thread(target=run_asyncio_task, args=(loop, send_request(parameter, value))).start()

def activate_gift_event(event_name):
    send_toggle_request(event_name.lower(), 1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.sleep(SLEEP_DURATION))
    send_toggle_request(event_name.lower(), 0)

def boop_toggle():
    send_toggle_request("BoopToggle", 1)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.sleep(SLEEP_DURATION))
    send_toggle_request("BoopToggle", 0)

class TextHandler(logging.Handler):
    # Logging handler to redirect logs to a Tkinter Text widget.
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text_widget.configure(state='normal')
            self.text_widget.insert(tk.END, msg + '\n')
            self.text_widget.configure(state='disabled')
            self.text_widget.yview(tk.END)
        self.text_widget.after(0, append)

# GUI Setup
root = tk.Tk()
root.title("TikTok Live Event Handler")
root.geometry("600x700")
root.resizable(True, True)

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 12), padding=10)
style.configure("TLabel", font=("Helvetica", 12))
style.configure("TFrame", padding=10)
style.configure("TLabelFrame", font=("Helvetica", 12), padding=10)

main_frame = ttk.Frame(root, padding="10 10 10 10")
main_frame.pack(fill=tk.BOTH, expand=True)

label = ttk.Label(main_frame, text="TikTok Live Event Handler", anchor="center", font=("Helvetica", 16, "bold"))
label.pack(pady=10)

start_button = ttk.Button(main_frame, text="Start Event Handling", command=start_button_click)
start_button.pack(pady=10, fill=tk.X)

rose_button = ttk.Button(main_frame, text="Activate Rose Event", command=lambda: activate_gift_event("Rose"))
rose_button.pack(pady=10, fill=tk.X)

galaxy_button = ttk.Button(main_frame, text="Activate Galaxy Event", command=lambda: activate_gift_event("Galaxy"))
galaxy_button.pack(pady=10, fill=tk.X)

boop_button = ttk.Button(main_frame, text="Boop Toggle", command=boop_toggle)
boop_button.pack(pady=10, fill=tk.X)

# Adding a ScrolledText widget for logging
log_frame = ttk.LabelFrame(main_frame, text="Logs")
log_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

log_text = scrolledtext.ScrolledText(log_frame, wrap=tk.WORD, height=10, state='disabled', font=("Helvetica", 10))
log_text.pack(fill=tk.BOTH, expand=True)

# Set up logging to the text widget
text_handler = TextHandler(log_text)
logging.basicConfig(level=logging.INFO, handlers=[text_handler])

# Start the Tkinter event loop
root.mainloop()
