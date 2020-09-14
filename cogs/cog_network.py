''' 
Author: k1rk and charge
Copyright: Zeus Selfbot (c) inc.
'''

# -- standard libraries -- #
import socket

# -- 3rd party libararies -- #
from discord.ext import commands
import discord

import ipapi
import pythonping

class Network(commands.Cog):
  '''A cog for handling commands related to networking'''
  def __init__(self, bot):
    self.config = bot.config
    self.embeds = bot.embeds
    self.bot = bot
  
  @commands.command(name='getip')
  async def host_to_ip(self, ctx, *, host: str):
    try:
      # -- attempt to get the hostname and create and embed -- #
      ip = socket.gethostbyname(host)
      embed = self.embeds.new_default_embed(
        title='**IP Found**',
        description='Host To IP Lookup Successfull',
        fields=(
          ('Host', host, False),
          ('IP', ip, True)
        )
      )
      await ctx.send(
        embed=embed,
        delete_after=self.config['embeds'].delete_after
      )

      if self.config['bot'].delete:
        await ctx.message.delete()

    # -- could not find the ip from the provided host -- #
    except socket.gaierror:
      embed = self.embeds.new_default_embed(
        title='**Error**', 
        description=\
          f'An Error Occured When Getting The IP of the host'
          f'Most Likely Occured Due to Invalid Host: {host}'
      )
      await ctx.send(
        embed=embed,
        delete_after=self.config['embeds'].delete_after
      )

      if self.config['bot'].delete:
        await ctx.message.delete()

  @commands.command(name='gethost')
  async def ip_to_host(self, ctx, *, ip: str):
    try:
      # -- attempt to get the ip and create and embed -- #
      host = socket.gethostbyaddr(ip)
      embed = self.embeds.new_default_embed(
        title='**Host Found**',
        description='IP To Host Lookup Successfull',
        fields=(
          ('IP', ip, False),
          ('Host', host[0], True)
        )
      )
      await ctx.send(
        embed=embed,
        delete_after=self.config['embeds'].delete_after
      )

      if self.config['bot'].delete:
        await ctx.message.delete()

    # -- could not find the ip from the provided host -- #
    except socket.herror:
      embed = self.embeds.new_default_embed(
        title='**Error**', 
        description=\
          f'An Error Occured When Getting The host of the IP\n'
          f'Most Likely Occured Due to Invalid IP: {ip}\n'
      )
      await ctx.send(
        embed=embed,
        delete_after=self.config['embeds'].delete_after
      )

      if self.config['bot'].delete:
        await ctx.message.delete()

  @commands.command(name='iplookup')
  async def ip_lookup(self, ctx, *, ip: str):
    ip_info = ipapi.location(ip=ip)

    # -- check that the response is not an error -- #
    if ip_info.get('error') is not None:
      await ctx.send(
        embed=self.embeds.new_default_embed(
          title='**Error**',
          description=\
          f'An Error Occured When looking up info on the IP\n'
          f'Most Likely Occured Due to Invalid IP: {ip}\n'
        ),
        delete_after=self.config['embeds'].delete_after
      )
      if self.config['bot'].delete:
          await ctx.message.delete()
      return

    # -- send the found info -- #
    embed = self.embeds.new_default_embed(
      title='**IP Info Found**',
      description=f'Found Info For: {ip}',
      fields=(
        ('IP', ip, False),
        ('Country', ip_info['country_name'], True),
        ('Region', ip_info['region'], True),
        ('City', ip_info['city'], True),
        ('Asn', ip_info['asn'], True),
        ('Org', ip_info['org'], True)
      )
    )
    await ctx.send(
      embed=embed,
      delete_after=self.config['embeds'].delete_after
    )
    
    if self.config['bot'].delete:
      await ctx.message.delete()

  @commands.command(name='hostlookup')
  async def host_lookup(self, ctx, *, host: str):
    pass

  @commands.command(name='ping')
  async def is_live(self, ctx, *, ip: str):
    try:
      result = pythonping.ping(ip, verbose=False)
      await ctx.send(
        embed=self.embeds.new_default_embed(
          title='Ping Results', 
          description=f'Returning Ping Results For: {ip}',
          fields=(
            ('Is Live', result.success(), False),
            ('Output', '```%s```' % "\n".join(str(x) for x in result), True)
          )
        ), 
        delete_after=self.config['embeds'].delete_after
      )
      
      if self.config['bot'].delete:
        await ctx.message.delete()

    except RuntimeError:
      await ctx.send(
        embed=self.embeds.new_default_embed(
          title='**Error**', 
          description=\
          f'An Error Occured When Pinging The IP\n'
          f'Most Likely Occured Due to Invalid IP: {ip}\n'
        ),
        delete_after=self.config['embeds'].delete_after
      )

      if self.config['bot'].delete:
        await ctx.message.delete()
      
# -- load the cog -- #
def setup(bot):
  bot.add_cog(Network(bot))
