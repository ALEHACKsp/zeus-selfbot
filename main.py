''' 
Author: k1rk and charge
Copyright: Zeus Selfbot (c) inc.
'''

# -- standard libraries -- #
import sys
import os
from time import sleep

# -- 3rd party libararies -- #
import discord
import colorama
from colorama import Fore, init, Style, Back
from discord.ext import commands
from pypresence import Presence

# -- local libraries -- #
from load_config import Loader
from custom_embeds import Embeds

if len(sys.argv) < 2:
  print(f'Usage: {sys.argv[0]} <config-file>')
  sys.exit()

class Zeus(commands.Bot):
  
  '''
  simple class that inherits from commands.Bot
  because when we load the logs the discord lib 
  passes the bot to all the cogs so if we set an attr 
  of the subclass to be the config on every reload
  then each cog will get a fresh config on reload
  '''
  
  def __init__(self, filename):
    self.rp = Presence('750864113248501898')
    self.config_file_name = filename
    self.config = {}
    self.embeds = ''

  def load(self):
    '''
    function to load the config 
    and fill out the instance variables with the config
    '''
    self.config = Loader(self.config_file_name).load_config()
    self.embeds = Embeds(self.config)
  
  def load_rp(self):
    '''loads the custom rich presence if the value is set to true in the config'''
    if self.config['bot'].presence:
      self.rp.connect()
      self.rp.update(
        state=self.config['presence'].state,
        details=self.config['presence'].details,
        large_image='big',
        small_image='small',
        small_text=self.config['presence'].hover_small,
        large_text=self.config['presence'].hover_big
      )

  def clear_screen(self):
    os.system("cls")

  def startprint(self):
    print(f'''
    
{Fore.CYAN}███████{Fore.WHITE}╗{Fore.CYAN}███████{Fore.WHITE}╗{Fore.CYAN}██{Fore.WHITE}╗   {Fore.CYAN}██{Fore.WHITE}╗{Fore.CYAN}███████{Fore.WHITE}╗
{Fore.WHITE}╚══{Fore.CYAN}███{Fore.WHITE}╔╝{Fore.CYAN}██{Fore.WHITE}╔════╝{Fore.CYAN}██{Fore.WHITE}║   {Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}██{Fore.WHITE}╔════╝
  {Fore.CYAN}███{Fore.WHITE}╔╝ {Fore.CYAN}█████{Fore.WHITE}╗  {Fore.CYAN}██{Fore.WHITE}{Fore.WHITE}║   {Fore.CYAN}██{Fore.WHITE}║{Fore.CYAN}███████{Fore.WHITE}╗
 {Fore.CYAN}███{Fore.WHITE}╔╝  {Fore.CYAN}██{Fore.WHITE}╔══╝  {Fore.CYAN}██{Fore.WHITE}║  {Fore.CYAN} ██{Fore.WHITE}║╚════{Fore.CYAN}██{Fore.WHITE}║
{Fore.CYAN}███████{Fore.WHITE}╗{Fore.CYAN}███████{Fore.WHITE}╗╚{Fore.CYAN}██████{Fore.WHITE}╔╝{Fore.CYAN}███████{Fore.WHITE}║
{Fore.WHITE}╚══════╝╚══════╝ ╚═════╝ ╚══════╝
By, {Fore.CYAN}.k{Fore.WHITE}, and{Fore.CYAN} charge


                                                      {Fore.CYAN}Commands
{Fore.WHITE}_______________________________________________________________________________________________________________________                                
    
    
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.CYAN} commands {Fore.WHITE}| Shows all command categories
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}messagetools {Fore.WHITE}| Shows all message tools
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}networktools {Fore.WHITE}| Shows all network tools
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}fun {Fore.WHITE}| Shows all fun commands
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}credits {Fore.WHITE}| Shows credits
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}poll {Fore.WHITE}| Creates a poll with given question 
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}covidstats {Fore.WHITE}| Shows current covid-19 stats
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}purge {Fore.WHITE}| Clears all messages in channel
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}dmpurge {Fore.WHITE}| Clears all messages in dms
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}serverpurge {Fore.WHITE}| Clears all dms in server
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}spam {Fore.WHITE}| Spams given message for given amount of time
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}embedspam {Fore.WHITE}| Spams given message in embed form
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}getip {Fore.WHITE}| Gets ip from host
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}ping {Fore.WHITE}| Pings given ip address 
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}gethost {Fore.WHITE}| Gets host from given ip
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}iplookup {Fore.WHITE}| Gets geo location from given ip addy
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}serverinfo {Fore.WHITE}| Grabs server info
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}userinfo {Fore.WHITE}| Grabs user info
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]  {Fore.CYAN}uav {Fore.WHITE}| Grabs user's avatar
{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.CYAN} sba {Fore.WHITE}| Grabs server banner''')

  def get_cogs(self):
    return [
      f'cogs.{x[:-3]}' for x in os.listdir('./cogs')
      if x.endswith('.py')
    ]
  
  def _load(self):
    '''function that loads all the cogs'''
    for cog in self.get_cogs():
      super().load_extension(cog)

  def _unload(self):
    '''function that unloads all the cogs'''
    for cog in self.get_cogs():
      super().unload_extension(cog)
  
  def refresh(self):
    '''function that refreshes all the cogs by calling load and unload'''
    self._unload()
    self._load()

  def init(self):
    '''
    runs the bot and loads all 
    the cogs and creates a bot from commands.Bot
    '''
    self.load()
    super().__init__(
      description=self.config['bot'].name, 
      command_prefix=self.config['bot'].prefix, 
      self_bot=True
    )
    self._load()
    self.load_rp()
    self.clear_screen()
    self.startprint()

  def go(self):
    super().remove_command('help')
    super().run(self.config['bot'].token, bot=False)
    

# -- create a new bot instance -- #
bot = Zeus(sys.argv[1])
bot.init()

# -- base commands for the bot -- #
@bot.command(name='load')
async def load_cog(ctx):
  bot.load()
  if bot.config['bot'].delete:
    await ctx.message.delete()
  bot._load()
  await ctx.send(
    'loaded!', 
    delete_after=bot.config['embeds'].delete_after
  )

@bot.command(name='unload')
async def unload_cog(ctx):
  if bot.config['bot'].delete:
    await ctx.message.delete()
  bot._unload()
  await ctx.send(
    'unloaded!', 
    delete_after=bot.config['embeds'].delete_after
  )

@bot.command(name='reload', aliases=['refresh', 'reset'])
async def reload(ctx):
  bot.load()
  if bot.config['bot'].delete:
    await ctx.message.delete()
  bot.refresh()
  await ctx.send(
    'reloaded!', 
    delete_after=bot.config['embeds'].delete_after
  )

# -- start running the bot -- #
bot.go()
