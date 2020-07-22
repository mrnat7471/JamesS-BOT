import discord
from discord.ext import commands
import asyncio
import datetime

TOKEN = 'NzI0NjczNDA3OTgzMTU3MzE5.XvDm6Q.Nbfn1uf2b_TsDE-7uKYF__gmFvM'
bot = commands.Bot(command_prefix = "-")
bot.remove_command("help")

extensions = ['Cogs.SayEmbedCog', 'Cogs.announceCog', 'Cogs.announcepingCog', 'Cogs.purgeCog', 'Cogs.helpCog']

#Events 
@bot.event
async def on_ready():
    print('Bot Online.')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="JamesS014 Community"))

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.channels, name="general")
    role = discord.utils.get(member.guild.roles, name="Member")
    embed = discord.Embed(colour=discord.Colour.blue(), description=f"{member.mention} joins the discord")
    embed.set_author(name='Member Joins', icon_url=bot.user.avatar_url)
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_thumbnail(url=member.avatar_url)   
    await audit.send(embed=embed)
    await channel.send(embed=embed)
    await member.add_roles(role)


#Commands
@bot.command()
async def load(extension):
    try:
        bot.load_extension(extension)
        print('Loaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be loaded [{}]'.format(extension, error))

@bot.command()
async def unload(extension):
    try:
        bot.unload_extension(extension)
        print('unLoaded {}'.format(extension))
    except Exception as error:
        print('{} cannot be unloaded [{}]'.format(extension, error))


if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print('{} cannot be loaded [{}]'.format(extension, error))

bot.run(TOKEN) 