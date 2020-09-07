"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import sys
import logging
import asyncio

# -- non-standard libraries -- #
import discord
from discord.ext import commands

# -- local libraries and imports -- # 

class MsgDel(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.embeds = client.embeds
    self.config = client.config

  @commands.command(name='del', aliases=['purge', 'clear'])
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

# -- setup cog -- #
def setup(client):
  client.add_cog(MsgDel(client))
