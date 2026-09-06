from disnake.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot(command_prefix="!")

@bot.slash_command()
async def hello(inter):
    await inter.reply("Привет")

@bot.event
async def on_ready():
    print("Бот запущен")

bot.run(os.getenv("token"))