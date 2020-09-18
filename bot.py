# bot.py
# author - Rayyan Zamir

# import libraries
import os
import random
import discord
import markovify
from dotenv import load_dotenv
from discord.ext import commands
from webserver import keep_alive
from makedictionaries import make_dictionaries
# find bot token
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# set command prefix
bot = commands.Bot(command_prefix='~')
# pull quotes
wisdom = make_dictionaries()


# change status
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    await bot.change_presence(activity=discord.Game("~help"))


# all of the wisdoms
@bot.command(name='holmeswisdom')
async def holmeswisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Holmes"])
        await ctx.send("Holmes: " + response)
        i += 1


@bot.command(name='karenwisdom')
async def karenwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Karen"])
        await ctx.send("Hunnicutt: " + response)
        i += 1


@bot.command(name='susanwisdom')
async def susanwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Elledge"])
        await ctx.send("Elledge: " + response)
        i += 1


@bot.command(name='rayyanwisdom')
async def rayyanwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Rayyan"])
        await ctx.send("Rayyan: " + response)
        i += 1


@bot.command(name='huywisdom')
async def huywisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Huy"])
        await ctx.send("Huy: " + response)
        i += 1


@bot.command(name='deannawisdom')
async def deannawisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Dowling"])
        await ctx.send("Dowling: " + response)
        i += 1


@bot.command(name='haritawisdom', help='Deshpande')
async def haritawisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Deshpande"])
        await ctx.send("Deshpande: " + response)
        i += 1


@bot.command(name='nancywisdom', help="Nancy Sun")
async def nancywisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Sun"])
        await ctx.send("Sun: " + response)
        i += 1


@bot.command(name='annanwisdom')
async def annanwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Annan"])
        await ctx.send("Annan: " + response)
        i += 1


@bot.command(name='jordanwisdom')
async def jordanwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Kauffman"])
        await ctx.send("Kauffman: " + response)
        i += 1


@bot.command(name='nathanwisdom', help='Nathan Kim')
async def nathanwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Nathan"])
        await ctx.send("Nathan: " + response)
        i += 1


# this insanity has every quote in a dictionary with the speaker
@bot.command(name='ibwisdom')
async def ibwisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        person = random.choice(list(wisdom.keys()))
        response = random.choice(wisdom[person])
        await ctx.send(person + ": " + response)
        i += 1

@bot.command(name='hivemind', help='this is experimental')
async def hivemind(ctx, number: int = 1):
    with open("quotes.txt", encoding='utf-8') as f:
        text = f.read()

# Build the model.
    def generateQuote():
        text_model = markovify.Text(text, well_formed = False)
        return text_model.make_short_sentence(300, tries=250, max_overlap_ratio = .8)
    i = 0
    while i < number:
        response = generateQuote()
        await ctx.send(str(response))
        i += 1



keep_alive()
bot.run(TOKEN)