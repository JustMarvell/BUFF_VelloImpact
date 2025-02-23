import settings
import discord
from discord import app_commands
from discord.ext import commands

class Client(commands.Bot):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        # sync to a specific guild
        # [delete this comment] test_guild = discord.Object(id=...)  # change ... to your test guild_id
        # [and this] self.tree.copy_global_to(guild=test_guild)
        
        # load commands
        await load_command()
        
        # sync to all servers if no specification
        await self.tree.sync()
        
        
async def load_command():
    for cmd in settings.CONTROLER_COMMAND_DIR.glob("*.py"):
        if cmd.name != "__init__.py":
            print(f'{cmd.name} loaded')
            await client.load_extension(f'cotrollers.{cmd.name[:-3]}')
        
intents = discord.Intents.default()
intents.message_content = True
client = Client(intents=intents)

client.run(settings.DISCORD_API_SECRET)