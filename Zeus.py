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
from random import randint


# -- 3rd party lib imports -- #
from pypresence import Presence
from discord.ext import commands
from colorama import Fore, init, Style, Back
import requests 
import discord


# -- globals and constanst -- #
CONFIG_FILE_NAME = "config.json"
AUTHOR_STRING = "Charge &c| Zxy"



# -- Entry Point -- #
def main():
  pass


from configloader import Loader





def login():
  pass

# -- main selfbot code -- #
def startprint():
  if giveaway_sniper:
    giveaway = f"{Fore.WHITE}[{Fore.GREEN}Enabled{Fore.WHITE}]" 
  else:
    giveaway = f"{Fore.WHITE}[{Fore.RED}Disabled{Fore.WHITE}]"

  if nitro_sniper:
    nitro = f"{Fore.WHITE}[{Fore.GREEN}Enabled{Fore.WHITE}]"        
  else:
    nitro = f"{Fore.WHITE}[{Fore.RED}Disabled{Fore.WHITE}]"
    print(f'''{Fore.RESET}

                        {Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗{Fore.BLUE}██{Fore.WHITE}╗   {Fore.BLUE}██{Fore.WHITE}╗{Fore.BLUE}███████{Fore.WHITE}╗
                        {Fore.WHITE}╚══███{Fore.WHITE}╔╝{Fore.BLUE}██{Fore.WHITE}╔════╝{Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}██{Fore.WHITE}╔════╝
                          {Fore.BLUE}███{Fore.WHITE}╔╝ {Fore.BLUE}█████{Fore.WHITE}╗  {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║{Fore.BLUE}███████{Fore.WHITE}╗
                         {Fore.BLUE}███{Fore.WHITE}╔╝  {Fore.BLUE}██{Fore.WHITE}╔══╝  {Fore.BLUE}██{Fore.WHITE}║   {Fore.BLUE}██{Fore.WHITE}║╚════{Fore.BLUE}██{Fore.WHITE}║
                        {Fore.BLUE}███████╗{Fore.BLUE}███████╗╚{Fore.BLUE}██████{Fore.WHITE}╔╝{Fore.BLUE}███████{Fore.WHITE}║
                        {Fore.WHITE}╚══════╝╚══════╝ ╚═════╝ ╚══════╝

                        {Fore.CYAN}Nitro Sniper {Fore.CYAN}- {nitro}
                        {Fore.CYAN}Giveaway Sniper {Fore.CYAN}- {giveaway}
                        {Fore.CYAN}Prefix {Fore.CYAN}- {Fore.WHITE}[{Fore.RED}{prefix}{Fore.WHITE}]
                        {Fore.CYAN}                                Commands
{Fore.WHITE}_________________________________________________________________________________________________________________________
        '''+Fore.RESET)

def RPC():
  client_id = "750864113248501898"
  RPC = Presence(client_id)
  RPC.connect()
  (RPC.update(state="   ", details="Zeus Selfbot", large_image="big", small_image="small"))

RPC()
# startprint()


print(f"{Fore.CYAN}Enter Your Desired Prefix:{Fore.WHITE}")
prefix = input(" ")
os.system('cls')


client = commands.Bot(
    description='Zeus Selfbot',
    command_prefix=f"{prefix}",
    self_bot=True
) 

token = Loader("config.json").main()[0]

client.run(token)
