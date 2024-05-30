import os
import asyncio
import logging
from aioudp import UDPServer
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent, CommentEvent
import concurrent.futures
import socket

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
    except socket.error as e:
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
        await asyncio.run_in_executor(None, send_request, event_name.lower(), 1)
        await asyncio.sleep(SLEEP_DURATION)
        await asyncio.run_in_executor(None, send_request, event_name.lower(), 0)

async def handle_comment(event: CommentEvent):
    # Handle comment events.
    logging.info(f"{event.user.nickname}: {event.comment}")
    if event.comment.lower() == "boop":
        await asyncio.run_in_executor(None, send_request, "BoopToggle", 1)
        await asyncio.sleep(SLEEP_DURATION)
        await asyncio.run_in_executor(None, send_request, "BoopToggle", 0)

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
            logging.error(f"Connection attempt {attempt + 1} failed : {e}")
            if attempt < RETRIES - 1:
                await asyncio.sleep(5)
            else:
                logging.error("All retry attempts failed.")
                raise

async def main():
    try:
        await check_gifts_and_comments()
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
