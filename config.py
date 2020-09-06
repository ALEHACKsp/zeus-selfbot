"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import json
from sys import stderr

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
    "embed": {
      "title": "Buy Zeus Selfbot For Yourself today !",
      "description": "Advanced dynamically customizable selfbot",
      "author": "Zeus",
      "author_url": "https://static.dribbble.com/users/1957224/screenshots/6208642/1_2x.jpg",
      "footer": "Zeus zz",
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
      "presence": True,
      "nitro_snipe": True,
      "giveaway_snipe": True,
      "log_messages": True
    },

    # -- default values for the bot's rich presence -- #
    "presence": {
      "idle": False,
      "details": "Root@Zeus-$"
    },

    # -- default values for the bot's message log feature -- #
    "log": {
      "user_ids": [
        ""
      ]
    }
  }

  def __init__(self, filename):
    self.filename = filename
    self.config = {}
    
  @staticmethod
  def die(e):
    print(
      f"""
      Zeus Selfbot [ERROR]
      Unkown Error Occured Due to one of these 
        - loading the json from the config file
      Actual Exception | Error: {getattr(e, 'message', repr(e)) if e else "nil"}
      """, file=stderr
    )
    quit()  
  
  def quick_load(self):
    '''quick function to return the config'''
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

        # -- check if all other values are there -- # 
        for key in Config.default_config.keys():
          if config.get(key) is None:
            Config.die(f'Missing Key: [{key}]')
          elif not config.get(key):
            config[key] = Config.default_config[key]

          nested = Config.default_config[key]
          # -- make sure key is a dict -- #
          if type(nested) == dict:
            for nkey in nested.keys():
              if config[key].get(nkey) is None:
                Config.die(f'Missing Key: [{nkey}]')
              elif not config[key].get(nkey):
                config[key][nkey] = Config.default_config[key][nkey]
              elif config[key].get(nkey) == "nil":
                config[key][nkey] = ""
              elif nkey == "color":
                config[key][nkey] = Config.color_lookup.get(config[key][nkey], \
                   Config.default_config['embed']['color'])

      self.config = config
    
     # -- handle fatal exception -- #
    except Exception as error:
      Config.die(error)
