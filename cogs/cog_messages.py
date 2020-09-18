"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import sys
import logging
import asyncio
import requests
import json

# -- non-standard libraries -- #
import discord
from discord.ext import commands

# -- local libraries and imports -- # 

class messages(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.embeds = client.embeds
    self.config = client.config

  @commands.command(name='del', aliases=['purge', 'clear', 'd'])
  async def clear(self, ctx, amount=None):
    '''simple function to purge/delete messages from a channel by the user'''

    if not isinstance(ctx.channel, discord.DMChannel) and \
      not isinstance(ctx.channel, discord.GroupChannel):
      await ctx.channel.purge(
        limit=amount if not amount else \
          int(amount), check=lambda m: m.author == ctx.author and \
            not m.is_system()
      )
      await ctx.send(
        embed=self.embeds.new_default_config_embed(
          title="Cleared Chats",
          description=f"Amount: {amount if amount else 9999}"
        ), delete_after=self.config['embeds']['delete']
      )  
      return

    # -- channel is dm or group channel so we must use a diffrent way to bulk delete -- #
    i = 0
    async for msg in ctx.channel.history(
      limit=amount if not amount else \
        int(amount)
      ):
      if msg.author == ctx.author and not msg.is_system():
        i += 1
        await msg.delete()
    await ctx.send(
        embed=self.embeds.new_default_config_embed(
          title="Cleared chats",
          description=f"Amount: {i}"
        ), 
        delete_after=self.config['embeds']['delete']
      )  

  @commands.command(name='dmpurge')
  async def del_all_dms(self, ctx):
    '''function that gathers a list of all your dm's and deletes all of them'''

    i = 0
    for channel in self.client.private_channels:
      async for msg in channel.history(limit=None):
        if msg.author == ctx.author and not msg.is_system():
          await msg.delete()
          i += 1
    await ctx.send(
      embed=self.embeds.new_default_config_embed(
        title="Cleared all dm chats",
        description=f"Amount: {i}"
      ),
      delete_after=self.config['embed']['delete']
    )

  @commands.command(name='serverpurge')
  async def del_all_channel(self, ctx):
    '''function that deletes all messages from a specific channels'''

    i = 0
    for guild in self.client.guilds:
      for channel in guild.text_channels:
        async for msg in channel.history(limit=None):
          if msg.author == ctx.author and not msg.is_system():
            await msg.delete()
            i += 1
    await ctx.send(
    embed=self.embeds.new_default_config_embed(
      title="Cleared all channel chats",
      description=f"Amount: {i}"
    ),
    delete_after=self.config['embed']['delete']
  )

  @commands.command(name='spam')
  async def spam_ctx(self, ctx, count: int, *, msg: str):
    
    for _ in range(count):
      await ctx.send(msg)

  @commands.command(name='embedspam')
  async def spam_embed_ctx(self, ctx, count: int, *, msg: str):
    
    embed = self.embeds.new_default_embed(
      title=f"Spamming: {msg}",
      description=f"Spamming G"
    ) 
    for _ in range(count):
      await ctx.send(embed=embed)

  @commands.command(name='covidstats')
  async def covid_status(self, ctx):
    r = requests.get("https://api.covid19api.com/world/total")
    res = r.json()
    totalc = 'TotalConfirmed'
    totald = 'TotalDeaths'
    totalr = 'TotalRecovered'
    await ctx.send(
      embed = self.embeds.new_default_embed(
          title='COVID-19 Stats',
          description=f"Deaths | **{res[totald]}**\nConfirmed | **{res[totalc]}**\nRecovered | **{res[totalr]}**"
      ),
        delete_after=self.config['embeds'].delete_after
      )

    if self.config['bot'].delete:
        await ctx.message.delete()

  @commands.command(name='embed')
  async def emsg(self, ctx, *, message):
    await ctx.send(
      embed = self.embeds.new_default_embed(
        title=f" ",
        description=f"{message}"
       
         ),
        delete_after=self.config['embeds'].delete_after
      )

    if self.config['bot'].delete:
        await ctx.message.delete()

  @commands.command(name='poll')
  async def poll_cmd(self, ctx, *, question: str):
    msg = await ctx.send(
      embed = self.embeds.new_default_embed(
        title=f"Poll!",
        description=f"{question}"

      )
    )
    try:
        await ctx.message.delete()
    except:
        pass
    if ctx.guild.id == 207943928018632705:
        # Essential :sexthumb:
        yes_thumb = discord.utils.get(
            ctx.guild.emojis, id=287711899943043072)
        no_thumb = discord.utils.get(
            ctx.guild.emojis, id=291798048009486336)
    else:
        yes_thumb = "👍"
        no_thumb = "👎"
    await msg.add_reaction(yes_thumb)
    await msg.add_reaction(no_thumb)
    








# -- setup cog -- #
def setup(client):
  client.add_cog(messages(client))