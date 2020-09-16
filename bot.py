# bot.py
# author - Rayyan Zamir

# import libraries
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands
from webserver import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='~')


# change status
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game("~help"))


@bot.command(name='holmeswisdom', help='Advice from momma Shelly Holmes herself')
async def holmeswisdom(ctx):
    wisdom = [
        "You are so weird",
        "Like, some kind of Jesus figure?",
        "I look intimidating but I'm really not.",
        "I hope there are no more reptiles during AP testing.",
        "Any questions, comments, concerns?",
        "I think eels are fascinating.",
        "Every year we have at least one kid fail their diploma.",
        "What did I just walk into? Is this a bad time?",
        "Should I be concerned?",
        "Terrifying.",
        "She could rip my face off and I would still love her.",
        "I have no idea what you are saying.",
        "Someone once described caviar to me as having the same consistency as bath oil beads.",
        "SO GLAD to hear you’ve been floor swimming.",
        "Real as penitentiary steel.",
    ]
    response = random.choice(wisdom)
    await ctx.send(response)


@bot.command(name='karenwisdom', help='Advice from momma Hunnicutt herself')
async def karenwisdom(ctx):
    kwisdom = [
        "I am so looking forward to reading your EE!",
        "I am looking forward to your presentation!",
        "Eric, my husband and my best friend...",
        "Have a wonderful day!",
        "Fabulous discussion",
        "Could you slide that off your desk please?",
        "You've got some good stuff!",
        "And you know, that's a really fascinating point you bring up. It reminds me of [some theory I read the other day]",
        "Hello my friends!",
        "We see the homeless as two standard deviations below the mean of human.",
        "Could you unplug for me please?",

    ]
    kresponse = random.choice(kwisdom)
    await ctx.send(kresponse)


@bot.command(name='susanwisdom', help='Quotes from Elledge herself')
async def susanwisdom(ctx):
    swisdom = [
        "So whatever on that one.",
        "And y'all...",
        "Hitler was not democratically elected.",
        "The Lusitania did not cause the United States to enter WWI.",
        "I like the First Moroccan Crisis.",
        "Someone talk other than Huy",
        "I like Truman.",
        "Y’all take out your notes.",
        "MacArthur was a...questionable kinda guy.",

    ]
    sresponse = random.choice(swisdom)
    await ctx.send(sresponse)

@bot.command(name='rayyanwisdom', help='...no explanation necessary')
async def rayyanwisdom(ctx):
    rwisdom = [
        "fuck you",
        "women don't deserve rights",
    ]
    rresponse = random.choice(rwisdom)
    await ctx.send(rresponse)

keep_alive()
bot.run(TOKEN)