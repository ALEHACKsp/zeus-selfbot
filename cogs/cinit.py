"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import sys
import logging
import asyncio

# -- non-standard libraries -- #
import discord
from discord.ext import commands

# -- local libraries and imports -- # 


class CogInit(commands.Cog):
  def __init__(self, client):
    '''
    The Main Cog with some default event listeners and basic commands
    Note: we wrap in try accept as we want errors to be caught and logged
    '''
    self.client = client
    self.config = client.config
    self.embed = client.embeds
  
  @commands.command(name='info')
  async def get_user_info(self, ctx, member: discord.User):
    await ctx.send(
      embed=self.embed.new_raw_embed(
        title="Found info",
        description=f"Showing profile info for: {member.mention}",
        fields=(
          ("Name", f"```{member.name}#{member.discriminator}```", True),
          ("ID", f"```{member.id}```", True),
          ("Friends", f"```{member.is_friend()}```", True),
          ("Created at", f"```{str(member.created_at).split()[0]}```", True)
        ), image_url=False,
      ), delete_after=self.config['embeds']['delete']
    )

  @commands.command(name='av')
  async def get_av(self, ctx, member: discord.Member):
    await ctx.send(
      embed=self.embed.new_raw_embed(
        title='Found profile picture',
        description=f'Showing profile picture for: {member.mention}',
        image_url=member.avatar_url
      ), delete_after=self.config['embeds']['delete']
    )

  @commands.command(name='spam')
  async def spam_ctx(self, ctx, count: int, *, msg: str):
    for _ in range(count):
      await ctx.send(msg)

  @commands.command(name='embedspam')
  async def spam_embed_ctx(self, ctx, count: int, *, msg: str):
    e = self.embed.new_default_config_embed(
      title=f"Spamming: {msg}",
      description=f"Spamming G"
    ) 
    for _ in range(count):
      await ctx.send(embed=e)

# -- setup cog -- #
def setup(client):
  client.add_cog(CogInit(client))

