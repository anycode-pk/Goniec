from Handlers.MessageHandler import MessageHandler
import settings, discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")
messageEventHandler = None

not_important_roles = ["Świeżak", "GameDev"]
all_roles = []

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix="$",intents=intents)
    # discord.User.display_name() ?? get names instead of name with ID
            
    @bot.command(
        aliases=['i'],
        help="This is help",
        description="",
        brief="this is brief"
    )
    async def info(ctx):
        """dziwne"""
        logger.info("Executting command $info...")
        await ctx.send("test")

    @bot.event
    async def on_ready():
        global messageEventHandler
        notification_channels = get_notification_channels(bot)

        all_roles_object, not_important_roles = get_roles()
        logger.info(f"All server roles: {', '.join([role.name for role in all_roles_object])}")
        logger.info(f"Not important roles: ")


        
        if notification_channels:
            channel_names = ', '.join([f'"{channel}"' for channel in notification_channels])
            logger.info(f"✅The {channel_names} channel(s) were found!")
            messageEventHandler = MessageHandler(notification_channels[1])
        else:
            logger.warning(f"❌The \"{notification_channels}\" channel was not found.")
        

    def get_notification_channels(bot):
        notification_channel_names = ["announcements-all", "info-member", "staże", "member-only-chat", "chess-robot", 
                                      "apka", "table-booking-app", "whiteboard-photos", "spotkania", "game-dev", 
                                      "enterprise", "mobile-dev", "wycieczka", "priv-debata", "inter-chat"]
        notification_channels = []
        i = 0

        for guild in bot.guilds:
            for channel in guild.text_channels:
                i += 1
                logger.info(f"Channel {i}: {channel}")
                if channel.name in notification_channel_names:
                    logger.info(f"Returning channel: {channel}")
                    notification_channels.append(channel)
        return notification_channels

    
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content.startswith('$'):
            logger.info("The message starts with '$'. Ommitting message.")
            return
        if message.author.roles in not_important_roles:
            logger.info(f"{message.author.display_name} has role '{message.author.role}'. Ommitting message.")
            return
        if messageEventHandler is not None:
            await messageEventHandler.on_message(message)
        else:
            logger.warning("MessageEventHandler is null")    
        await bot.process_commands(message) # <- nie usuwac xdd

    def get_roles():
        all_roles = []
        not_important_roles_objects = []

        for guild in bot.guilds:
            for role in guild.roles:
                all_roles.append(role)
                if role.name in not_important_roles:
                    not_important_roles_objects.append(role)
        logger.info(f"Declared not important roles list: {not_important_roles}")
        for role_name in not_important_roles:
            logger.info(f"✅not_important_role: '{role_name}' found.")
        
        logger.warning(f"❌The following roles were not found: {', '.join(not_important_roles)}")
        return all_roles, not_important_roles
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
    