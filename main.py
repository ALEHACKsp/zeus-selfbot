"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import os

# -- non-standard libraries -- #

# -- local libraries and imports -- #
from init import ZeusBot

# -- globals and constants -- #
CONFIG_FILE_NAME = ''
ERROR_LOG_FILE = ''

# -- create the client object -- #
client = ZeusBot()
client.init()

# -- discord.py main functions -- #
@client.command(name='refresh', aliases=['reload', 'reset'])
async def refresh(ctx):
  for file_name in os.listdir('./cogs'):
    if file_name.endswith('.py'):
      client.load_config()
      client.load_embeds()
      client.unload_extension(f'cogs.{file_name[:-3]}')
      client.load_extension(f'cogs.{file_name[:-3]}')
  await ctx.send("cogs reloaded", delete_after=3)

client._start()
