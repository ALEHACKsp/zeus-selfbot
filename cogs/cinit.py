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
import os

# -- non-standard libraries -- #
import discord
from selenium import webdriver
from discord.ext import commands

# -- local libraries and imports -- # 


class CogInit(commands.Cog):
  def __init__(self, client):
    '''
    The Main Cog with some default event listeners and basic commands
    Note: we wrap in try accept as we want errors to be caught and logged
    '''
    self.client = client
    self.config = client.config
    self.embed = client.embeds
  
  async def cog_command_error(self, ctx, error):
    '''
    called when an error occurs in this cog
    will log to error file with speicifed time and info
    '''
    print(error)

  @commands.Cog.listener()
  async def on_ready(self):
    print(f"Bot Started, Logged In As |---> {self.client.user}")

  @commands.Cog.listener() 
  async def on_message(self, ctx):
    try:
      author = str(ctx.author)
    except Exception as e:
      logging.error(e, exc_info=True)
  
  @commands.command(name='spam')
  async def spam(self, ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
      await ctx.send(message)

  @commands.command(name='embed')
  async def embeds(self, ctx, * , message):
     await ctx.message.delete()
     await ctx.send(
      embed=self.embed.new_raw_embed(
        title=' ',
        description=f"{message}"

      )
     )

  @commands.command(name='av')
  async def get_av(self, ctx, member: discord.Member):
    await ctx.send(
      embed=self.embed.new_raw_embed(
        title='Found Avatar',
        description=f'Showing profile picture for, {member.mention}',
        image_url=member.avatar_url
      )
    )

  @commands.command(name='covid')
  async def getcovid(self, ctx):
    r = requests.get("https://api.covid19api.com/world/total")
    res = r.json()
    totalc = 'TotalConfirmed'
    totald = 'TotalDeaths'
    totalr = 'TotalRecovered'
    await ctx.send(
      embed=self.embed.new_raw_embed(
        title='COVID-19 Stats',
        description=f'Deaths | **{res[totald]}**\nConfirmed | **{res[totalc]}**\nRecovered | **{res[totalr]}**'
      )
   )

  @commands.command(name='del', aliases=['purge', 'clear', 'd'])
  async def clear(self, ctx, amount=None):
    '''simple function to purge/delete messages from a channel by the user'''
    if not isinstance(ctx.channel, discord.DMChannel) and \
      not isinstance(ctx.channel, discord.GroupChannel):
      await ctx.channel.purge(
        limit=amount if not amount else \
          int(amount), check=lambda m: m.author == ctx.author
      )  
      return

    # -- channel is dm or group channel so we must use a diffrent way to bulk delete -- #
    async for msg in ctx.channel.history(
      limit=amount if not amount else \
        int(amount)
      ):
      if msg.author == ctx.author:
        await msg.delete()
        await asyncio.sleep(0.56)

  
  
# -- setup cog -- #
def setup(client):
  client.add_cog(CogInit(client))
