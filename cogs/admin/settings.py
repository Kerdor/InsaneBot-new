from disnake.ext import commands
from bot.config import TEST_GUILD_ID

class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name = "settings", 
                            description="Изменение настроек сервера",
                            guild_ids=[TEST_GUILD_ID])
    async def settings(self,inter): pass

def setup(bot):
    bot.add_cog(Settings(bot))