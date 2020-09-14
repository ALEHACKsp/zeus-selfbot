'''
Author: k1rk and charge
Copyright: Zeus Selfbot (c) inc.
'''

# -- 3rd party libraries -- #
import discord
from discord.ext import commands

def is_mem(member):
  '''checks if a user is discord.Member'''
  return isinstance(member, discord.Member)

def get_user(user, context, bot):
  '''attempts to get user from a string'''
  if not user:
    return
  if len(context.message.mentions) == 0:
      if not is_mem(user):
        return
      user = context.guild.get_member_named(user)
  else:
    user = context.message.mentions[0]
  if not user:
    user = context.guild.get_member(int(user))
  if not user:
    user = bot.get_user(int(user))
  if user:
    return user
