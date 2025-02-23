from discord.ext import commands
from discord import app_commands
import controllers.weapons as wc
import discord
import typing

async def setup(bot : commands.Bot):
    await bot.add_cog(Weapons(bot))

class Weapons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command()
    async def show_weapon_list (self, ctx : commands.Context):
        """ Return a list of available weapons """
        
        fourstarweapon = await wc.get_weapon_list_based_on_quality(4)
        fivestarweapon = await wc.get_weapon_list_based_on_quality(5)
        
        field1 = ""
        field2 = ""

        fourindex = 1
        fiveindex = 1

        for weapon in fourstarweapon:
            field1 += f'{fourindex}. {weapon}\n'
            fourindex += 1
            
        for weapon in fivestarweapon:
            field2 += f'{fiveindex}. {weapon}\n'
            fiveindex += 1
            
        embed = discord.Embed(title = "Weapon List", description = "Here is the available weapon in the database")
        embed.add_field(name = "4 star weapons", value = field1, inline = False)
        embed.add_field(name = "5 star weapons", value = field2, inline = False)
            
        await ctx.send(embed = embed)
        
    @commands.hybrid_command()
    async def show_weapon(self, ctx : commands.Context, *, weapon_name : str):
        """ Return a description of the selected weapon """
        
        weapon = await wc.check_weapon(weapon_name)
        
        if weapon != None:
            id = await wc.get_weapon_id(weapon)
            embed = discord.Embed(title = weapon)
        else:
            await ctx.send(f'There is no weapon named {weapon_name} in the database')
            return
        
        weapon_type = await wc.get_weapon_type(id)
        quality = await wc.get_weapon_quality(id)
        stars = await wc.convert_quality_to_star(quality)
        base_attack = await wc.get_weapon_base_attack(id)
        secondary_attribute_type = await wc.get_secondary_attribute_type(id)
        secondary_attribute = await wc.get_secondary_attribute(id)
        weapon_description = await wc.get_weapon_description(id)
        weapon_skill_name = await wc.get_weapon_skill_name(id)
        weapon_skill_description = await wc.get_weapon_skill_description(id)
        weapon_icon = await wc.get_weapon_icon(id)
        embed_color = await wc.get_color_based_on_quality(id)
        
        weapon_info_field = f'Name : {weapon}\nWeapon Type : {weapon_type}\nWeapon Quality : {stars}'
        weapon_base_stats_field = f'Base ATK : {base_attack}\nSecondary Attribute : {secondary_attribute} {secondary_attribute_type}'
        weapon_skill_field = f'{weapon_skill_description}'
        
        embed.description = weapon_description
        embed.color = embed_color
        embed.add_field(name = "Info", value = weapon_info_field, inline = False)
        embed.add_field(name = "Base Stats", value = weapon_base_stats_field, inline = False)
        embed.add_field(name = weapon_skill_name, value = weapon_skill_field, inline = False)
        embed.set_image(url = weapon_icon)
        embed.set_author(name= "Genshin Impact Fandom Wiki", url = "https://genshin-impact.fandom.com/wiki/Genshin_Impact_Wiki", icon_url= "https://static.wikia.nocookie.net/gensin-impact/images/e/e6/Site-logo.png/revision/latest?cb=20210723101020")
        
        await ctx.send(embed = embed)
            
    @show_weapon.autocomplete("weapon_name")
    async def character_autocomplete(
        self,
        ctx : commands.Context,
        current : str
    ) -> typing.List[app_commands.Choice[str]]:
        data = []
        weaponlist = await wc.get_weapon_list()
        for weapon in weaponlist:
            data.append(app_commands.Choice(name = weapon, value = weapon))
        return data