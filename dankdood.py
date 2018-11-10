# Author:  Benjamin Johnson
# Purpose: It wants to be the very dankest.


import discord

from bot import config, bot
from commands import lookup, dank, misc


# startup stuff
@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Game(name="vine compilations | !halp"))
    print('Logged in, fo shizzle')


# every message goes through here
@bot.event
async def on_message(message):
    # make case-insensitive
    message.content = message.content.lower()

    # get the bonks, boonks, and the oofs
    if message.content == 'oof':
        await message.channel.send('lol rip')
    elif message.content == 'bonk':
        await message.channel.send(bonk)

    # process everything else
    else:
        await bot.process_commands(message)


'''
STRINGS
'''


bonk = (':regional_indicator_b: '
        ':regional_indicator_o: '
        ':regional_indicator_n: '
        ':regional_indicator_k:')


# run the bot
bot.run(config['discord'])
