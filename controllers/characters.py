import connections.dbConnect as db
import discord
    
async def get_characters_list():
    mycursor = await db.Connect()
    
    sql = "SELECT char_name FROM characters"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    charlist = []
    for char in myresult:
        charlist += char
    mycursor.close()
    
    return charlist

async def get_character_id(char_name : str):
    mycursor = db.Connect()
    
    sql = "SELECT id FROM characters WHERE char_name=%s"
    charname = (char_name, )
    
    mycursor.execute(sql, charname)
    myresult = mycursor.fetchone()
    
    id = 0
    for result in myresult:
        id += result
    mycursor.close()
        
    return id

async def check_character(char_name: str):
    mycursor = await db.Connect()
    
    wildcard = f'%{char_name}%'
    
    sql = "SELECT char_name FROM characters WHERE char_name LIKE %s"
    charname = (wildcard, )
    
    mycursor.execute(sql, charname)
    
    myresult = mycursor.fetchone()
    mycursor.close()
    
    if myresult != None:
        name = ""
        for r in myresult:
            name += r
        
        return name
    else:
        return None

async def get_character_name(id : int):
    mycursor = db.Connect()
    
    sql = "SELECT char_name FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    name = ""
    for result in myresult:
        name += result
    mycursor.close()
    
    return name

async def get_character_quality(id : int):
    mycursor = db.Connect()
    
    sql = "SELECT quality FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    quality = 0
    for result in myresult:
        quality += result
    mycursor.close()
        
    return quality

async def get_character_constelation_name(id: int):
    mycursor = db.Connect()
    
    sql = "SELECT constelation FROM characters WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    constelation = ""
    for result in myresult:
        constelation += result
    mycursor.close()
        
    return constelation

async def get_character_description(id: int):
    mycursor = db.Connect()
    
    sql = "SELECT char_desc FROM characters WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    desc = ""
    for result in myresult:
        desc += result
    mycursor.close()
        
    return desc

async def get_character_icon(id: int):
    mycursor = db.Connect()
    
    sql = "SELECT char_icon FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    url = ""
    for result in myresult:
        url += result
    mycursor.close()
    
    return url

async def get_character_card(id: int):
    mycursor = db.Connect()
    
    sql = "SELECT char_card FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    url = ""
    for result in myresult:
        url += result
    mycursor.close()
    
    return url

async def get_character_list_based_on_quality(quality : int):
    mycursor = await db.Connect()
    
    sql = "SELECT char_name FROM characters WHERE quality = %s"
    char_quality = (quality, )
    
    mycursor.execute(sql, char_quality)
    myresult = mycursor.fetchall()
    
    charlist = []
    for char in myresult:
        charlist += char
    mycursor.close()
    
    return charlist

#region element color
hydro = discord.Color.blue()
pyro = discord.Color.red()
geo = discord.Color.gold()
dendro = discord.Color.green()
electro = discord.Color.purple()
cryo = discord.Color.dark_grey()
anemo = discord.Color.teal()
#endregion
async def get_element_color(id: int):
    mycursor = db.Connect()
    
    sql = "SELECT element FROM characters WHERE id=%s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    element = ""
    mycursor.close()
    
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
    mycursor = db.Connect()
    
    sql = "SELECT element FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    element = ""
    for result in myresult:
        element += result
    mycursor.close()
    
    return element

async def get_character_weapon(id : int):
    mycursor = db.Connect()
    
    sql = "SELECT weapon_type FROM characters WHERE id=%s"
    _id = (id, )
    
    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    weapon = ""
    for result in myresult:
        weapon += result
    mycursor.close()
        
    return weapon