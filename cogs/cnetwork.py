"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import sys
import logging
import asyncio
import requests
import json

# -- non-standard libraries -- #
import discord
from discord.ext import commands

# -- local libraries and imports -- # 

class Network(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.config = client.config
    self.embed = client.embeds

  @commands.command(name='whois')
  async def iptrack(self, ctx, ip: str):
    if self.config['bot']['delete'] == 'on':
      await ctx.message.delete()
    r = requests.get(url=f"http://api.ipstack.com/{ip}?access_key=54082d4a5c4de095265ba3185db4c1f4")
    if r.status_code == 200:
        if(r.json()['type'] == None):
            await ctx.send(
          embed=self.embed.new_raw_embed(
            title=f"{ip} Is Invalid!"
          )
            )
        else:
            flag = f":flag_{r.json()['continent_code'].lower()}:"
            await ctx.send(
            embed=self.embed.new_raw_embed(
              title=f"{flag}  **WhoIS**  {flag}",
              description=f"IP | `{ip}`\n Type | `{r.json()['type']}`\n Continent | `{r.json()['continent_name']}`\n Continent Code | `{r.json()['continent_code']}`\n Country | `{r.json()['country_name']}`\n Country Code | `{r.json()['country_code']}`\n Region | `{r.json()['region_name']}`\n City | `{r.json()['city']}`\n Zip | `{r.json()['zip']}`\n Latitude | `{r.json()['latitude']}`\n Longitude | `{r.json()['longitude']}`"
            )
          )

# -- setup cog -- #
def setup(client):
  client.add_cog(Network(client))
