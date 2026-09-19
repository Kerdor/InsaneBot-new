from disnake.ext import commands
import logging

from bot.config import TOKEN

from bot.extensions import load_cogs
from bot.logger import setup_logging

setup_logging()

bot = commands.InteractionBot()

@bot.event
async def on_ready():
    logging.info(f"Бот запущен: {bot.user}")


load_cogs(bot)
bot.run(TOKEN)