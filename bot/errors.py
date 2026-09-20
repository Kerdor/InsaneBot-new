import logging
from disnake.ext import commands


async def on_slash_command_error(inter, error):
    if isinstance(error, commands.CommandInvokeError):
        error = error.original

    if isinstance(error, commands.MissingPermissions):
        await inter.response.send_message(
            f"У вас недостаточно прав для выполнения команды ``/{inter.application_command.qualified_name}``.", 
            ephemeral=True
        )
        return

    if isinstance(error, commands.BotMissingPermissions):
        await inter.response.send_message(
            f"У бота недостаточно прав для выполнения команды ``/{inter.application_command.qualified_name}``.",
            ephemeral=True
        )
        return
    
    if isinstance(error, commands.CheckFailure):
        await inter.response.send_message(
            f"Вы не можете использовать команду ``/{inter.application_command.qualified_name}``.",
            ephemeral=True
        )
        return

    logging.error(
        f"Ошибка при выполнении команды "
        f"'/{inter.application_command.qualified_name}' "
        f"пользователем {inter.author.id}",
        exc_info=error
    )
    await inter.response.send_message(
        f"При обработке команды ``/{inter.application_command.qualified_name}`` произошла ошибка.",
        ephemeral=True
    )


def setup_error_handler(bot):
    bot.add_listener(on_slash_command_error)