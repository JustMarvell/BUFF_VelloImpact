from discord.ext import commands
from discord import app_commands
import controllers.artefacts as ac
import discord
import typing
import connections.webhook as wb

async def setup(bot : commands.Bot):
    await bot.add_cog(Artefacts(bot))

class Artefacts(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    # STILL ERROR : show artefact list
    @commands.hybrid_command()
    async def show_artefacts_list(self, ctx : commands.Context):
        """ Return a list of available artefacts """

        common = await ac.get_artefacts_based_on_quality("1-3")
        normal = await ac.get_artefacts_based_on_quality("3-4")
        rare = await ac.get_artefacts_based_on_quality("4-5")

        comfield = ""
        norfield = ""
        rarfield = ""

        comind = 1
        norind = 1
        rarind = 1

        for arte in common:
            comfield += f'{comind}. {arte}\n'
            comind += 1
            
        for arte in normal:
            norfield += f'{norind}. {arte}\n'
            norind += 1
            
        for arte in rare:
            rarfield += f'{rarind}. {arte}\n'
            rarind += 1
            
        data = {
            "embeds": [
                {
                    "title": "ARTEFACT LIST"
                },
                {
                    "title": "1-3  ⭐  ARTEFACTS",
                    "description": comfield
                },
                {
                    "title": "3-4  ⭐  ARTEFACTS",
                    "description" : norfield
                },
                {
                    "title" : "4-5  ⭐  ARTEFACTS",
                    "description" : rarfield
                }
            ],
                "username": "[/] BUFF_VelloImpact",
                "attachments": []
        }
        
        await ctx.send("Showing List....")
        if await wb.PostWebhook(data) == False:
            #await ctx.send("Failed to Get the list. Please try again in a few moments")
            await ctx.send(common)
            
    @commands.hybrid_command(pass_context = True)
    async def show_artefact(self, ctx : commands.Context, *, set_name : str):
        """ show an artefact set based on [set_name] """
        
        name = await ac.check_artefact(set_name)

        if name != None:
            embed = discord.Embed(title = f'Genshin Impact Fandom Wiki | Artefacts | {name}')
        else:
            await ctx.send(f'There is no artefact[s] named : {set_name} in the database')
            return
        
        id = await ac.get_id(name)
        quality = await ac.get_quality(id)
        bonus_2pc = await ac.get_2pc_bonus(id)
        bonus_4pc = await ac.get_4pc_bonus(id)
        flower_name = await ac.get_flower_name(id)
        flower_icon = await ac.get_flower_icon(id)
        plume_name = await ac.get_plume_name(id)
        plume_icon = await ac.get_plume_icon(id)
        sands_name = await ac.get_sands_name(id)
        sands_icon = await ac.get_sands_icon(id)
        goblet_name = await ac.get_goblet_name(id)
        goblet_icon = await ac.get_goblet_icon(id)
        circlet_name = await ac.get_circlet_name(id)
        circlet_icon = await ac.get_circlet_icon(id)

        field1 = f'Set Name : {name}\nQuality : {quality}\n'
        field2 = f'{bonus_2pc}\n'
        field3 = f'{bonus_4pc}\n'
        field4 = f'*Flower of Life :*\n{flower_name}\n*Plume of Death :*\n{plume_name}\n*Sands of Eon :*\n{sands_name}\n*Goblet of Eonothem :*\n{goblet_name}*\nCirclet of Logos :*\n{circlet_name}'

        embed.color = discord.Color.dark_gold()
        embed.set_thumbnail(url = "https://static.wikia.nocookie.net/gensin-impact/images/e/e6/Site-logo.png/revision/latest?cb=20210723101020")
        embed.add_field(name = f'ARTEFACT INFO', value = field1, inline = False)
        embed.add_field(name = f'2 PIECE BONUS :', value = field2, inline = False)
        embed.add_field(name = f'4 PIECE BONUS :', value = field3, inline = False)
        embed.add_field(name = name, value = field4, inline = False)
        embed.set_footer(text = "Data collected from Genshin Impact Fandom Wiki", icon_url = "https://static.wikia.nocookie.net/6a181c72-e8bf-419b-b4db-18fd56a0eb60")

        data = {
            "embeds": [
                {
                    "title": "Genshin Impact Fandom Wiki | Artefacts | {name}",
                    "color": None,
                    "fields": [
                        {
                            "name": "ARTEFACT INFO",
                            "value": "Set Name : name\nQuality : quality",
                            "inline": True
                        },
                        {
                            "name": "2 PIECE BONUS",
                            "value": "Geo DMG Bonus +15%",
                            "inline": True
                        },
                        {
                            "name": "4 PIECE BONUS",
                            "value": "Upon obtaining an Elemental Shard created through a Crystallize Reaction, all party members gain 35% DMG Bonus for that particular element for 10s. Only one form of Elemental DMG Bonus can be gained in this manner at any one time."
                        },
                        {
                            "name": "FLOWER OF LIFE",
                            "value": "Flower of Creviced Cliff"
                        }    
                    ],
                        "image": {
                        "url": "https://static.wikia.nocookie.net/gensin-impact/images/9/9f/Item_Flower_of_Creviced_Cliff.png/revision/latest?cb=20201120064841"
                    },
                        "thumbnail": {
                        "url": "https://static.wikia.nocookie.net/gensin-impact/images/e/e6/Site-logo.png/revision/latest?cb=20210723101020"
                    }
                },
                {
                    "url": "https://static.wikia.nocookie.net/gensin-impact/images/9/9f/Item_Flower_of_Creviced_Cliff.png/revision/latest?cb=20201120064841",
                    "color": None,
                    "fields": [
                        {
                            "name": "PLUME OF DEATH",
                            "value": "Feather of Jagged Peaks",
                            "inline": True
                        },
                        {
                            "name": "SANDS OF EON",
                            "value": "Sundial of Enduring Jade",
                            "inline": True
                        }
                    ],
                        "image": {
                        "url": "https://static.wikia.nocookie.net/gensin-impact/images/a/a5/Item_Feather_of_Jagged_Peaks.png/revision/latest?cb=20201120064919"
                    }
                },
                {
                    "url": "https://static.wikia.nocookie.net/gensin-impact/images/9/9f/Item_Flower_of_Creviced_Cliff.png/revision/latest?cb=20201120064841",
                    "image": {
                        "url": "https://static.wikia.nocookie.net/gensin-impact/images/1/1d/Item_Sundial_of_Enduring_Jade.png/revision/latest?cb=20201120064941"
                    }
                },
                {
                    "url": "https://static.wikia.nocookie.net/gensin-impact/images/0/02/Item_Goblet_of_Chiseled_Crag.png/revision/latest?cb=20201120064951",
                    "color": None,
                    "fields": [
                        {
                            "name": "GOBLET OF EONOTHEM",
                            "value": "Goblet of Chiseled Crag",
                            "inline": True
                        },
                        {
                            "name": "CIRCLET OF LOGOS",
                            "value": "Mask of Solitude Basalt",
                            "inline": True
                        }
                    ],
                    "image": {
                        "url": "https://static.wikia.nocookie.net/gensin-impact/images/0/02/Item_Goblet_of_Chiseled_Crag.png/revision/latest?cb=20201120064951"
                    }
                },
                {
                    "url": "https://static.wikia.nocookie.net/gensin-impact/images/0/02/Item_Goblet_of_Chiseled_Crag.png/revision/latest?cb=20201120064951",
                    "image": {
                        "url": "https://static.wikia.nocookie.net/gensin-impact/images/0/09/Item_Mask_of_Solitude_Basalt.png/revision/latest?cb=20201120065000"
                    }
                }
            ],
            
            "username": "[/] BUFF_VelloImpact",
            "attachments": []
            
            }

        #await ctx.send(embed = embed)
        await ctx.send(content="Sending Data")
        if await wb.PostWebhook(data) == False:
            await ctx.send("Failed to Get the list. Please try again in a few moments")