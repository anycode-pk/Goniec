from Handlers.MessageHandler import MessageHandler
import settings, discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")
messageEventHandler = None

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="$",intents=intents)

    # discord.User.display_name() ?? get names instead of name with ID
            
    @bot.event
    async def on_ready():
        global messageEventHandler
        notification_channel = get_notification_channel(bot)

        if notification_channel:
            logger.info(f"✅The \"{notification_channel}\" channel was found!")
            messageEventHandler = MessageHandler(notification_channel)
        else:
            logger.warning(f"❌The \"{notification_channel}\" channel was not found.")

    def get_notification_channel(bot):
        i=0
        for guild in bot.guilds:
            for channel in guild.text_channels:
                i += 1
                logger.info(f"Channel {i}: {channel}")
                if channel.name == "notifications":
                    logger.info(f"Returning channel: {channel}")
                    return channel
        return None

    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return  # Ignore messages from the bot
        if messageEventHandler is not None:
            await messageEventHandler.on_message(message)
        else:
            logger.warning("MessageEventHandler is null")    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
    