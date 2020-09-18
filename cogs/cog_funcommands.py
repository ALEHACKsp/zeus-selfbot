''' 
Author: k1rk and charge
Copyright: Zeus Selfbot (c) inc.
'''

# -- standard libraries -- #
import asyncio
import requests
import json

# -- 3rd party libararies -- #
import discord
from discord.ext import commands

# -- local libraries -- #
import cogs.utils.checks as checks

class funcommands(commands.Cog):
  '''A cog for handling commands related to user and server info'''
  def __init__(self, bot):
    self.config = bot.config
    self.embeds = bot.embeds
    self.bot = bot

    @commands.command(name='ban')
    async def ban_user(self, ctx, member : discord.Member, *, reason = None):
        await member.ban(reason = reason)
        await ctx.send(
        embed=self.embeds.new_raw_embed(
          title=f"Banned {member}"

      )
    )



# -- load the cog -- #
def setup(bot):
  bot.add_cog(funcommands(bot))
