import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

channel_id = os.getenv('TARGET_CHANNEL_ID')

role_id = os.getenv('TARGET_ROLE_ID')
