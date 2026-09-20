from disnake.ext import commands

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="test", description='Test command')
    async def test(self, inter):
        runtime = self.bot.runtime
        await inter.response.send_message(f"{runtime.uptime}")


def setup(bot):
    bot.add_cog(Test(bot))