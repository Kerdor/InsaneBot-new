from disnake.ext import commands
from dotenv import load_dotenv
import os

from bot.config import TEST_GUILD_ID
from bot.extensions import load_cogs

from bot.storage.database import get_session
from bot.storage.models import User


load_dotenv()

bot = commands.InteractionBot()

@bot.slash_command(guild_ids=[TEST_GUILD_ID])
async def start(inter):
    await inter.response.send_message("Будущее начальное сообщение с помощью пользователю")

@bot.event
async def on_ready():
    print(f"Бот запущен {bot.user}")


load_cogs(bot)
bot.run(os.getenv("token"))