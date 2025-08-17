# 𝐌𝐑𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑™ 
# Add your details here and then deploy

import os
from os import environ

# Telegram API / Bot
API_ID = int(environ.get("API_ID", "22470912"))
API_HASH = environ.get("API_HASH", "511be78079ed5d4bd4c967bc7b5ee023"))
BOT_TOKEN = environ.get("BOT_TOKEN", "")

# Owner / Auth users
OWNER = int(environ.get("OWNER", "7678862761"))
CREDIT = "𝐌𝐑𝐒𝐓𝐑𝐀𝐍𝐆𝐄𝐑™"

AUTH_USER = os.environ.get("AUTH_USERS", "7678862761").split(",")
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]

if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))

# Downloader tuning (for m3u8 parallel downloader)
MAX_CONN = int(os.environ.get("MAX_CONN", "16"))            # Parallel connections
RETRY = int(os.environ.get("RETRY", "3"))                  # Retries per segment
CONNECT_TIMEOUT = int(os.environ.get("CONNECT_TIMEOUT", "15"))
READ_TIMEOUT = int(os.environ.get("READ_TIMEOUT", "60"))
CHUNK_LIMIT_PER_HOST = int(os.environ.get("CHUNK_LIMIT_PER_HOST", "8"))
