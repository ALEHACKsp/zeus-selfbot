"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import json
from sys import stderr, exit

# -- non-standar libraries - #
import discord 

class Config:
 
  color_lookup = {
    'blue': discord.Color.blue(),
    'blurple': discord.Color.blurple(),
    'dark_blue': discord.Color.dark_blue(),
    'dark_gold': discord.Color.dark_gold(),
    'dark_gray': discord.Color.dark_gray(),
    'dark_green': discord.Color.dark_green(),
    'dark_grey': discord.Color.dark_grey(),
    'dark_magenta': discord.Color.dark_magenta(),
    'dark_orange': discord.Color.dark_orange(),
    'dark_purple': discord.Color.dark_purple(),
    'dark_red': discord.Color.dark_red(),
    'dark_teal': discord.Color.dark_teal(),
    'darker_gray': discord.Color.darker_gray(),
    'gold': discord.Color.gold(),
    'green': discord.Color.green(),
    'greyple': discord.Color.greyple(),
    'light_gray': discord.Color.light_gray(),
    'light_grey': discord.Color.light_grey(),
    'lighter_gray': discord.Color.lighter_gray(),
    'lighter_grey': discord.Color.lighter_grey(),
    'magenta': discord.Color.magenta(),
    'orange': discord.Color.orange(),
    'purple': discord.Color.purple(),
    'red': discord.Color.red(),
    'black': 0x000000
  }

  # -- the default config for the discord selfbot -- # 
  default_config = {
    
    # -- default values for embeds sent by the bot -- #
    "embeds": {
      "title": "Buy Zeus Selfbot For Yourself today !",
      "description": "Advanced dynamically customizable selfbot",
      "author": "Buy Zeus Selfbot For Yourself today !",
      "author_url": "https://static.dribbble.com/users/1957224/screenshots/6208642/1_2x.jpg",
      "footer": "Location: In Hiding",
      "footer_url": "https://static.dribbble.com/users/1957224/screenshots/6208642/1_2x.jpg",
      "image_url": "https://static.dribbble.com/users/1957224/screenshots/6208642/1_2x.jpg",
      "color": color_lookup['black'],
      "thumbnail": "https://static.dribbble.com/users/1957224/screenshots/6208642/1_2x.jpg",
      "delete": 0,
      "link": "https://proxysec.xyz/"
    },  

    # -- defualt values for information about the bot -- # 
    "bot": {
      "name": "Zeus Selfbot",
      "prefix": ".",
      "presence": "on",
      "nitro_snipe": "on",
      "giveaway_snipe": "on",
    },

    # -- default values for the bot's rich presence -- #
    "presence": {
      "state": "Coming Soon - Zeus",
      "details": "Advanced Dynamic Selfbot"
    }
  }

  def __init__(self, filename):
    self.filename = filename
    self.config = {}
    
  @staticmethod
  def die(e):
    print(
      "Zeus Selfbot [ERROR]\n"
      "Unkown Error Occured Due to one of the listed errors\n"
      "1: loading the json from the config file\n"
      f"Actual Exception | Error: {getattr(e, 'message', repr(e)) if e else 'nil'}",
      file=stderr
    )
    exit(-1)
  
  def quick_load(self):
    """quick function to return the config"""
    self.load()
    return self.config

  def load(self):
    """wrap in try accept whenever we accsess files as errors could always occurr here"""
    try:
      with open(self.filename, 'r') as f:

        # -- load config -- #
        config = json.load(f)

         # -- make sure token is there -- # 
        if not config.get('token'):
          Config.die('please provide a token in the json config file')

        embed_keys = Config.default_config['embeds'].keys()
        bot_keys = Config.default_config['bot'].keys()
        presence_keys = Config.default_config['presence'].keys()

        if config.get('embeds') is None or config.get('bot') \
          is None or config.get('presence') is None:
          Config.die("missing key (embeds or bot or presence)")
        
        # -- parse embeds key -- #
        for key in embed_keys:
          if config['embeds'].get(key) is None:
            Config.die(f"missing field: [{key}] in [embeds] header")
          if key == "delete":
            if type(config['embeds']['delete']) != int:
              Config.die("delete field in embeds header must be of int")
            if config['embeds']['delete'] not in range(1, 999):
              Config.die("delete field in embeds header must be in range 1-999")
          if config['embeds'].get(key) == "":
            config['embeds'][key] = Config.default_config['embeds'][key]
            continue
          if config['embeds'].get(key) == "nil":
            config['embeds'][key] = ""
        
        # -- parse bot keys -- #
        for i, v in enumerate(bot_keys):
          if config['bot'].get(v) is None:
            Config.die(f"missing field: [{v}] in [bot] header")
          if i > 1:
            if config['bot'].get(v) not in ['on', 'off']:
              Config.die(f"field: [{v}] in [bot] header must be on or off")
          if config['bot'].get(v) == "":
            config['bot'][v] = Config.default_config['bot'][v]
            
        # -- parse presence keys -- #
        for k in presence_keys:
          if config['presence'].get(k):
            Config.die(f"missing field: [{k}] in [presence] header")
          if config['presence'].get(k) == "":
            config['presence'][k] = Config.default_config['presence'][k]

      self.config = config
    
    # -- handle fatal exception -- #
    except Exception as error:
      Config.die(error)
