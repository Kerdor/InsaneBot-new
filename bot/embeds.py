import disnake

SUCCESS_COLOR = 0x00B30C
ERROR_COLOR = 0xB30000
WARNING_COLOR = 0xD5D930
INFO_COLOR = 0x3100C4
DEFAULT_COLOR = 0xD4B5FF

def setup_embed(embed, inter):
    embed.set_author(
        name=inter.author.display_name,
        icon_url=inter.author.display_avatar.url
    )
    embed.set_footer(
        text=inter.bot.user.name,
        icon_url=inter.bot.user.display_avatar.url
    )
    return embed

def create_embed(title, description="", color=DEFAULT_COLOR):
    return disnake.Embed(
        title=title,
        description=description,
        color=color
    )

def success_embed(title, description=""):
    return create_embed(title, description, SUCCESS_COLOR)

def error_embed(title, description=""):
    return create_embed(title, description, ERROR_COLOR)

def warning_embed(title, description=""):
    return create_embed(title, description, WARNING_COLOR)

def info_embed(title, description=""):
    return create_embed(title, description, INFO_COLOR)