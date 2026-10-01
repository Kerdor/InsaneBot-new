import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("token")

GUILD_IDS = [
    519209364280573954, # TEST
]

MUSIC_INSTANCES = {
    "music-1": {
        "token": os.getenv("music_1_token"),
        "discord_id": 1552327305932710000,
    },
    "music-2": {
        "token": os.getenv("music_2_token"),
        "discord_id": 1552328293099773975,
    },
    "music-3": {
        "token": os.getenv("music_3_token"),
        "discord_id": 1552329072024227861,
    },
}