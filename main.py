from disnake.ext import commands
import logging
import asyncio

from bot.config import TOKEN

from bot.extensions import load_cogs
from bot.logger import setup_logging
from bot.errors import setup_error_handler
from bot.runtime import RuntimeInfo
from bot.instance import InstanceManager


bot = commands.InteractionBot()
bot.runtime = RuntimeInfo()
bot.instance_manager=InstanceManager()



setup_logging()
setup_error_handler(bot)

@bot.event
async def on_ready():
    logging.info(f"Бот запущен: {bot.user}")
    bot.instance_manager.start_all()

load_cogs(bot)
bot.run(TOKEN)