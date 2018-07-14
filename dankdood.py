# Author:  Benjamin Johnson
# Purpose: It wants to be the very dankest.


import discord
from random import randint
import urllib
import json

from utils import giphy
from utils import dankrank

class DankDood(discord.Client):
    def __init__(self):
        # set up giphy search
        with open('keys/giphy.txt', 'r') as f:
            lines = f.readlines()
            if len(lines) != 1:
                raise IOError
            self.giphy = giphy.Giphy(lines[0])

        # dankness ranking
        self.dankrank = dankrank.DankRank()

        # init client thing
        super().__init__()

    async def on_ready(self):
        await self.change_presence(activity=discord.Game(name="vine compilations"))
        print('logged in, fo shizzle')
        print('-------------------------------')

    async def on_message(self, message):
        # string stuff
        isstring = True
        s = ''

        # for shortness
        chan = message.channel

        # do-not-reply
        if message.author == self.user:
            return

        # make case insensitive
        message.content = message.content.lower()

        # standard !* commands
        if message.content.startswith('!'):
            # split and get relevant stuff
            msplit = message.content[1:].split(' ', 1)
            command = msplit[0]

            # no param commands
            if len(msplit) == 1:
                if command == 'hello':
                    await chan.send(f'yo {message.author}, what\'s danking my dood?')
                elif command == 'dank':
                    await chan.send(':100: :ok_hand: :joy:')
                elif command == 'dankdank':
                    await chan.send('3 DANK 5 ME')
                elif command == 'howdank':
                    await chan.send('how dank')
                    # await chan.send(self.dankrank.rank())
                elif command == 'notdank':
                    await chan.send('not dank')
                    # await chan.send(self.dankrank.rank_bad())
                if command == 'random':
                    await chan.send('random gif search here')
                    # await chan.send(self.giphy.search_random())


# start this bad boi
with open('keys/discord.txt', 'r') as f:
    lines = f.readlines()
    if len(lines) == 1:
        client = DankDood()
        client.run(lines[0].strip())






'''
# setup
client = discord.client.Client()

halp_message = "**!hello** - gives a dank message\n**!dank** - gives some dank 'mojis\n**!howdank** - gives a dankness rating\n**!doubledank** - when dank just isn't enough\n**!notdank** - for those rare occations when something isn't up to snuff\n\n**DANK GIFS**\n\n**!random** - gives a random gif (NOT GUARANTEED DANK)\n**!gif [query]** - returns a semi random gif of your choosing (GUARANTEED AS DANK AS YOUR QUERY)\n"

# ready message
@client.event
async def on_ready():
    print('Logged in, fo shizzle')

# main looping algorithm
@client.event
async def on_message(mess):
    s = ""
    valid_comm = True

    if mess.content.startswith('!hello'):
        s += "yo " + mess.author.name + ", what's danking my dood?"
    elif "!howdank" in mess.content:
        s += rate()
    elif "doubledank" in mess.content:
        s += "3 DANK 5 ME"
    elif "!dank" in mess.content:
        s += ":100: :ok_hand: :joy:"
    elif "!notdank" in mess.content:
        s += not_dank()
    elif mess.content.startswith('!halp'):
        em = discord.Embed(title='How To Dank, My Doods', description=halp_message, colour=0xff00df)
        return await client.send_message(mess.channel, embed=em)
    elif mess.content.startswith('!random'):
        s += get_rand_gif()
    elif mess.content.startswith('!gif'):
        s += get_search_gif(mess.content)
    else: valid_comm = False

    if valid_comm: return await client.send_message(mess.channel, s)

# helper functions

def get_rand_gif():
    data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/random?api_key=[giphy api key]=1").read())
    return data["data"]["image_original_url"]

def get_search_gif(mess):
    # setup

    # remove command and clean the string
    mess = mess[4:].strip()

    # error checking
    if len(mess) == 0: return "You need a search query my doods"

    # replace spaces with +
    new_mess = mess.replace(" ", "+")

    # try to grab data
    try:
        data = json.loads(urllib.request.urlopen("http://api.giphy.com/v1/gifs/search?q=" + new_mess + "&api_key=[giphy api key]=100").read())
        if (len(data["data"]) == 0): return "not dank enough (empty results)"
        num = randint(1, len(data["data"]) - 1)
        return data["data"][num]["bitly_gif_url"]
    except IOError:
        return "Request failed. Not exactly sure why, but whatevs, dood. Try again or something"

def rate():
    num = randint(0, 100)
    if num < 10:
        return ":thumbsdown: not dank"
    elif num < 30:
        return ":ok_hand: dank enough for government work"
    elif num < 40:
        return "On a scale from one to dank, this is off the charts probably"
    elif num < 50:
        return "100 emoji worthy, my dood"
    elif num < 70:
        return "That's dank, or my name isn't dank dood"
    elif num < 90:
        return "You smell that? That's some dank stuff right there."
    elif num < 101:
        return "10/10.  Would dank again."

def not_dank():
    num = randint(0, 100)
    if num < 10:
        return ":thumbsdown: not dank, my dood"
    elif num < 30:
        return "I find your lack of dank... disturbing"
    elif num < 40:
        return "Words can't describe how not dank that was...\nBut numbers can. 2/10"
    elif num < 50:
        return "https://i.imgur.com/pJa6IkX.jpg"
    elif num < 70:
        return "not dank enough, yo. better luck next time."
    elif num < 90:
        return "You smell that? It certainly doesn't smell dank."
    elif num < 101:
        return "Listen.  We need to have a talk.  I hear something wasn't dank.  I don't take kindly to such actions.\n\nhttp://www.reactiongifs.com/r/2013/05/about-to-go-down.gif"

client.run("[discord api key]")
'''
