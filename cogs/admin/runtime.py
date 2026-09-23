from disnake.ext import commands
from datetime import timedelta

from bot.config import GUILD_IDS
from bot.embeds import info_embed, setup_embed


class Runtime(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="runtime", 
                            description="Информация о состоянии бота",
                            guild_ids=GUILD_IDS)
    async def runtime(self, inter):
        runtime = self.bot.runtime

        embed = info_embed(
            title=":gear: Runtime Information")

        embed.add_field(
            name=f"Python",
            value=runtime.python_version,
            inline=True
        )
        embed.add_field(
            name="Disnake",
            value=runtime.disnake_version,
            inline=True
        )
        embed.add_field(
            name="ОС",
            value=runtime.os_name,
            inline=True
        )
        embed.add_field(
            name="Архитектура",
            value=runtime.architecture,
            inline=True
        )
        embed.add_field(
            name="Запущен",
            value=runtime.startup_time.strftime("%d.%m.%Y %H:%M:%S"),
            inline=True
        )
        embed.add_field(
            name="Аптайм",
            value=str(timedelta(seconds=round(runtime.uptime))),
            inline=True
        )
        
        setup_embed(embed,inter)
        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(Runtime(bot))