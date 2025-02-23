import settings
import discord
from discord import app_commands
from discord.ext import commands
from cogs.characters import Characters

class Client(commands.Bot):
    async def on_ready(self):
        # sync to a specific guild
        # [delete this comment] test_guild = discord.Object(id=...)  # change ... to your test guild_id
        # [and this] self.tree.copy_global_to(guild=test_guild)
        
        # load commands
        await load_command()
        
        # sync to all servers if no specification
        synced = await self.tree.sync()
        print(f'{len(synced)} commands sycned')
        
async def load_command():
    for cogs in settings.COGS_DIR.glob("*.py"):
        if cogs.name != "__init__.py":
            await client.load_extension(f'cogs.{cogs.name[:-3]}')
            print(f'{cogs.name} loaded')
        
intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)

client.run(settings.DISCORD_API_SECRET)