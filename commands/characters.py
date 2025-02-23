import connections.dbConnect as db
from discord.ext import commands
import controllers.characters as cc
import discord

async def setup(bot):
    bot.add_command(get_characters_list)
    
# Added
@commands.hybrid_command()
async def get_characters_list(ctx):
    """ Return list of characters in the database """
    clist = await cc.get_characters_list()
    cl = ""
    i = 1
    
    for c in clist:
        cl += f'{i}. {cl}'
        i += 1
        
    embed = discord.Embed(title = "Character List Test")
    embed.add_field(name = "list", value = cl, inline = False)
        
    await ctx.send(embed = embed)
        