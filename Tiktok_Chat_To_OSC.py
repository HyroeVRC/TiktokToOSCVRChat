import asyncio
import logging
from aioudp import UDPServer
from TikTokLive import TikTokLiveClient
from TikTokLive.types.events import GiftEvent, CommentEvent
import concurrent.futures

# Configuration options
UDP_IP = "127.0.0.1"
UDP_PORT = 9000
USERNAME = "@your_username"  # CHANGE YOUR USERNAME HERE
SLEEP_DURATION = 2  # Duration to sleep after sending a gift or boop

# Function to send a request to the IP address with the current state of a parameter
async def send_request(parameter, value):
    async with UDPServer(UDP_IP, UDP_PORT) as server:
        await server.send_message(f"/avatar/parameters/{parameter}", value)

# Define a function to handle gift events
async def handle_gift(event: GiftEvent):
    allowed_events = ["Rose", "Galaxy"]
    event_name = event.gift.name
    if event_name in allowed_events:
        await asyncio.run_in_executor(None, send_request, event_name.lower(), 1)  # Send 1 when the gift is received
        await asyncio.sleep(SLEEP_DURATION)
        await asyncio.run_in_executor(None, send_request, event_name.lower(), 0)  # Send 0 after the specified duration

# Define a function to handle comment events
async def handle_comment(event: CommentEvent):
    # Display the message in ASCII in the console
    logging.info(f"{event.user.nickname}: {event.comment}")
    # Check if the comment is "boop"
    if event.comment.lower() == "boop":
        await asyncio.run_in_executor(None, send_request, "BoopToggle", 1)  # Send 1 when "boop" is received
        await asyncio.sleep(SLEEP_DURATION)
        await asyncio.run_in_executor(None, send_request, "BoopToggle", 0)  # Send 0 after the specified duration

async def check_gifts_and_comments():
    client = TikTokLiveClient(unique_id=USERNAME)
    client.on("gift", handle_gift)
    client.on("comment", handle_comment)

    # Retry mechanism
    retries = 5
    for attempt in range(retries):
        try:
            await client.connect()
            break  # Exit loop if successful
        except Exception as e:
            logging.error(f"Connection attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                await asyncio.sleep(5)  # Wait before retrying
            else:
                logging.error("All retry attempts failed.")
                raise  # Re-raise the exception after final attempt

async def main():
    await check_gifts_and_comments()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # Set logging level
    asyncio.run(main())
