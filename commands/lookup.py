import discord
from bot import bot, config
from utils import giphy


class redolog:
    mess = None
    search = None
    param = None


# keeping score
rl = redolog()

# giphy class
giphy = giphy.Giphy(config['giphy'])


@bot.command()
async def gif(ctx, param: str):
    last_type = 'gif'
    last_param = param
    rl.mess = ctx.message
    result = giphy.search_keyword(param)

    await ctx.send(result)


@bot.command()
async def random(ctx):
    last_type = 'random'
    result = giphy.search_random()

    await ctx.send(result)


@bot.command()
async def redo(ctx):
    print(rl.mess)
    await ctx.send(rl.mess.content)
