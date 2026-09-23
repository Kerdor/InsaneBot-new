from disnake.ext import commands
from bot.embeds import *

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="test", description='Test command')
    async def test(self, inter):
        runtime = self.bot.runtime
        embed = create_embed(
            "",
            f"{runtime.uptime}"
        )
        await inter.response.send_message(embed=embed)


def setup(bot):
    bot.add_cog(Test(bot))