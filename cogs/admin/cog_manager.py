import disnake
from disnake.ext import commands
import logging

from bot.config import GUILD_IDS
from bot.extensions import find_extensions


class CogManager(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def autocomplete_load(self, inter, user_input):
        all_extensions = find_extensions()
        
        filtered_extensions = []
        for extension in all_extensions:
            extension_name = extension.removeprefix("cogs.")
            if extension_name.startswith(user_input) and extension not in self.bot.extensions:
                filtered_extensions.append(extension_name)
        return filtered_extensions

    async def autocomplete_loaded(self, inter, user_input):
        filtered_extensions = []
        for extension in self.bot.extensions:
            extension_name = extension.removeprefix('cogs.')
            if extension_name.startswith(user_input):
                filtered_extensions.append(extension_name)
        return filtered_extensions


    @commands.slash_command(name = "cog", description="Менеджер расширений",
                            guild_ids=GUILD_IDS)
    async def cog(self,inter):
        pass

    @cog.sub_command(name = "list", description="Список расширений",
                     guild_id=GUILD_IDS)
    async def list_cog(self, inter):
        loaded_cogs = self.bot.extensions.keys()
        loaded_cogs_list = []
        for cog in loaded_cogs:
            loaded_cogs_list.append(f"• {cog}")
        text = "\n".join(loaded_cogs_list)

        embed = disnake.Embed(title=f"{len(loaded_cogs_list)} загруженных расширений", 
                              color=disnake.Color.blue())
        embed.add_field(name='Расширения', value=text)

        await inter.response.send_message(embed=embed, ephemeral=True)

    @cog.sub_command(name = "load",
                     description="Загрузить расширение",
                     guild_id=GUILD_IDS)
    async def load_cog(self, inter,
                       name: str = commands.Param(autocomplete = autocomplete_load)):
        message = self.manage_extension("load", name)
        await inter.response.send_message(message, ephemeral = True)
    
    @cog.sub_command(name = "unload",
                         description="Выгрузить расширение",
                         guild_id=GUILD_IDS)
    async def unload_cog(self, inter,
                        name: str = commands.Param(autocomplete = autocomplete_loaded)):
        message = self.manage_extension("unload", name)
        await inter.response.send_message(message, ephemeral = True)

    @cog.sub_command(name = "reload",
                             description="Перезагрузить расширение",
                             guild_id=GUILD_IDS)
    async def reload_cog(self, inter, 
                         name: str = commands.Param(autocomplete = autocomplete_loaded)):
        message = self.manage_extension("reload", name)
        await inter.response.send_message(message, ephemeral=True)


    def manage_extension(self, action, name):
        cog = "cogs."
        try:
            if (action == "load"):
                self.bot.load_extension(cog+name)
                return f"✅ Расширение ``{name}`` загружено."
            elif (action == "unload"):
                self.bot.unload_extension(cog+name)
                return f"✅ Расширение ``{name}`` выгружено."
            elif (action == "reload"):
                self.bot.reload_extension(cog+name)
                return f"✅ Расширение ``{name}`` перезагружено."
        except commands.errors.ExtensionNotFound:
            return f":x: Расширения ``{name}`` не существует."
        except commands.errors.ExtensionAlreadyLoaded:
            return f":x: Расширение ``{name}`` уже загружено."
        except commands.errors.ExtensionNotLoaded:
            return f":x: Расширение ``{name}`` не загружено."
        except commands.errors.ExtensionFailed:
            return f":x: В расширении ``{name}`` произошла ошибка."
        except Exception as error:
            logging.error(
                f"При обработке {name} произошла неизвестная ошибка",
                exec_info=True
            )
            return f":x: При обработке ``{name}`` произошла неизвестная ошибка."


def setup(bot): 
    bot.add_cog(CogManager(bot))