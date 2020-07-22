import discord
from discord.ext import commands
import asyncio
import datetime

class helpCog(commands.Cog):
    bot = commands.Bot(command_prefix='bhf.')
    bot.remove_command('help')

    def __init__(self, bot):
        self.bot = bot

    @bot.command(name='help')
    async def help(self, ctx):
        embed = discord.Embed(
            colour=discord.Colour.red(), 
            description="I don't know",
            title='Help!')
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_footer(text=f'Posted by {ctx.message.author.name}', icon_url=ctx.message.author.avatar_url)

        await ctx.channel.send(embed=embed)
            
        await ctx.message.delete()
def setup(bot):
    bot.add_cog(helpCog(bot)) 