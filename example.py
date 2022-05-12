import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        )
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)



@bot.command(name='info')
async def nine_nine(ctx):
    info = [
        'I am a news bot on discord'
    ]
    response = random.choice(info)
    await ctx.send(response)

@bot.command(name='sports')
async def Sports(ctx):
    sports = [
        'I provide u sports news'
    ]
    response = random.choice(sports)
    await ctx.send(response)

@bot.command(name='entertainment')
async def entertainment(ctx):
    enter = [
        'I provide u entertainment news'
    ]
    response = random.choice(enter)
    await ctx.send(response)

@bot.command(name='tech')
async def tech(ctx):
    tech = [
        'I provide u technology news'
    ]
    response = random.choice(tech)
    await ctx.send(response)

@bot.command(name='lifestyle')
async def lifestyle(ctx):
    life = [
        'I provide u lifestyle news'
    ]
    response = random.choice(life)
    await ctx.send(response)

@bot.command(name='health')
async def health(ctx):
    health = [
        'I provide u health news'
    ]
    response = random.choice(health)
    await ctx.send(response)

@bot.command(name='international')
async def international(ctx):
    inter = [
        'I provide u interantional news'
    ]
    response = random.choice(inter)
    await ctx.send(response)
bot.run(TOKEN)