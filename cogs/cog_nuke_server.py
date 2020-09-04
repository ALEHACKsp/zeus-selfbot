
#  -- standard libraries -- #
import os 
import sys

#  -- 3rd party libraries -- #
import discord
from discord.ext import commands

class NukeServer(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.command(name="nuke")
  async def nuke(self):
    pass

  
# -- setup cog -- #
def setup(client):
  client.add_cog(HandleError(client))
