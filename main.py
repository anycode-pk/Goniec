import settings
import discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    print("Hello")
    intents = discord.Intents.default()
    bot = commands.Bot(command_prefix="!",intents=intents)
    #client = discord.Client()

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info("______________")
        #logger.info('Logged as client: {0.user}'.format(client))

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)
    #client.run(settings.DISCORD_API_SECRET)

if __name__ == "__main__":
    run()
    