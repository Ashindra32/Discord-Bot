import os
import random
from urllib import response
from discord.ext import commands
from dotenv import load_dotenv
from news_scraper import timesofindia
from tech import tech_news
from business import business_news
from entertainment import enter_news
from sports import sports_news
from lifestyle import lifestyle_news
from health import health_news
from science import science_news
from discord import Client
from smalltalk import *
import discord

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix='!')
client = discord.Client()


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


async def on_message(ctx):
    if ctx.author.bot:
        return
    elif ctx.content.startswith('!help'):
        await ctx.send('!hello - Hello!\n!news - News\n!tech - Technology\n!business - Business\n!entertainment - Entertainment\n!sports - Sports\n!lifestyle - Lifestyle\n!health - Health\n!science - Science')
    elif ctx.content.startswith('!news'):
        await ctx.send('Choose from the following categories: \n!tech\n!business\n!entertainment\n!sports\n!lifestyle\n!health\n!science')
    elif ctx.content.startswith('!tech'):
        await ctx.send(tech_news())
    elif ctx.content.startswith('!business'):
        await ctx.send(business_news())
    elif ctx.content.startswith('!entertainment'):
        await ctx.send(enter_news())
    elif ctx.content.startswith('!sports'):
        await ctx.send(sports_news())
    elif ctx.content.startswith('!lifestyle'):
        await ctx.send(lifestyle_news())
    elif ctx.content.startswith('!health'):
        await ctx.send(health_news())
    elif ctx.content.startswith('!science'):
        await ctx.send(science_news())
    elif ctx.content.startswith('!headlines'):
        await ctx.send(timesofindia())
    elif len(ctx.content) > 10:
        print(ctx.content)
        out = predict(ctx.content)
        await ctx.send(out)
    else:
        await ctx.send('Please enter a valid command or message') 
    


@bot.command(name='info')
async def nine_nine(ctx):
    info = [
        'I am a news bot on discord'
    ]
    response = random.choice(info)
    await ctx.send(response)

@bot.command(name='sports')
async def Sports(ctx):
    news = sports_news()
    news_titles = [f" > {idx+1}. {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0] 
    news_content ="sports News\n"+"\n".join(news_titles[:2000])
    await ctx.send(news_content)

@bot.command(name='entertainment')
async def entertainment(ctx):
    news = enter_news()
    news_titles = [f"> {idx+1}. {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0] 
    
    news_content ="Entertainment News\n"+"\n".join(news_titles)
    await ctx.send(news_content[:2000])

@bot.command(name='lifestyle')
async def lifestyle(ctx):
    news = lifestyle_news()
    news_titles = [f"> {idx+1}. {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0]
    news_content ="Life Style News\n"+"\n".join(news_titles)
    await ctx.send(news_content[:2000])

@bot.command(name='health')
async def health(ctx):
    news = health_news()
    news_titles = [f" > {idx+1}. {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0]
    news_content ="Health News\n"+"\n".join(news_titles)
    await ctx.send(news_content[:2000])

@bot.command(name='headlines')
async def international(ctx):
    news = timesofindia()
    news_titles = [f"News {idx} : {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0] 
    await ctx.send("\n".join(news_titles)[:2000])

@bot.command(name='tech')
async def tech(ctx):
    print('tech news')
    news = tech_news()
    news_titles = [f"> {idx+1}. {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0]
    news_content = "Tech News\n"+"\n".join(news_titles)[:2000] 
    await ctx.send(news_content)

@bot.command(name='business')
async def business(ctx):
    news = business_news()
    news_titles = [f"> {idx+1}. {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0] 
    news_content ="Business News\n"+"\n".join(news_titles)
    await ctx.send(news_content[:2000])

@bot.command(name='science')
async def science(ctx):
    news = science_news()
    news_titles = [f"> {idx+1}. {item['title']}" for idx,item in enumerate(news) if len(item['title'])>0] 
    news_content ="Science News\n"+"\n".join(news_titles)
    await ctx.send(news_content[:2000])


if __name__ == "__main__":
    bot.run(TOKEN)

