#  -- standard libraries -- #
import os 
import sys

#  -- 3rd party libraries -- #
import discord
from discord.ext import commands

class ErrorNoDiscord:
  # -- class variables -- #

  def __init__(self, file_name):
    
    # -- check if a file is not nil -- #
    if file_name == "":
      self.file_name = "errors.log"
    else:
      self.file_name = file_name
    
    # -- create variables -- #
    self.init_string = "|-----| [ZEUS SELFBOT LOG INIT] |----|"


  def init_file(self):
    # -- load error log file into instance -- #
    if not os.path.exists(os.path.abspath(f'./{self.file_name}')):
      return "[ERROR]: File name does not exist"
    
    try:
      with open(self.file_name, 'w') as f:
        f.write(
          f'{self.init_string}\n\n',
        )
      return ""
    
    except Exception as e:
      # -- return the error-- #
      return (
        f"[error occured when writing to file, {e}]"
      )

  def new_error(self, info, error): # fatal is a bool if truthy log error and quit
    # --- wrap all file writing functions in try except --- # 
    try:
      
      with open(self.file_name, 'w') as f:

        # -- TODO: get date and time here --#      
        d = 1
        t = 1
        
        f.write(
          f'\n\n ------ Info: Date: {d}, Time: {t} |-|-| Error: {error} ------ \n\n'
        )
      return ""
    
    except Exception as e:
      # -- return the error-- #
      return (
        f"[error occured when writing to file, {e}]"
      )

  def new_event(self, info):
    # --- wrap all file writing functions in try except --- # 
    try:
      with open(self.file_name, 'w') as f:
        f.write(
          f'\n\n ------ Info: {info} |-|-| Error: {"nil"} ------ \n\n'
        )
      return ""
    
    except Exception as e:
      # -- return the error-- #
      return (
        f"[error occured when writing to file, {e}]"
      )

class HandleError(commands.Cog):
  def __init__(self, client):
    self.client = client

    # -- init file -- #
    error = ErrorNoDiscord("errors.log").init_file()
    if error != "":
      print(f"Failed to Load Cog exiting... \n{error}")
      return

    self.log = error

  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    '''handle errors that occur when using commands'''

    # -- all errors to be ignored go in here #
    ignored = (
      commands.CommandNotFound,
      commands.MissingRequiredArgument,
    )

    error = getattr(error, 'original', error)

    # -- checks ignored tuple -- #
    if isinstance(error, ignored):
      print("An error occured but was part of the ignored errors and was not logged")
      return
    
    # -- check against known errors and custom message -- #
    if isinstance(error, commands.BadArgument):
      self.log("bad argument error occured nothing to worry about", error)
      return
  

# -- setup cog -- #
def setup(client):
  client.add_cog(HandleError(client))



