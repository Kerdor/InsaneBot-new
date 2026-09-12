from disnake.ext import commands
import os

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