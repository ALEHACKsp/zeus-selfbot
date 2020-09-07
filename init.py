"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import os
import sys
import logging

# -- non-standard libraries -- #
import discord
from discord.ext import commands
from pypresence import Presence

# -- local libraries and imports -- #
from config import Config
from embeds import Embeds

class ZeusBot(commands.Bot):
  def __init__(self, *args, cfilename='config.json', efilename='errors.log'):
    '''simple class that inherits the defualt bot, meant to replace it so we can dynmaically pass config to the cogs''' 
    self.args = args
    self.cfilename = cfilename
    self.efilename = efilename    
    self.config = {}
    self.embeds = ''

  def load_config(self):
    self.config = Config(self.cfilename).quick_load()

  def load_presence(self):
    if self.config['bot']['presence'] == 'on':
      client_id = "750864113248501898"
      RPC = Presence(client_id)
      RPC.connect()
      RPC.update(state=self.config['presence']['state'], details=self.config['presence']['details'], large_image="big", small_image="small")

  def load_embeds(self):
    self.embeds = Embeds(self.config)

  def init_log(self):
    if not os.path.exists(os.path.abspath(self.efilename)):
      open(self.efilename, 'w+').close()

    logging.basicConfig(
      filename=self.efilename,
      filemode='a',
      format='Time: %(asctime)s - Error: %(message)s File:  %(filename)s', 
      datefmt='%d-%b-%y %H:%M:%S'
    )
  
  def init(self):
    self.load_config()
    self.load_presence()
    self.init_log()
    self.load_embeds()
    
    super().__init__(
      *self.args, 
      description=self.config['bot']['name'],
      command_prefix=self.config['bot']['prefix'],
      self_bot=True
    )
    
    for file_name in os.listdir('./cogs'):
      if file_name.endswith('.py'):
        super().load_extension(f'cogs.{file_name[:-3]}')

  def _start(self):
    super().run(self.config['token'], bot=False)
