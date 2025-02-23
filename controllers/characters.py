import connections.dbConnect as db
from discord.ext import commands

@commands.hybrid_command()
async def get_characters_list(ctx):
    mycursor = await db.Connect()
    
    sql = "SELECT char_name FROM characters"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    charlist = []
    for char in myresult:
        charlist += char
    mycursor.close()
    
    await ctx.send(charlist)

async def setup(bot):
    bot.add_command(get_characters_list)