import discord
from discord.ext import commands
import asyncio
import datetime
import json
import requests


class purgeCog(commands.Cog):
    bot = commands.Bot(command_prefix='-')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='purge')
    @commands.has_any_role("Server Manager")
    async def clear(self,ctx, message, emoji):
        await ctx.channel.purge(limit=int(message))

def setup(bot):
    bot.add_cog(purgeCog(bot))  