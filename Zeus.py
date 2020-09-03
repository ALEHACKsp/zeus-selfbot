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


# -- 3rd party lib imports -- #
from pypresence import Presence
from discord.ext import commands
from discord.ext import tasks
from colorama import Fore, init, Style, Back
import requests 
import discord
colorama.init()


# -- globals and constanst -- #
CONFIG_FILE_NAME = "config.json"
AUTHOR_STRING = "Charge &c| Zxy"

# -- Config Stuff -- #


# -- Entry Point -- #
def main():
  pass


from configloader import Loader





def login():
  pass

# -- main selfbot code -- #
def startprint():
  #if giveaway_sniper:
    #giveaway = f"{Fore.WHITE}[{Fore.GREEN}Enabled{Fore.WHITE}]" 
  #else:
    #giveaway = f"{Fore.WHITE}[{Fore.RED}Disabled{Fore.WHITE}]"

  #if nitro_sniper:
    #nitro = f"{Fore.WHITE}[{Fore.GREEN}Enabled{Fore.WHITE}]"        
  #else:
    #nitro = f"{Fore.WHITE}[{Fore.RED}Disabled{Fore.WHITE}]"
    print(f'''{Fore.RESET}

                        {Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗
                        {Fore.WHITE}╚══{Fore.BLUE}███{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}╔════╝{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔════╝
                          {Fore.BLUE}███{Fore.WHITE}╔╝ {Fore.BLUE}█████{Fore.WHITE}╗  {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}╗
                         {Fore.BLUE}███{Fore.WHITE}╔╝  {Fore.BLUE}██{Fore.WHITE}╔══╝  {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║╚════{Fore.BLUE}██{Fore.WHITE}║
                        {Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗╚{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}███████{Fore.WHITE}║
                        {Fore.WHITE}╚══════╝╚══════╝ ╚═════╝ ╚══════╝

                        {Fore.CYAN}Nitro Sniper {Fore.CYAN}- 
                        {Fore.CYAN}Giveaway Sniper {Fore.CYAN}- 
                        {Fore.CYAN}Prefix {Fore.CYAN}- {Fore.WHITE}[{Fore.CYAN}{prefix}{Fore.WHITE}]
                        {Fore.CYAN}                                Commands
{Fore.WHITE}________________________________________________________________________________________________________________________
        '''+Fore.RESET)

def RPC():
  client_id = "750864113248501898"
  RPC = Presence(client_id)
  RPC.connect()
  (RPC.update(state="Coming Soon.", details="root@zeus~#", large_image="big", small_image="small"))




print(f"{Fore.CYAN}Enter Your Desired Prefix:{Fore.WHITE}")
prefix = input(" ")
os.system('cls')

RPC()
colorama.init()
startprint()


client = commands.Bot(
    description='Zeus Selfbot',
    command_prefix=f"{prefix}",
    self_bot=True
)
client.remove_command('help')
loop = asyncio.get_event_loop()
clear = lambda: os.system('cls')
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()

token = Loader("config.json").main()[0]
 
client.run(token)
