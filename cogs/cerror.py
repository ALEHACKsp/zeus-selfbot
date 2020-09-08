"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import logging

# -- non-standard libraries -- #
import discord
from discord.ext import commands

# -- local libraries and imports -- # 

class CogError(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    '''function for handling errors that are command based''' 
    print(error, "////")
    
  @commands.Cog.listener()
  async def on_error(self, ctx, error):
    '''function for handling errors that are non-command based''' 
    print(error, "????")

# -- setup cog -- #
def setup(client):
  client.add_cog(CogError(client))
