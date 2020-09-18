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

class othercmds(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.embeds = client.embeds
    self.config = client.config




  @commands.command(name='commands')
  async def help_cmd(self, ctx):
   await ctx.send(
   embed = self.embeds.new_default_embed(
          title='***Commands***',
          description=f"**MessageTools** | Shows all message tools \n **NetworkTools** | Shows our network tools \n **Fun** | Shows all fun commands \n **Credits** | Shows credits"
    
    )
   )

  @commands.command(name='credits')
  async def credits_cmd(self, ctx):
    await ctx.send(
   embed = self.embeds.new_default_embed(
     title='***Credits***',
     description=f"Zeus Selfbot, is the most dynamically customizable selfbot ever created.\n\n**Developers**\n`Developed by .k#1999, and charge#0001`\n\n**Website**\n`COMING SOON`\n\n**Discord**\nhttps://discord.gg/virus"
   ),
        delete_after=self.config['embeds'].delete_after
      )

    if self.config['bot'].delete:
        await ctx.message.delete()
   
  @commands.command(name='***messagetools***')
  async def message_cmd(self, ctx):
   await ctx.send(
   embed = self.embeds.new_default_embed(
          title='***Message Tools***',
          description=f"**Purge** | Purges all messages in channel \n **EmbedSpam** | Spams given message in a embed \n **Spam** | Spams given message \n **ServerPurge** | Clears all messages in the server \n **DMPurge** | Clears all DMs"
    
    )
   ) 

  @commands.command(name=f"fun")
  async def fun_cmds(self, ctx):
      await ctx.send(
    embed = self.embeds.new_default_embed(
    title=f"***Fun Commands***",
    description=f"**Poll** | Creates a poll with given question \n **CovidStats** | Shows current COVID-19 statistics"
    )
      )


   # -- setup cog -- #
def setup(client):
  client.add_cog(othercmds(client))