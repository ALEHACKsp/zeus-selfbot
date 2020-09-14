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
    #self.load_rp()

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
