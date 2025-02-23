from discord.ext import commands
from discord import app_commands
import controllers.characters as cc
import discord
import typing

async def setup(bot : commands.Bot):
    await bot.add_cog(Characters(bot))

class Characters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Added
    @commands.hybrid_command()
    async def get_characters_list(self, ctx : commands.Context):
        """ Return list of characters in the database """
        clist = await cc.get_characters_list()
        cl = ""
        i = 1
        
        for c in clist:
            cl += f'{i}. {c}\n'
            i += 1
            
        embed = discord.Embed(title = "Character List Test")
        embed.add_field(name = "list", value = cl, inline = False)
            
        await ctx.send(embed = embed)
        
    # Added
    @commands.hybrid_command()
    async def show_character(self, ctx : commands.Context, *, char_name : str):
        """ show a character based on [char_name] """
        
        name = await cc.check_character(char_name)
        
        if name != None:
            embed = discord.Embed(title=name)
        else:
            await ctx.send(f'Theres no character named : {char_name} in the database')
            return
        
        id = await cc.get_character_id(name)
        desc = await cc.get_character_description(id)
        constelation = await cc.get_character_constelation_name(id)
        icon = await cc.get_character_icon(id)
        color = await cc.get_element_color(id)
        element = await cc.get_character_element(id)
        weapon = await cc.get_character_weapon(id)
        quality = await cc.get_character_quality(id)
        
        field1 = f'Name : {name}\nElement : {element}\nConstelation : {constelation}\nQuality : {quality} star\nWeapon : {weapon}'
        
        embed.colour = color
        embed.description = desc
        embed.set_thumbnail(url = "https://static.wikia.nocookie.net/gensin-impact/images/e/e6/Site-logo.png/revision/latest?cb=20210723101020")
        embed.set_image(url = icon)
        embed.set_author(name= "Genshin Impact Fandom Wiki", url = "https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki", icon_url= "https://static.wikia.nocookie.net/gensin-impact/images/e/e6/Site-logo.png/revision/latest?cb=20210723101020")
        embed.add_field(name = f'About {name}', value = field1, inline = False)
        
        await ctx.send(embed=embed)
        
    # Added
    @show_character.autocomplete("char_name")
    async def character_autocomplete(
        self, 
        ctx : commands.Context,
        current : str
    ) -> typing.List[app_commands.Choice[str]]:
        data = []
        charlist = await cc.get_characters_list()
        for char in charlist:
            data.append(app_commands.Choice(name = char, value = char))
        return data