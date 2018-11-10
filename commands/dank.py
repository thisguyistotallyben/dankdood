import discord
from bot import bot, config
from utils import dankrank


# dank message
dankmess = ':100: :ok_hand: :joy:'

@bot.command()
async def dank(ctx):
    await ctx.send(dankmess)


@bot.command()
async def howdank(ctx):
    await ctx.send(dankrank.rank())


@bot.command()
async def notdank(ctx):
    await ctx.send(dankrank.rank_bad())
