import discord
from discord import client
from discord.embeds import Embed
from discord.ext import commands
from discord import Color
import asyncio
import random
import os



bot = commands.Bot(command_prefix='c!')
bot.remove_command('help')
    

@bot.event
async def on_ready():
    await bot.change_presence(activity = discord.Game(name = f""))
    print("Confession Bot is online!!!")

async def ch_pr():
  await bot.wait_until_ready()
  statuses = [f'Currently on {len(bot.guilds)} servers', "c!source to see the source code.", 'with your Confessions']
  while not bot.is_closed():
    status = random.choice(statuses) 
    await bot.change_presence(activity = discord.Game(name = status))
    await asyncio.sleep(18)

@bot.command()
async def help(ctx):
        embed = discord.Embed(title = 'Help', colour = Color.red())
        embed.add_field(name = 'c!confess', value = "```Use this command in direct messages to confess your feelings.``` ")
        embed.add_field(name = 'But dev can see my confession, right?', value = "```No. Don't panik no ones going to know who confessed what. See the source code(c!source).```" , inline = False)
        await ctx.channel.send(embed = embed)

extentions = ['cogs.confession']    
for ext in extentions:
    bot.load_extension(ext)

bot.loop.create_task(ch_pr())
bot.run(os.environ.get('TOKEN'))

