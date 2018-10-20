import json
import os
import random

from discord.ext import commands


class Markslop:
    """Заменитель Маркслопа"""

    def __init__(self, bot):
        self.bot = bot
        print(os.getcwd())
        with open('cogs/markslop/resources/games_list.json', encoding='utf-8') as f:
            self.games_list = json.load(f)

    @commands.group(name='маркслоп')
    async def markslop_(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(f'Некорректная команда для модуля "маркслоп". Помощь: {ctx.prefix}help маркслоп')

    @markslop_.command(name='игры')
    async def games_(self, ctx):
        """Отображает список всех игр Маркслопа"""

        message = '**Список игр**:\n' + '\n'.join(f' - {game}' for game in self.games_list)

        await ctx.send(message)

    @markslop_.command(name='игра')
    async def game_(self, ctx):
        """Выбирает одну случайную игру из списка"""

        message = f'{ctx.author}, сегодня тебе повезло и ты наконец поиграешь в **{random.choice(self.games_list)}**!'
        await ctx.send(message)

    @markslop_.command(name='аксиома')
    async def axiom_(self, ctx):
        """Отображает определение аксиомы Маркслопа"""

        message = '**Аксиома Маркслопа** - утверждение, взятое из головы, основано на минимальных знаниях предметной области и случайных неподтвержденных данных из Интернета, которое не требует доказательств своей правдивости. Ключевыми свойствами аксиомы Маркслопа являются аргументы про логическое размышление, факт личной проверки или подкрепление информации неавторитетными видеороликами / статьями.'

        await ctx.send(message)


def setup(bot):
    bot.add_cog(Markslop(bot))
