
# -- standard library -- #
import os


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
    if not os.path.exists(self.file_name):
      return "[ERROR]: File name does not exist"
    
    try:
      with open(self.file_name) as f:
        f.write(
          f'{self.init_string}\n\n',
        )
      return ""
    
    except Exception as e:
      # -- return the error-- #
      return (
        f"error occured when writing to file, {e}"
      )

  def new_error(self, info, error):
    # --- wrap all file writing functions in try except --- # 
    try:
      
      with open(self.file_name) as f:
        f.write(
          f'\n\n ------ Info: {info} |-|-| Error: {error} ------ \n\n'
        )
      return ""
    
    except Exception as e:
      # -- return the error-- #
      return (
        f"error occured when writing to file, {e}"
      )

  def new_event(self, info):
    # --- wrap all file writing functions in try except --- # 
    try:
      with open(self.file_name) as f:
        f.write(
          f'\n\n ------ Info: {info} |-|-| Error: {"nil"} ------ \n\n'
        )
      return ""
    
    except Exception as e:
      # -- return the error-- #
      return (
        f"error occured when writing to file, {e}"
      )
  
  