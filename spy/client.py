from spy.config import config
from pyrogram import Client

bot = Client(
    session_name=config.SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins={'root': 'spy.plugins'}
)

asst = Client(
  "dynamic_bot",
  api_id = config.API_ID,
  api_hash = config.API_HASH,
  bot_token = config.TOKEN,
  plugins={'root': "spy.assistant"}
)
