import discord
from connections import dbConnect as db

mycursor = db.mycursor

# DONE : Get artefacts list
async def get_artefact_list():
    sql = "SELECT set_name FROM artefacts"


    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    artelist = []
    for arte in myresult:
        artelist += arte
    artelist.sort()
    
    return artelist

# TODO : Check for artefact
async def check_artefact(set_name : str):
    wildcard = f'%{set_name}%'
    
    sql = "SELECT set_name FROM artefacts WHERE set_name LIKE %s"
    setname = (wildcard, )

    mycursor.execute(sql, setname)
    myresult = mycursor.fetchone()
    
    if myresult != None:
        name = ""
        for r in myresult:
            name += r
        return name
    else:
        return None


# DONE : Get weapon id
async def get_id(set_name : str):
    sql = "SELECT id FROM artefacts WHERE set_name = %s"
    setname = (set_name, )

    mycursor.execute(sql, setname)
    myresult = mycursor.fetchone()
    
    id = 0
    for result in myresult:
        id += result
    
    return id

# DONE : Get set name
async def get_name(id : int):
    sql = "SELECT set_name FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    name = ""
    for result in myresult:
        name += result
    
    return name

# DONE : Get quality
async def get_quality(id : int):
    sql = "SELECT quality FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()
    
    quality = ""
    for result in myresult:
        quality += result
        
    return quality

async def get_artefacts_based_on_quality(quality : str):
    sql = "SELECT set_name FROM artefacts WHERE quality = %s"
    _quality = (quality, )

    mycursor.execute(sql, _quality)
    myresult = mycursor.fetchall()

    res = []
    for result in myresult:
        res += result
    res.sort()
        
    return res

# DONE : Get 2 piece bonus
async def get_2pc_bonus(id : int):
    sql = "SELECT 2_set_bonus FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    desc = ""
    for result in myresult:
        desc += result
    
    return desc

# DONE : Get 4 piece bonus
async def get_4pc_bonus(id : int):
    sql = "SELECT 4_set_bonus FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    desc = ""
    for result in myresult:
        desc += result
    
    return desc

async def get_flower_name(id : int):
    sql = "SELECT flower_name FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_flower_icon(id : int):
    sql = "SELECT flower_icon FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_plume_name(id : int):
    sql = "SELECT plume_name FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_plume_icon(id : int):
    sql = "SELECT plume_icon FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_sands_name(id : int):
    sql = "SELECT sands_name FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_sands_icon(id : int):
    sql = "SELECT sands_icon FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_goblet_name(id : int):
    sql = "SELECT goblet_name FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_goblet_icon(id : int):
    sql = "SELECT goblet_icon FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_circlet_name(id : int):
    sql = "SELECT circlet_name FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res

async def get_circlet_icon(id : int):
    sql = "SELECT circlet_icon FROM artefacts WHERE id = %s"
    _id = (id, )

    mycursor.execute(sql, _id)
    myresult = mycursor.fetchone()

    res = ""
    for result in myresult:
        res += result
    
    return res