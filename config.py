"""
Authors: k1rk and charge
Copyright: Zeus Selbot Source Code (C)
"""

# -- standard libraries -- #
import json
from collections import namedtuple
from sys import stderr
from pprint import pprint


class Config:

  # -- the default config for the discord selfbot -- # 
  default_config = {
    
    # -- default values for embeds sent by the bot -- #
    "embed": {
      "author": "k1rk and charge",
      "author_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Fthunder-zeus-god-artwork-can-use-t-shirt-gamer-esport-logo-artwork-is-editable-layers_9309504.htm&psig=AOvVaw1veDsqPkx2EC0bgZLyh_Tr&ust=1599289148174000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJiY7sv2zusCFQAAAAAdAAAAABAE",
      "footer": "k1rk and charge",
      "footer_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Fthunder-zeus-god-artwork-can-use-t-shirt-gamer-esport-logo-artwork-is-editable-layers_9309504.htm&psig=AOvVaw1veDsqPkx2EC0bgZLyh_Tr&ust=1599289148174000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJiY7sv2zusCFQAAAAAdAAAAABAE",
      "image_url": "1",
      "color": "2"
    },

    # -- defualt values for information about the bot -- # 
    "bot": {
      "name": "Zeus Selfbot",
      "prefix": ".",
      "rich_presence": True,
      "nitro_snipe": True,
      "giveaway_snipe": True,
      "log_messages": True
    },

    # -- default values for the bot's rich presence -- #
    "rich_presence": {
      "state": "Coming Soon.",
      "details": "Root@Zeus-$"
    },

    # -- default values for the bot's error logs -- #
    "errors": {
      "filename": "errors.log",
      "custom_string": "[+] Zeus Selfbot Error And Event Log [+]"
    },

    # -- default values for the bot's message log feature -- #
    "log": {
      "file_name": "messages.log",
      "user_ids": [
        0, 0
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
      Unkown Error Occured When During Loading Json Most Likely required keys are missing
      In Program Exception: {getattr(e, 'message', repr(e)) if e else "nil"}
      """, file=stderr
    )
    quit()
    

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
      
      self.config = config

    # -- handle fatal exception -- #
    except Exception as error:
      Config.die(error)
