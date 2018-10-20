import logging
import sys
import traceback

import discord
from discord.ext import commands
from dynaconf import settings

from models import init_database

# list of cogs is available in the "cogs" folder
cogs = ("quotes", "markslop")

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(case_insensitive=True, command_prefix="!", pm_help=False)


@bot.command(name='веном')
async def venom_(ctx, *, caption=None):
    await ctx.message.delete()

    embed = discord.Embed(
        colour=discord.Colour.dark_grey(),
        description=caption
    )
    # embed.set_image(url='https://i.imgur.com/b5z2y6c.png')
    embed.set_image(
        url='https://images-ext-2.discordapp.net/external/8MLzgyhGMqZdBnIvWfbN-1lzDjFobB8t8onM2XoX4Bw/https/i.imgur.com/b5z2y6c.png')
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@bot.event
async def on_ready():
    for cog in cogs:
        try:
            bot.load_extension(f"cogs.{cog}.cog")
            logging.info("Loaded {}".format(cog))
        except Exception as e:
            print("Failed to load extension {}.".format(cog), file=sys.stderr)
            traceback.print_exc()
    logging.info("Bot loaded")


def main():
    init_database()
    bot.run(settings.TOKEN)


if __name__ == "__main__":
    main()
