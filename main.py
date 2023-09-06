import settings, discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")

def run():
    print("Hello")
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix="$",intents=intents)

    @bot.event
    async def on_ready():
        logger.info(f"User: {bot.user} (ID: {bot.user.id})")
        logger.info("______________")

    @bot.event
    async def on_message(message):
        logger.info(f'Message from {message.author}: {message.content}')

        if message.content.startswith('$hello'):
            await message.channel.send('Hello World!')

    

    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
    