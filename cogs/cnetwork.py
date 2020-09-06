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

class Template(commands.Cog):
  def __init__(self, client):
    self.client = client


# -- setup cog -- #
def setup(client):
  client.add_cog(Template(client))
