import os
import json
import asyncio
from datetime import datetime
from dotenv import load_dotenv
from telethon import TelegramClient

# Load .env
load_dotenv()

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
phone = os.getenv("PHONE_NUMBER")

client = TelegramClient("session", api_id, api_hash)

CHANNELS = [
    "CheMed123",
    "lobelia4cosmetics",
    "tikvahpharma"
]

# Create folders if not exist
def ensure_dirs():
    os.makedirs("data/raw/telegram_messages", exist_ok=True)
    os.makedirs("data/raw/images", exist_ok=True)

async def main():
    ensure_dirs()

    await client.start(phone=phone)
    print("Connected to Telegram!")

    today = datetime.now().strftime("%Y-%m-%d")

    for channel in CHANNELS:
        print(f"\nScraping: {channel}")

        try:
            entity = await client.get_entity(channel)

            messages_data = []

            async for message in client.iter_messages(entity, limit=50):
                data = {
                    "message_id": message.id,
                    "date": str(message.date),
                    "text": message.text,
                    "views": message.views,
                    "forwards": message.forwards,
                    "has_media": message.media is not None
                }

                messages_data.append(data)

                # Download image if exists
                if message.media:
                    image_path = f"data/raw/images/{channel}_{message.id}.jpg"
                    await client.download_media(message, file=image_path)

            # Save JSON file
            json_path = f"data/raw/telegram_messages/{today}_{channel}.json"

            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(messages_data, f, ensure_ascii=False, indent=2)

            print(f"Saved: {json_path}")

        except Exception as e:
            print(f"Error scraping {channel}: {e}")

with client:
    client.loop.run_until_complete(main())
    
async def main():
    await client.start(phone=phone)

    for channel in CHANNELS:
        entity = await client.get_entity(channel)

        async for message in client.iter_messages(entity, limit=50):

            # SAVE IMAGE (correct place)
            if message.photo:
                image_path = f"data/raw/images/{channel}_{message.id}.jpg"
                await client.download_media(message, file=image_path)

            print(message.id, message.text)