#import connections.dbConnect as db
import discord
from connections import dbConnect as db

mycursor = db.mycursor
onestarcolor = discord.Color.greyple()
twostarcolor = discord.Color.dark_green()
threestarcolor = discord.Color.og_blurple()
fourstarcolor = discord.Color.purple()
fivestarcolor = discord.Color.gold()

async def get_weapon_list():
    sql = "SELECT weapon_name FROM weapons"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    weaponlist = []
    for weapon in myresult:
        weaponlist += weapon
        
    return weaponlist

async def get_weapon_list_based_on_quality(quality : int):
    sql = "SELECT weapon_name FROM weapons WHERE quality = %s"
    weaponquality = (quality, )
    
    mycursor.execute(sql, weaponquality)
    myresult = mycursor.fetchall()
    
    weaponlist = []
    for weapon in myresult:
        weaponlist += weapon
    
    return weaponlist

async def check_weapon(weapon_name: str):
    
    wildcard = f'%{weapon_name}%'
    
    sql = "SELECT weapon_name FROM weapons WHERE weapon_name LIKE %s"
    weaponname = (wildcard, )
    
    mycursor.execute(sql, weaponname)
    
    myresult = mycursor.fetchone()
    
    if myresult != None:
        name = ""
        for r in myresult:
            name += r
        
        return name
    else:
        return None
    
async def get_weapon_id(weapon_name : str):
    sql = "SELECT id FROM weapons WHERE weapon_name=%s"
    weaponname = (weapon_name, )
    
    mycursor.execute(sql, weaponname)
    myresult = mycursor.fetchone()
    
    id = 0
    for result in myresult:
        id += result
        
    return id

async def get_weapon_name(id : int):
    
    sql = "SELECT weapon_name FROM weapons WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    name = ""
    for result in myresult:
        name += result
        
    return name

async def get_weapon_type(id : int):
    
    sql = "SELECT weapon_type FROM weapons WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    weapon = ""
    for result in myresult:
        weapon += result
        
    return weapon

async def get_weapon_quality(id : int):
    sql = "SELECT quality FROM weapons WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    quality = 0
    for result in myresult:
        quality += result
        
    return quality

async def convert_quality_to_star(quality : int):
    star = "⭐"
    result = ""
    
    for i in range(quality):
        result += star
    
    return result

async def get_weapon_base_attack(id : int):
    sql = "SELECT base_attack FROM weapons WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    ba = 0                      # ba : Base Attack
    for result in myresult:
        ba += result
        
    return ba

async def get_secondary_attribute_type(id : int):
    
    sql = "SELECT secondary_attribute_type FROM weapons WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    sat = ""                    # sat : Secondary Attribute Type
    for result in myresult:
        sat += result
    
    return sat

async def get_secondary_attribute(id : int):
    
    sql = "SELECT secondary_attribute FROM weapons WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    sa = ""                    # sat : Secondary Attribute
    for result in myresult:
        sa += result
    
    return sa

async def get_weapon_description(id: int):
    
    sql = "SELECT weapon_description FROM weapons WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    desc = ""
    for result in myresult:
        desc += result
        
    return desc

async def get_weapon_skill_name(id: int):
    
    sql = "SELECT weapon_skill_name FROM weapons WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    wsn = ""                            # wsn : Weapon Skill Name
    for result in myresult:
        wsn += result
        
    return wsn

async def get_weapon_skill_description(id: int):
    
    sql = "SELECT weapon_skill_description FROM weapons WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    wsd = ""                            # wsd : Weapon Skill Description
    for result in myresult:
        wsd += result
        
    return wsd

async def get_weapon_icon(id: int):
    
    sql = "SELECT weapon_icon FROM weapons WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    icon = ""
    for result in myresult:
        icon += result
        
    return icon

async def get_color_based_on_quality(id : int):

    sql = "SELECT quality FROM weapons WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    quality = 0
    for result in myresult:
        quality += result
        
    if quality == 1:
        return onestarcolor
    elif quality == 2:
        return twostarcolor
    elif quality == 3:
        return threestarcolor
    elif quality == 4:
        return fourstarcolor
    elif quality == 5:
        return fivestarcolor