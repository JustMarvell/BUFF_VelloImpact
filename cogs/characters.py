from discord.ext import commands
from discord import app_commands
import controllers.characters as cc
import discord
import typing
import connections.webhook as wb
import random

async def setup(bot : commands.Bot):
    await bot.add_cog(Characters(bot))

class Characters(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Added
    @commands.hybrid_command()
    async def show_characters_list(self, ctx : commands.Context):
        """ Return a list of available characters """
        
        fourstarchar = await cc.get_character_list_based_on_quality(4)
        fivestarchar = await cc.get_character_list_based_on_quality(5)
        
        field1 = ""
        field2 = ""

        fourindex = 1
        fiveindex = 1

        for char in fourstarchar:
            field1 += f'{fourindex}. {char}\n'
            fourindex += 1
            
        for char in fivestarchar:
            field2 += f'{fiveindex}. {char}\n'
            fiveindex += 1
            
        data = {
            "embeds": [
                {
                    "title": "CHARACTER LIST"
                },
                {
                    "title": "4 STAR CHARACTERS",
                    "description": field1
                },
                {
                    "title": "5 STAR CHARACTERS",
                    "description" : field2
                }
            ],
                "username": "[/] BUFF_VelloImpact",
                "attachments": []
            }
        
        await ctx.send("Showing List....")
        if await wb.PostWebhook(data) == False:
            await ctx.send("Failed to Get the list. Please try again in a few moments")
        
    
    async def character_autocomplete(
        self, 
        ctx : commands.Context,
        current : str
    ) -> typing.List[app_commands.Choice[str]]:
        data = []
        charlist = await cc.get_characters_list()
        charlist.append('random')
        for char in charlist:
            if current.lower() in char.lower():
                data.append(app_commands.Choice(name = char, value = char))
        return data[:25]
    
    @commands.hybrid_command()
    @app_commands.autocomplete(char_name = character_autocomplete)
    async def show_character(self, ctx : commands.Context, *, char_name : str):
        """ show a character based on [char_name] or [random] to select random character """
        
    
        if char_name == 'random':
            lst = await cc.get_characters_list()
            c = len(lst) - 1
            r = random.randint(0, c)
            name = lst[r]
        else:
            name = await cc.check_character(char_name)
        
        if name != None:
            embed = discord.Embed(title=f'Genshin Impact Fandom Wiki | Characters | {name}')
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
        stars = await cc.convert_quality_to_star(quality)
        
        field1 = f'Name : {name}\nElement : {element}\nConstelation : {constelation}\nQuality : {stars}\nWeapon Type: {weapon}'
        
        embed.colour = color
        embed.description = desc
        embed.set_thumbnail(url = "https://static.wikia.nocookie.net/gensin-impact/images/e/e6/Site-logo.png/revision/latest?cb=20210723101020")
        embed.set_image(url = icon)
        embed.add_field(name = f'CHARACTER INFO', value = field1, inline = False)
        embed.set_footer(text = "Data collected from Genshin Impact Fandom Wiki", icon_url = "https://static.wikia.nocookie.net/6a181c72-e8bf-419b-b4db-18fd56a0eb60")
        
        await ctx.send(embed=embed)
        