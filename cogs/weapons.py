from discord.ext import commands
from discord import app_commands
import controllers.weapons as wc
import discord
import typing
import connections.webhook as wb

async def setup(bot : commands.Bot):
    await bot.add_cog(Weapons(bot))

class Weapons(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.hybrid_command()
    async def show_weapon_list (self, ctx : commands.Context):
        """ Return a list of available weapons """
        
        onestarweapon = await wc.get_weapon_list_based_on_quality(1)
        twostarweapon = await wc.get_weapon_list_based_on_quality(2)
        threestarweapon = await wc.get_weapon_list_based_on_quality(3)
        fourstarweapon = await wc.get_weapon_list_based_on_quality(4)
        fivestarweapon = await wc.get_weapon_list_based_on_quality(5)
        
        field1 = ""
        field2 = ""
        field3 = ""
        field4 = ""
        field5 = ""

        oneindex = 1
        twoindex = 1
        threeindex = 1
        fourindex = 1
        fiveindex = 1

        for weapon in onestarweapon:
            field1 += f'{oneindex}. {weapon}\n'
            oneindex += 1
            
        for weapon in twostarweapon:
            field2 += f'{twoindex}. {weapon}\n'
            twoindex += 1
        
        for weapon in threestarweapon:
            field3 += f'{threeindex}. {weapon}\n'
            threeindex += 1

        for weapon in fourstarweapon:
            field4 += f'{fourindex}. {weapon}\n'
            fourindex += 1
            
        for weapon in fivestarweapon:
            field5 += f'{fiveindex}. {weapon}\n'
            fiveindex += 1
            
        data = {
            "embeds": [
                {
                    "title": "WEAPON LIST"
                },
                {
                    "title": "1 STAR WEAPONS",
                    "description": field1
                },
                {
                    "title": "2 STAR WEAPONS",
                    "description" : field2
                },
                {
                    "title": "3 STAR WEAPONS",
                    "description" : field3
                },
                {
                    "title": "4 STAR WEAPONS",
                    "description" : field4
                },
                {
                    "title": "5 STAR WEAPONS",
                    "description" : field5
                }
            ],
                "username": "[/] BUFF_VelloImpact",
                "attachments": []
            }
        
        await ctx.send("Showing List....")
        if await wb.PostWebhook(data) == False:
            await ctx.send("Failed to Get the list. Please try again in a few moments")
        
    async def weapon_autocomplete(
        self,
        ctx : commands.Context,
        current : str
    ) -> typing.List[app_commands.Choice[str]]:
        data = []
        weaponlist = await wc.get_weapon_list()
        for weapon in weaponlist:
            if current.lower() in weapon.lower():
                data.append(app_commands.Choice(name = weapon, value = weapon))
        return data[:25]        

    @commands.hybrid_command()
    @app_commands.autocomplete(weapon_name = weapon_autocomplete)
    async def show_weapon(self, ctx : commands.Context, *, weapon_name : str):
        """ Return a description of the selected weapon """
        
        weapon = await wc.check_weapon(weapon_name)
        
        if weapon != None:
            id = await wc.get_weapon_id(weapon)
            embed = discord.Embed(title = f'Genshin Impact Fandom Wiki | Weapons | {weapon_name}')
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
        embed.add_field(name = "WEAPON INFO", value = weapon_info_field, inline = False)
        embed.add_field(name = "WEAPON STATS", value = weapon_base_stats_field, inline = False)
        embed.add_field(name = f'PASSIVE SKILL : {weapon_skill_name}', value = weapon_skill_field, inline = False)
        embed.set_image(url = weapon_icon)
        embed.set_footer(text = "Data collected from Genshin Impact Fandom Wiki", icon_url = "https://static.wikia.nocookie.net/6a181c72-e8bf-419b-b4db-18fd56a0eb60")
        
        await ctx.send(embed = embed)