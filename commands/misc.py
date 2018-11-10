import discord
import time
from datetime import datetime, timedelta
from bot import bot, config


# start time
start_time = time.time()


'''
UPTIME
'''


@bot.command()
async def uptime(ctx):
    await ctx.send(calc_uptime())


def calc_uptime():
    up = str(timedelta(seconds=(time.time()-start_time)))

    # parse it pretty-like
    upsplit = up.split(',', 1)
    if len(upsplit) == 1:
        days = '0'
    else:
        days = upsplit[0].split()[0]
        upsplit[0] = upsplit[1]

    upsplit = upsplit[0].split(':')
    if len(upsplit) != 3:
        print('Something happened')
        return ''

    hours = upsplit[0]
    minutes = upsplit[1]
    if minutes[0] == '0':
        minutes = minutes[1]
    seconds = upsplit[2].split('.', 1)[0]
    if seconds[0] == '0':
        seconds = seconds[1]

    # horribly complicated, but appeases my awful need for proper plurality

    rets = ''
    rets += f"{days} day{'' if days == '1' else 's'}, "
    rets += f"{hours} hour{'' if hours == '1' else 's'}, "
    rets += f"{minutes} minute{'' if minutes == '1' else 's'}, "
    rets += f"{seconds} second{'' if seconds == '1' else 's'}"

    return rets


'''
Oof counter
TODO: make this server specific
'''


@bot.command()
async def oofs(ctx):
    await ctx.send(f"Number of oofs since last reboot: {config['oofs']}")
