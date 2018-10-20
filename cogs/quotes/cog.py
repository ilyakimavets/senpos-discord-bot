import json
import os
import random

import discord
from discord.ext import commands
from peewee import fn

from models.quote import Quote


class Quotes:
    """Модуль с цитатами"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group(name="цитаты")
    async def quotes_(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(
                f'Некорректная команда для модуля "цитаты". Помощь: {ctx.prefix}help цитаты'
            )

    @quotes_.command(name="добавить")
    @commands.guild_only()
    async def add_(self, ctx, *, quote_text: str):
        """Добавить цитату в базу"""
        if not quote_text:
            return await ctx.send(
                f"**{ctx.author.name}**, что ты мне прислал? Используй !help цитаты"
            )

        quote, created = Quote.get_or_create(author_id=ctx.author.id, text=quote_text)

        if created:
            return await ctx.send(
                f'**{ctx.author.name}** добавил цитату _"{quote_text}"_.'
            )

        return await ctx.send(
            f'Цитата _"{quote_text}"_ (**{ctx.author.name}**) уже есть в базе.'
        )

    @quotes_.command(name="удалить")
    @commands.guild_only()
    @commands.is_owner()
    async def remove_(self, ctx, *, quote_text: str):
        """Удалить цитату из базы"""
        if not quote_text:
            return await ctx.send(
                f"**{ctx.author.name}**, что ты мне прислал? После команды отправь цитату, которую надо удалить!"
            )

        deleted = bool(Quote.delete().where(Quote.text == quote_text).execute())

        if not deleted:
            return await ctx.send(
                f'Цитата _"{quote_text}"_ **не найдена** базе.'
            )
        return await ctx.send(
            f'Цитата _"{quote_text}"_ **удалена** из базы.'
        )

    @quotes_.command(name="список")
    @commands.guild_only()
    async def list_(self, ctx):
        """Показать список всех цитат"""
        quotes = tuple(Quote.select())
        if not quotes:
            return await ctx.send(f"В базе цитат пусто")

        message = '\n\n'.join(f'Автор: **{self.bot.get_user(quote.author_id).name}**\n'
                              f' - *"{quote.text}"*' for quote in quotes)
        await ctx.send(message)

    @quotes_.command(name="случайная")
    @commands.guild_only()
    async def random_(self, ctx):
        """Показать случайную цитату"""
        quote = Quote.select().order_by(fn.Random()).get()
        if not quote:
            return await ctx.send(f"В базе цитат пусто")

        message = f'Автор: **{self.bot.get_user(quote.author_id).name}**\n' \
                  f' - *"{quote.text}"*'
        await ctx.send(message)


def setup(bot):
    bot.add_cog(Quotes(bot))
