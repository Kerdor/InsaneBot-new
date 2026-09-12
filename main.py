from disnake.ext import commands
from dotenv import load_dotenv

import os

load_dotenv()

bot = commands.InteractionBot()

@bot.slash_command(guild_ids=[519209364280573954])
async def hello(inter):
    await inter.response.send_message("Привет")

@bot.event
async def on_ready():
    print(f"Бот запущен {bot.user}")

def load_cogs(bot):
    for root, dirs, files in os.walk('cogs'):
        if root.endswith("__pycache__"): continue
        for file in files:
            if file.endswith(".py") and file != "__init__.py":
                roots = root.split(os.sep)
                load_text = ".".join(roots)
                try:
                    bot.load_extension(f"{load_text}.{file[:-3]}")
                    print("Загружено", f"{load_text}/{file}")
                except Exception as e:
                    print("Не загружено", f"{load_text}/{file}", e)
    

load_cogs(bot)
bot.run(os.getenv("token"))