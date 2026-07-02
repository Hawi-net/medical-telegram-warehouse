import os
import json
import logging
from datetime import datetime

from dotenv import load_dotenv
from telethon import TelegramClient

# Load environment variables
load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

# Telegram client
client = TelegramClient("session", API_ID, API_HASH)

# Channels to scrape
CHANNELS = [
    "CheMed123",
    "lobelia4cosmetics",
    "tikvahpharma"
]

# Create required directories
os.makedirs("data/raw/telegram_messages", exist_ok=True)
os.makedirs("data/raw/images", exist_ok=True)
os.makedirs("logs", exist_ok=True)

# Configure logging
logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


async def scrape_channel(channel):
    print(f"\nScraping: {channel}")
    logging.info(f"Started scraping {channel}")

    entity = await client.get_entity(channel)

    messages = []

    today = datetime.now().strftime("%Y-%m-%d")
    json_folder = f"data/raw/telegram_messages/{today}"
    os.makedirs(json_folder, exist_ok=True)

    image_folder = f"data/raw/images/{channel}"
    os.makedirs(image_folder, exist_ok=True)

    async for message in client.iter_messages(entity, limit=50):

        message_data = {
            "message_id": message.id,
            "date": str(message.date),
            "text": message.text,
            "views": message.views,
            "forwards": message.forwards,
            "has_media": message.media is not None,
        }

        messages.append(message_data)

        # Download photos
        if message.photo:
            image_path = os.path.join(image_folder, f"{message.id}.jpg")
            await client.download_media(message, file=image_path)

    json_path = os.path.join(json_folder, f"{channel}.json")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=4)

    print(f"Saved {len(messages)} messages from {channel}")
    logging.info(f"Saved {len(messages)} messages from {channel}")


async def main():
    await client.start(phone=PHONE_NUMBER)
    print("Connected to Telegram!")

    for channel in CHANNELS:
        try:
            await scrape_channel(channel)
        except Exception as e:
            print(f"Error scraping {channel}: {e}")
            logging.error(f"Error scraping {channel}: {e}")


with client:
    client.loop.run_until_complete(main())