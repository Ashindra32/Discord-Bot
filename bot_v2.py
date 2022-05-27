import os
from discord.ext import commands
from dotenv import load_dotenv
from news_scraper import headlines
from tech import tech_news
from business import business_news
from entertainment import enter_news
from sports import sports_news
from lifestyle import lifestyle_news
from health import health_news
from science import science_news
from smalltalk import predict
import discord
import requests
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


class NewsCog(commands.Cog, name='News'):

    news_colors = {
        'tech': discord.Colour.dark_teal(),
        'business': discord.Colour.red(),
        'entertainment': discord.Colour.orange(),
        'sports': discord.Colour.green(),
        'lifestyle': discord.Colour.blue(),
        'health': discord.Colour.purple(),
        'science': discord.Colour.dark_gold(),
        'talk': discord.Colour.dark_teal(),
        'headlines': discord.Colour.dark_magenta(),
        
    }

    def __init__(self, bot):
        self.bot = bot
        
    def trim2000char(self, text):
        if len(text) > 2000:
            return text[:1996] + '...'
        else:
            return text

    def get_quote(self):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        return(quote)

    @commands.command(name='news')
    async def info(self, ctx):
        '''
        Info about the bot news command
        '''
        response = discord.Embed(title='News', description='Choose from the following categories: \nheadlines\n!tech\n!business\n!entertainment\n!sports\n!lifestyle\n!health\n!science', color=discord.Colour.dark_blue())
        await ctx.send(response)

    @commands.command(name='tech')
    async def tech(self, ctx):
        '''
        Get the latest tech news
        '''

        news = tech_news()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Tech News', description='\n'.join(embeddable_news), color=self.news_colors['tech'])
        await ctx.send(embed=embed)
        
    @commands.command(name='business')
    async def business(self, ctx):
        '''
        Get the latest business news
        '''
        news = business_news()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Business News', description='\n'.join(embeddable_news), color=self.news_colors['business'])
        await ctx.send(embed=embed)

    @commands.command(name='entertainment')
    async def entertainment(self, ctx):
        '''
        Get the latest entertainment news
        '''

        news = enter_news()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Entertainment News', description='\n'.join(embeddable_news), color=self.news_colors['entertainment'])
        await ctx.send(embed=embed)

    @commands.command(name='sports')
    async def sports(self, ctx):
        '''
        Get the latest sports news
        '''
        news = sports_news()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Sports News', description='\n'.join(embeddable_news), color=self.news_colors['sports'])
        await ctx.send(embed=embed)

    @commands.command(name='lifestyle')
    async def lifestyle(self, ctx):
        '''
        Get the latest lifestyle news
        '''
        news = lifestyle_news()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Lifestyle News', description='\n'.join(embeddable_news), color=self.news_colors['lifestyle'])
        await ctx.send(embed=embed)

    @commands.command(name='health')
    async def health(self, ctx):
        '''
        Get the latest health news
        '''
        news = health_news()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Health News', description='\n'.join(embeddable_news), color=self.news_colors['health'])
        await ctx.send(embed=embed)
    
    @commands.command(name='science')
    async def science(self, ctx):
        '''
        Get the latest science news
        '''
        news = science_news()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Science News', description='\n'.join(embeddable_news), color=self.news_colors['science'])
        await ctx.send(embed=embed)

    @commands.command(name='headlines')
    async def headlines(self, ctx):
        '''
        Get the latest headlines
        '''
        news = headlines()
        embeddable_news = []
        counter = 0
        for idx, item in enumerate(news):
            news_entry = f"[{item['title']}]({item['link']})" + '\n'
            counter += len(news_entry)
            if counter > 2000:
                break
            embeddable_news.append(news_entry)
        embed = discord.Embed(title='Headlines', description='\n'.join(embeddable_news), color=self.news_colors['headlines'])
        await ctx.send(embed=embed)
    
    @commands.command(name='inspire', aliases=['in'])
    async def quote(self, ctx):
        '''
        Get a random inspirational quote, !inspire or !in
        '''
        quote = self.get_quote()
        await ctx.send(quote)

   
class ServerCog(commands.Cog, name='Server'):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='invite', aliases=['inv'])
    async def invite(self, ctx):
        '''
        Get the bot invite link use !inv to get the link
        '''
        embed = discord.Embed(title="Invite me to your server!", 
        description="[Click here to invite me!](https://discordapp.com/api/oauth2/authorize?client_id=970590663961874462&permissions=8&scope=bot)", color=0x00ff00)
        await ctx.send(embed=embed)

    @commands.command(name='query', aliases=['q'])
    async def query(self, ctx, *, query):
        '''
        Ask the bot a question use !q <question>
        '''
        if query.startswith('!q'):
            query = query[2:]
            out = predict(query)
            await ctx.send(out)
        else:
            out = predict(query)
            await ctx.send(out)

# test bot
if __name__ == '__main__':
    bot = commands.Bot(command_prefix='!')

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
    
    # handle unknow commands
    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found!')

    bot.add_cog(NewsCog(bot))
    bot.add_cog(ServerCog(bot))
    bot.run(TOKEN)