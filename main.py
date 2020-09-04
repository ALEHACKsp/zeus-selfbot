"""
Authors: k1rk and charge
Copyright: Zeus Selbot Source Code (C)
"""

# -- standard libraries -- #
import os
import sys

# -- non-standard libraries -- #
import discord
from discord.ext import commands
from discord.ext import tasks
from pypresence import Presence

# -- local libraries and imports -- #
from config import Config


if len(sys.argv) < 2:
  print(f"Usage: <{sys.argv[0]}> <json-config>")
  quit()

if not os.path.exists(os.path.abspath(sys.argv[1])):
  print(f"Please Provide a path to a config file {sys.argv[1]} was not found")
  sys.exit()

loader = Config(sys.argv[1])
loader.load()
config = loader.config

client_id = "750864113248501898"
RPC = Presence(client_id)
RPC.connect()
RPC.update(state=config['rich_presence']['state'], details=config['rich_presence']['details'], large_image="big", small_image="small")


client = commands.Bot(
  description=config['bot']['name'],
  command_prefix=config['bot']['prefix'],
  self_bot=True
)

try:
  client.run(config['token'])
except Exception as e:
  print(
    f"""
    Zeus Selfbot [ERROR]
    Failed To Run the bot with provided token
    In Program Exception: {getattr(e, 'message', repr(e))}
    """
  )
  quit()


# @client.command()
# async def load(ctx, extension):
#   client.load_extension(f'cogs.{extension}')

# @client.command()
# async def unload(ctx, extension):
#   client.unload_extension(f'cogs.{extension}')

# # -- load all cogs in same directory by looping through -- #
# for file_name in os.listdir('./cogs'):
#   if file_name.endswith('.py'):
#     client.load_extension(f'cogs.{file_name[:-3]}')
