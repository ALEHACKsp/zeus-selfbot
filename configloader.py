
# -- standard libraries -- #
import os 
import json


class Loader(object):
  # -- class variables -- #
  _token = "token" # string
  _nitro_snipe = "nitro_snipe" # value retreived is bool
  _giveaway_snipe = "giveaway_sniper" # value retreived is bool
  _embed_color = "embed color" # value retreived is bool


  def __init__(self, file_name):
    
    # -- color data retreived from config --#
    self.colors = {
      "red": 0xff000,
      "blue": 0x0000FF,
      "black": 0x00000,
      "green": 0x008000
    }

    # -- main data retreived from config --#
    self.token = ""
    self.embed_color = ""
    self.img_url_string = ""

    # -- get file name -- #
    if file_name == "":
      self.file_name = "config.json"
    else:
      self.file_name = file_name
  
  
  def load_config(self):
    # -- check if file name exists -- #
    if not os.path.exists(self.filename):
      return "[ERROR]: File name does not exist"
    
    # -- load into dictionary -- #
    with open(self.file_name) as f:
      
      # -- wrap in try accept block as loading json can raise exception -- #
      try:
        config = json.load(f)
      except Exception as e:
        # -- most likely failed to convert json to dict so log error and quit -- #
        return (
          f"[ERROR]: Failed to load config, Exception: {f}"
        )

      # -- get will return nil if value was not not found and nil is falsy --- #
      config = (
        config.get(Loader._token),
        config.get(Loader._giveaway_snipe),
        config.get(Loader._nitro_snipe),
        config.get(Loader._embed_color)
      )
    
    # -- check if any val in tuple if so return error string -- #
    if any(not x for x in config):
      return "[ERROR]: Invalid Value Provided In Json"
     
    return config







  def check_token_valid(self):
    pass

  def check_valid_color(self):
    pass






    

