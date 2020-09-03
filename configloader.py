# -- standard libraries -- #
import os 
import json

class Loader(object):
  # -- class variables -- #
  _token = "token" # string
  _nitro_snipe = "nitro_snipe" # value retreived is bool
  _giveaway_snipe = "giveaway_sniper" # value retreived is bool
  _embed_color = "embed_color" # value retreived is bool


  def __init__(self, file_name):
    
    # -- color data retreived from config --#
    self.colors = {
      "red": 0xff000,
      "blue": 0x0000FF,
      "black": 0x00000,
      "green": 0x008000
    }

    # -- get file name -- #
    if file_name == "":
      self.file_name = "config.json"
    else:
      self.file_name = file_name
  

  def main(self):
    # -- main function to load and validate conig -- # 
    config = self.load_config()

    if isinstance(config, str):
      # --- handle error fatally here ---
      print(config)
      quit()
    

    # --- if len of str returned greater the string is not a color rather an error message --- #
    e = self.check_valid_color(config[3])
    if isinstance(e, str):
      # --- handle error fatally here ---
      print(e)
      quit()

    # -- check if the token was valid if not handle fatally -- #
    re = self.check_token_valid(config[0])
    if re != "":
      print("temp invalid token exiting...")
      quit()
    
    return config


  def load_config(self):
    # -- check if file name exists -- #
    if not os.path.exists(self.file_name):
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
      return f"[ERROR]: Invalid Value Provided In {self.file_name} file"
     
    return config

  
  def check_token_valid(self, token):
    # -- validate token -- #
    import discord
    client = discord.Client()
    try:
      client.run(token, bot=False)
      client.logout()
      return ""
    except Exception as failed:
      # -- handle invalid token here --- #
      return (
        f"[ERROR]: Invalid Token, Please Provide A Valid Token, Execption: {failed}"
      )

  def check_valid_color(self, e_color):
    # -- checks if the config color provided mapped to the instance dict -- #
    return self.colors.get(
      e_color, "[ERROR]: Please Provide A Valid color! Options: Red, Blue, Green, and Black."
    )
