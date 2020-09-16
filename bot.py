# bot.py
# author - Rayyan Zamir

# import libraries
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

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
        "I look intimidating but I'm really not",
        "I hope there are no more reptiles during AP testing",
        "Any questions, comments, concerns?",
        "I think eels are fascinating",
        "Every year we have at least one kid fail their diploma",
        "What did I just walk into. Is this a bad time"
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
        "And you know, that's a really fascinating point you bring up. It reminds me of [some theory I read the other day]"
    ]
    kresponse = random.choice(kwisdom)
    await ctx.send(kresponse)


@bot.command(name='susanwisdom', help='Quotes from Elledge herself')
async def susanwisdom(ctx):
    swisdom = [
        "So whatever on that one",
        "And y'all...",
        "Hitler was not democratically elected.",
        "The Lusitania did not cause the United States to enter WWI.",
    ]
    sresponse = random.choice(swisdom)
    await ctx.send(sresponse)

@bot.command(name='rayyanwisdom', help='...no explanation necessary')
async def rayyanwisdom(ctx):
    wisdom = [
        "fuck you",
    ]
    response = random.choice(wisdom)
    await ctx.send(response)

bot.run(TOKEN)
