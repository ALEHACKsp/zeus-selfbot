''' 
Author: k1rk and charge
Copyright: Zeus Selfbot (c) inc.
'''

# -- standard libraries -- #
import os
import sys
import json
from typing import Optional, Dict

# -- 3rd party libararies -- #
from pydantic import BaseModel

# -- base classes that are used to validate the config -- #

class Token(BaseModel):
  token: str

class Embeds(BaseModel):
  title = 'Buy Zeus for yourself today!'
  description = 'Advanced Customizable Selfbot'
  author = 'Authors: k1rk & Charge'
  author_url = 'https://static.dribbble.com/users/1957224/screenshots/6208642/1_2x.jpg'
  footer = 'Zeus Selfbot Inc. (c)'
  footer_url: Optional[str] = None
  image_url: Optional[str] = None
  link = ''
  thumbnail: Optional[str] = None
  delete_after = 5
  color = 0x000000

class Bot(BaseModel):
  name = 'Zeus Selfbot'
  prefix = '.'
  token: str
  presence = False
  sniper = False
  delete = True

class Presence(BaseModel):
  state = 'Zeus - Coming Soon'
  details = 'Advanced Selfbot'
  hover_big = 'DM .k#1999 or charge#0666'
  hover_small = 'Zeus Selfbot'
  
# -- Main class used to load the config -- #
class Loader:
  keys = ['bot', 'embeds', 'presence']

  def __init__(self, filename):
    '''
    class that opens json config 
    loads it in and validates that each value
    is correct
    '''
    self.filename = filename

  @classmethod
  def die(cls, info, e):
    print(
      f'Zeus Selfbot (c)\n'
      f'Info: {info if info else "nil"}\n'
      f'Error: {getattr(e, "message", repr(e)) if e else "nil"}',
      file=sys.stderr
    )
    sys.exit(-1)
  
  def file_is_there(self):
    for filename in os.listdir('.'):
      if filename == self.filename:
        return True
    return False
  
  def load_config(self):
    if not self.file_is_there:
      Loader.die(
        f'Config File: {self.filename}, Could not be found in local dir', 
        None
      )
    
    try:
      with open(self.filename, 'r') as cf:
        config = json.load(cf)
    except Exception as e:
      Loader.die(f'Could Not Open File and or Read File Into Json Format', e)
    
    for k in Loader.keys:
      if config.get(k) is None:
        Loader.die(f'Missing required value in json config: {k}', None)
    
    data = {
      'embeds': None,
      'bot': None,
      'presence': None
    }
    
    try:
      e = Embeds(**config['embeds'])
      data['embeds'] = e
      b = Bot(**config['bot'])
      data['bot'] = b
      p = Presence(**config['presence'])
      data['presence'] = p
    except Exception as e:
      Loader.die(f'Failed To Load the config', e)
    
    return data
