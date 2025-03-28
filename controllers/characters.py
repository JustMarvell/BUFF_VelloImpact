import connections.dbConnect as db
import discord

mycursor = db.mycursor

#region element color
hydro = discord.Color.blue()
pyro = discord.Color.red()
geo = discord.Color.gold()
dendro = discord.Color.green()
electro = discord.Color.purple()
cryo = discord.Color.dark_grey()
anemo = discord.Color.teal()
#endregion

async def get_characters_list():
    sql = "SELECT char_name FROM characters"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    charlist = []
    for char in myresult:
        charlist += char
    charlist.sort()
    
    return charlist

async def get_character_id(char_name : str):
    sql = "SELECT id FROM characters WHERE char_name=%s"
    charname = (char_name, )
    
    mycursor.execute(sql, charname)
    myresult = mycursor.fetchone()
    
    id = 0
    for result in myresult:
        id += result
        
    return id

async def check_character(char_name: str):
    wildcard = f'%{char_name}%'
    
    sql = "SELECT char_name FROM characters WHERE char_name LIKE %s"
    charname = (wildcard, )
    
    mycursor.execute(sql, charname)
    
    myresult = mycursor.fetchone()
    
    if myresult != None:
        name = ""
        for r in myresult:
            name += r
        
        return name
    else:
        return None

async def get_character_name(id : int):
    sql = "SELECT char_name FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    name = ""
    for result in myresult:
        name += result
    
    return name

async def get_character_quality(id : int):
    sql = "SELECT quality FROM characters WHERE id=%s"
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

async def get_character_constelation_name(id: int):
    sql = "SELECT constelation FROM characters WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    constelation = ""
    for result in myresult:
        constelation += result
        
    return constelation

async def get_character_description(id: int):
    sql = "SELECT char_desc FROM characters WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    desc = ""
    for result in myresult:
        desc += result
        
    return desc

async def get_character_icon(id: int):
    sql = "SELECT char_icon FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    url = ""
    for result in myresult:
        url += result
    
    return url

async def get_character_card(id: int):
    sql = "SELECT char_card FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    url = ""
    for result in myresult:
        url += result
    
    return url

async def get_character_list_based_on_quality(quality : int):
    sql = "SELECT char_name FROM characters WHERE quality = %s"
    char_quality = (quality, )
    
    mycursor.execute(sql, char_quality)
    myresult = mycursor.fetchall()
    
    charlist = []
    for char in myresult:
        charlist += char
    charlist.sort()
    
    return charlist

async def get_element_color(id: int):
    sql = "SELECT element FROM characters WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    element = ""
    
    for result in myresult:
        element += result
    
    if element == "Hydro":
        return hydro
    elif element == "Pyro":
        return pyro
    elif element == "Electro":
        return electro
    elif element == "Anemo":
        return anemo
    elif element == "Cryo":
        return cryo
    elif element == "Geo":
        return geo
    elif element == "Dendro":
        return dendro

async def get_character_element(id : int):
    sql = "SELECT element FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    element = ""
    for result in myresult:
        element += result
    
    return element

async def get_character_weapon(id : int):
    sql = "SELECT weapon_type FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    weapon = ""
    for result in myresult:
        weapon += result
        
    return weapon