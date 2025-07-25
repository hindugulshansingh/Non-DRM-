#🄶🅄🄻🅂🄷🄰🄽
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "26259762"))
API_HASH = environ.get("API_HASH", "6f33406b8cb80f659d268fccd7329b0f")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

OWNER = int(environ.get("OWNER", "5504996957"))
CREDIT = environ.get("CREDIT", "𝕲𝖚𝖑𝖘𝖍𝖆𝖓𝕾𝖎𝖓𝖌𝖍")

TOTAL_USER = os.environ.get('TOTAL_USERS', '1804514955').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '1804514955').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
