"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import datetime

# -- non-standard libraries -- #
import discord
from discord.ext import commands

# -- local libraries and imports -- #
from config import Config 


class Embeds:
  def __init__(self, config):
    self.config = config['embed']
    self.url = config['embed']['link']
    self.author = self.config['author']
    self.author_url = self.config['author_url']
    self.footer = self.config['footer']
    self.footer_url = self.config['footer_url']
    self.image_url = self.config['image_url']
    self.color = self.config['color']
    self.title = self.config['title']
    self.description = self.config['description']
    self.thumbnail = self.config['thumbnail']
  
  def new_default_config_embed(self, 
    title='', description='', timestamp='', 
    fields=()
  ): 
    '''dynamic customizable function for creating an embed with the default config'''
    
    # -- init an embed  -- #
    e = discord.Embed(
      title=(title if title else f"{self.title}"), 
      description=(description if description else f"{self.description}"),
      timestamp=(timestamp if timestamp else datetime.datetime.now()),
      url=self.url,
      color=self.color
    )
    
    # -- set all embed info -- #
    if self.author and self.author_url:
      e.set_author(name=self.author, icon_url=self.author_url)
    elif self.author:
      e.set_author(name=self.author)
    if self.footer and self.footer_url:
      e.set_footer(text=self.footer, icon_url=self.footer_url)
    elif self.footer:
      e.set_footer(text=self.footer)
    if self.image_url:
      e.set_image(url=self.image_url)
    if self.thumbnail:
      e.set_thumbnail(url=self.thumbnail)
    
    if len(fields) == 0:
      # -- set fields -- #
      for i in fields:
        e.add_field(name=i[0], value=i[1], inline=i[2])
    
    # -- return new embed -- #
    return e

  def new_raw_embed(self,
    title='', description='', timestamp='', 
    fields=(), 
    thumbnail=None, footer=None,
    footer_url=None, author=None,
    author_url=None, url=None, image_url=None,
  ):
    # -- check if any of they kw are none -- #
    if thumbnail is None:
      thumbnail = self.thumbnail 
    if footer is None:
      footer = self.footer
    if footer_url is None:
      footer_url = self.footer_url
    if author is None:
      author = self.author
    if author_url is None:
      author_url = self.author_url
    if url is None:
      url = self.url
    if image_url is None:
      image_url = self.image_url

    e = discord.Embed(
      title=(title if title else f"{self.title}"), 
      description=(description if description else f"{self.description}"),
      timestamp=(timestamp if timestamp else datetime.datetime.now()),
      url=url,
      color=self.color
    )
    
    # -- set all embed info -- #
    if author and author_url:
      e.set_author(name=author, icon_url=author_url)
    elif author:
      e.set_author(name=author)
    if footer and footer_url:
      e.set_footer(text=footer, icon_url=footer_url)
    elif footer:
      e.set_footer(text=footer)
    if image_url:
      e.set_image(url=image_url)
    if thumbnail:
      e.set_thumbnail(url=thumbnail)
    
    if len(fields) == 0:
      # -- set fields -- #
      for i in fields:
        e.add_field(name=i[0], value=i[1], inline=i[2])
    
    # -- return new embed -- #
    return e
