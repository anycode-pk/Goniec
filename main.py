from Handlers import MessageHandler, EventHandler
import settings, discord
from Commands import Informations, Tools
from Utilities import Utilities, GoniecHelpCommand
from discord.ext import commands
import asyncio



logger = settings.logging.getLogger("bot")
messageEventHandler = None
defined_not_important_roles = ["Świeżak", "GameDev", "dupa"]
all_roles = []
all_server_text_channels_object = []

async def run():
    global bot
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="$",intents=intents)
    await bot.add_cog(Informations.Informations(bot))
    await bot.add_cog(Tools.Tools(bot))
    await bot.add_cog(Utilities.Utilities(bot))
    await bot.add_cog(EventHandler.EventHandlers(bot))
    await bot.add_cog(GoniecHelpCommand.GoniecHelp(bot))

if __name__ == "__main__":
    asyncio.run(run()) 
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)
