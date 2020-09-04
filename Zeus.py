# -- std lib imports -- #
import json
import os 
import numpy 
import random 
import time 
import ctypes 
import socket
import time
import asyncio
import colorama
import datetime
from random import randint
import sys

# -- 3rd party lib imports -- #
from pypresence import Presence
from discord.ext import commands
from discord.ext import tasks
from colorama import Fore, init, Style, Back
import requests 
import discord
from configloader import Loader


# -- globals and constants -- #
CONFIG_FILE_NAME = "config.json"
AUTHOR_STRING = "Charge | Zxy"
BOT_NAME = "Zeus Selfbot"
PREFIX_LENGTH = 5
BANNER = lambda x: f"""
\033[34;1m
███████╗███████╗██╗   ██╗███████╗
╚══███╔╝██╔════╝██║   ██║██╔════╝
███╔╝ █████╗  ██║   ██║███████╗
███╔╝  ██╔══╝  ██║   ██║╚════██║- Prefix {x}
███████╗███████╗╚██████╔╝███████║- By Charge and Zxy
╚══════╝╚══════╝ ╚═════╝ ╚══════╝\033[0m                              
"""



def init():
  colorama.init()
  
  # -- init rpc -- #
  client_id = "750864113248501898"
  RPC = Presence(client_id)
  RPC.connect()
  RPC.update(state="Coming Soon.", details="root@zeus~#", large_image="big", small_image="small")

  # -- get prefix from user -- #
  prefix_str = input("Enter The Desired Prefix For Your Selfbot: ")

  if len(prefix_str) > PREFIX_LENGTH:
    print("Prefix len is greater than max %d" % PREFIX_LENGTH)
    sys.exit(1)
  
  return prefix_str

# -- Entry Point -- #
print("Make sure you create an errors.log and config.json file")

# -- get prefix -- #
prefix = init()

client = commands.Bot(
  description=BOT_NAME,
  command_prefix=prefix,
  self_bot=True
)

# -- load cog -- #
@client.command()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

# -- unload cog -- #
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')


# -- load all cogs in same directory by looping through -- #
for file_name in os.listdir('./cogs'):
  if file_name.endswith('.py'):
    client.load_extension(f'cogs.{file_name[:-3]}')

# -- print welcome message shit -- #
print(BANNER(prefix))

# -- start bot -- #
client.remove_command('help')
token = Loader(CONFIG_FILE_NAME).main()[0]
client.run(token)












