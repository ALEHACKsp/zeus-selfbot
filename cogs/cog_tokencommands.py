"""
Authors: K1rk, and Charge.
Copyright: Zeus Selfbot Source Code (©)
"""

# -- standard libraries -- #
import requests, os, discord, json, numpy, numpy, smtplib, subprocess, sys, datetime, string
import random, time, ctypes, socket, re, colorama, time, asyncio

# -- non-standard libraries -- #
import discord
from discord.ext import commands
from discord.ext import tasks
from selenium import webdriver

# -- local libraries and imports -- # 

class tokencommands(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.embeds = client.embeds
    self.config = client.config


# -- setup cog -- #
def setup(client):
  client.add_cog(tokencommands(client))