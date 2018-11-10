from random import randint


def rank():
    r = randint(0, 100)
    return dank[weight(r)]


def rank_bad():
    r = randint(0, 100)
    return notdank[weight(r)]


# TODO: make this dynamic I'm just being lazy here
def weight(r):
    if r < 10:
        return 0
    if r < 30:
        return 1
    if r < 40:
        return 2
    if r < 50:
        return 3
    if r < 70:
        return 4
    if r < 90:
        return 5
    if r < 101:
        return 6


'''
RANKS
'''

dank = [
    ":thumbsdown: not dank",
    ":ok_hand: dank enough for government work",
    "On a scale from one to dank, this is off the charts probably",
    "100 emoji worthy, my dood",
    "That's dank, or my name isn't dank dood",
    "You smell that? That's some dank stuff right there.",
    "10/10.  Would dank again."
]

notdank = [
    ":thumbsdown: not dank, my dood",
    "I find your lack of dank... disturbing",
    "Words can't describe how not dank that was...\nBut numbers can. 2/10",
    "https://i.imgur.com/pJa6IkX.jpg",
    "not dank enough, yo. better luck next time.",
    "You smell that? It certainly doesn't smell dank.",
    "Listen.  We need to have a talk.  I hear something wasn't dank.  \
    I don't take kindly to such actions.\n\n\
    http://www.reactiongifs.com/r/2013/05/about-to-go-down.gif"
]
