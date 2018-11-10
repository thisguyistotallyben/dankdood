import json
import discord
from discord.ext import commands


'''
CONFIG
'''

config = {}
with open('config.json', 'r') as f:
    config = json.load(f)


'''
SHARED BOT
'''

# this is the best way to share the bot I think
# TODO: figure out if this is the best way to share the bot

# birth of a bot
bot = discord.ext.commands.Bot(command_prefix=config["prefix"],
                               description='idk')

# for custom help dialog
bot.remove_command('help')
