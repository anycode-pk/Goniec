from Handlers.MessageHandler import MessageHandler
import settings, discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")
messageEventHandler = None

defined_not_important_roles = ["Świeżak", "GameDev", "dupa"]
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

        get_notification_from_those_channel_names, all_server_text_channels = get_channels(bot)
        all_roles_object, not_important_roles_objects = get_roles()
        
        if get_notification_from_those_channel_names:
            messageEventHandler = MessageHandler(get_notification_from_those_channel_names[1])
        else:
            logger.warning(f"❌The \"{get_notification_from_those_channel_names}\" channel(s) w not found.")
        
    def get_channels(bot):
        get_notification_from_those_channel_names = ["announcements-all", "info-member", "staże", "member-only-chat", "chess-robot", 
                                      "apka", "table-booking-app", "whiteboard-photos", "spotkania", "game-dev", 
                                      "enterprise", "mobile-dev", "wycieczka", "priv-debata", "inter-chat"]
        notification_channels = []
        all_server_text_channels = []
        i = 0

        for guild in bot.guilds:
            for channel in guild.text_channels:
                all_server_text_channels.append(channel.name)
                if channel.name in get_notification_from_those_channel_names:
                    notification_channels.append(channel)
        logger.info(f"✅Important channel list({len(notification_channels)}): \"{', '.join(channel.name for channel in notification_channels)}\" were found in server!")
        logger.info(f"All text server channel list({len(all_server_text_channels)}): \"{', '.join(channel for channel in all_server_text_channels)}\".")

        return notification_channels, all_server_text_channels

    
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        if message.content.startswith('$'):
            logger.info("The message starts with '$'. Ommitting message.")
            return
        author_roles_names = get_author_roles(message)
        if any([author_role_name in author_roles_names for author_role_name in defined_not_important_roles]):
            not_important_author_roles = [role for role in author_roles_names if role in defined_not_important_roles]
            logger.warning(f"❌{message.author.display_name} of message has ({len(not_important_author_roles)}) not important role(s): {not_important_author_roles}. Ommitting message.")
            return
        logger.info(f"{message.author.display_name} of message has ({len(author_roles_names)}) role(s) and they are important: {author_roles_names}")
        if author_roles_names in defined_not_important_roles:
            logger.info(f"{message.author.display_name} has role '{message.author.role}'. Ommitting message.")
            return
        if messageEventHandler is not None:
            await messageEventHandler.on_message(message)
        else:
            logger.warning("❌MessageEventHandler is null")    
        await bot.process_commands(message)

    def get_roles():
        all_roles_objects = []
        all_roles = []
        not_important_roles_objects = []
        not_found_important_roles = []

        logger.info(f"Declared not important roles list: {defined_not_important_roles}")
        for guild in bot.guilds:
            for role in guild.roles:
                all_roles_objects.append(role)
                all_roles.append(role.name)
                if role.name in defined_not_important_roles:
                    not_important_roles_objects.append(role)
                    not_found_important_roles.append(role.name)
                    logger.info(f"✅not_important_role: '{role.name}' found in server.")

        roles_wrongly_declared = [role for role in defined_not_important_roles if role not in all_roles]
        logger.info(f"❌Wrongly declared not important roles: {roles_wrongly_declared}")

        logger.info(f"✅All server roles ({len(all_roles)}): {', '.join([role.name for role in all_roles_objects])}")
        return all_roles_objects, not_important_roles_objects
    
    def get_author_roles(message):
        return [role.name for role in message.author.roles] 
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
    