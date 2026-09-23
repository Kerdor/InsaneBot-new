from disnake.ext import commands
from bot.config import GUILD_IDS

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = "settings", 
                            description="Изменение настроек сервера",
                            guild_ids=GUILD_IDS)
    async def settings(self,inter): pass

def setup(bot):
    bot.add_cog(Settings(bot))