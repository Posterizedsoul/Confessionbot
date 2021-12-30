import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
import asyncio
import random
from discord.utils import get
from datetime import datetime
from discord import Color
import os

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'confess', aliases=['cfs', 'confession', 'cf'])
    async def confess(self, ctx):
        if ctx.channel.type == discord.ChannelType.private:
            
            embed = discord.Embed(
                title = 'Type your confession.',
                description = 'Confess out anything. If you feel insecure, check out source code using c!source.',
                colour=Color.green(),
                timestamp = datetime.utcnow()
                
            )
            embed.set_author(name = 'Confession', icon_url = 'https://media.discordapp.net/attachments/925823792880701572/925840257780437032/1188983.jpg?width=814&height=678')
            embed.set_footer(text = 'You have 3 minutes to confess.'),
            demand = await ctx.send(embed = embed)
            try:
                msg = await self.bot.wait_for('message', timeout=180, check = lambda message: message.author == ctx.author and message.channel == ctx.channel)

                if msg:
                    channel = get(self.bot.get_all_channels(), guild__name = os.environ.get('SERVER'), name = 'confessions')
                    embed = discord.Embed(
                        title = 'Anonymous Confession',
                        description = f'{msg.content}', 
                        colour=Color.teal(),
                        timestamp = datetime.utcnow()
                    )
                    
                    embed.set_author(name = 'Confession Time', icon_url = 'https://media.discordapp.net/attachments/925823792880701572/925845309496623104/RingingBell.gif')
                    
                    embed.set_footer(text='Do c!confess in my DMs to confess.')
                    await channel.send(embed= embed)
                    await demand.delete()
            except asyncio.TimeoutError:
                await ctx.send('Cancelled request because you took more than 3 minutes. Try again.')
                await demand.delete()
        else:
            await ctx.send('Slide into my DMs to confess. ( ͡° ͜ʖ ͡°)')

    @commands.command(name = 'source')
    async def source(self, ctx):
        embed = discord.Embed(title = 'Source', description = 'https://github.com/Posterizedsoul/Confessionbot')
        await ctx.channel.send(embed = embed)

def setup(bot):
    bot.add_cog(Command(bot))