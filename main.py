from disnake.ext import commands
import logging

from bot.config import TOKEN

from bot.extensions import load_cogs
from bot.logger import setup_logging
from bot.errors import setup_error_handler
from bot.runtime import RuntimeInfo


bot = commands.InteractionBot()
bot.runtime = RuntimeInfo()

setup_logging()
setup_error_handler(bot)

@bot.event
async def on_ready():
    logging.info(f"Бот запущен: {bot.user}")

load_cogs(bot)
bot.run(TOKEN)