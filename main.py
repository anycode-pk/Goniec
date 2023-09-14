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
        notification_channels = get_notification_channels(bot)

        if notification_channels:
            channel_names = ', '.join([f'"{channel}"' for channel in notification_channels])
            logger.info(f"✅The {channel_names} channel(s) were found!")
            messageEventHandler = MessageHandler(notification_channels)
        else:
            logger.warning(f"❌The \"{notification_channels}\" channel was not found.")

    def get_notification_channels(bot):
        notification_channel_names = ["notifications", "important-notify"]
        channels = []
        i = 0

        for guild in bot.guilds:
            for channel in guild.text_channels:
                i += 1
                logger.info(f"Channel {i}: {channel}")
                if channel.name in notification_channel_names:
                    logger.info(f"Returning channel: {channel}")
                    channels.append(channel)
        return channels

    
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if messageEventHandler is not None:
            await messageEventHandler.on_message(message)
        else:
            logger.warning("MessageEventHandler is null")    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
    