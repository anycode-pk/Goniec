from Handlers.MessageHandler import MessageHandler
import settings, discord
from discord.ext import commands

logger = settings.logging.getLogger("bot")
messageEventHandler = None

defined_not_important_roles = ["Świeżak", "GameDev", "dupa"]
all_roles = []
all_server_text_channels_object = []

def run():
    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    bot = commands.Bot(command_prefix="$",intents=intents)
            
    @bot.command(
        aliases=['i'],
        help="Info about AnyCode",
        description="",
        brief="Info about AnyCode"
    )
    async def info(ctx):
        """Info about AnyCode"""
        logger.info("Executting command $info...")
        await ctx.send("We are student science club \'AnyCode\' at the Koszalin University of Technology")

    @bot.command(
        aliases=['his'],
        help="History of AnyCode",
        description="",
        brief="History of AnyCode"
    )
    async def history(ctx):
        """History of AnyCode"""
        logger.info("Executting command $history...")
        await ctx.send("This is history of our club:")

    @bot.event
    async def on_ready():
        global messageEventHandler
        global welcome_channel
        global rules_channel

        get_notification_from_those_channel_names, all_server_text_channels, all_server_text_channels_object = get_channels(bot)
        all_roles_object, not_important_roles_objects = get_roles()
        for text_channel in all_server_text_channels_object:
            if text_channel.name.lower() == 'welcome':
                welcome_channel = text_channel
            if text_channel.name.lower() == 'rules':
                rules_channel = text_channel
        if get_notification_from_those_channel_names:
            messageEventHandler = MessageHandler(get_notification_from_those_channel_names[1])
        else:
            logger.warning(f"❌The \"{get_notification_from_those_channel_names}\" channel(s) w not found.")

    @bot.event
    async def on_member_join(member):
        logger.info(f"User \'{member.name}\' has joined the server!")
        if welcome_channel is not None:
            welcome_message = (
                        f"👋 **Welcome to the server, {member.mention}!** 🎉\n\n"
                        f"🌟 We're excited to have you as part of our community. "
                        f"Please take a moment to read the rules in {rules_channel.mention} and feel free to introduce yourself in the chat. "
                        f"If you have any questions, don't hesitate to ask. Enjoy your time here! 😊"
                    )            
            await welcome_channel.send(welcome_message)
        else:
            logger.warning("Welcome channel is not set!")

    @bot.event
    async def on_member_remove(member):
        logger.info(f"User \'{member.name}\' has left the server :((")
        if welcome_channel is not None:
            farewell_message = (
                f"😢 **{member.display_name} has left the server.**\n\n"
                f"👋 We'll miss you! If you ever decide to return, you're always welcome here. "
                f"Feel free to stay in touch with us. Take care!"
            )
            await welcome_channel.send(farewell_message)
        else:
            logger.warning("Welcome channel is not set!")

    def get_channels(bot):
        get_notification_from_those_channel_names = ["announcements-all", "info-member", "staże", "member-only-chat", "chess-robot", 
                                      "apka", "table-booking-app", "whiteboard-photos", "spotkania", "game-dev", 
                                      "enterprise", "mobile-dev", "wycieczka", "priv-debata", "inter-chat"]
        notification_channels = []
        all_server_text_channels = []
        all_server_text_channels_object = []
        i = 0

        for guild in bot.guilds:
            for channel in guild.text_channels:
                all_server_text_channels_object.append(channel)
                all_server_text_channels.append(channel.name)
                if channel.name in get_notification_from_those_channel_names:
                    notification_channels.append(channel)
        logger.info(f"✅Important channel list({len(notification_channels)}): \"{', '.join(channel.name for channel in notification_channels)}\" were found in server!")
        logger.info(f"All text server channel list({len(all_server_text_channels)}): \"{', '.join(channel for channel in all_server_text_channels)}\".")

        return notification_channels, all_server_text_channels, all_server_text_channels_object

    
    @bot.event
    async def on_message(message):
        if message.author == bot.user:
            return
        author_roles_names = get_author_roles(message)
        if any([author_role_name in author_roles_names for author_role_name in defined_not_important_roles]):
            not_important_author_roles = [role for role in author_roles_names if role in defined_not_important_roles]
            logger.warning(f"❌{message.author.display_name} of message has ({len(not_important_author_roles)}) not important role(s): {not_important_author_roles}. Ommitting message.")
            return
        logger.info(f"{message.author.display_name} of message has ({len(author_roles_names)}) role(s) and they are important: {author_roles_names}")
        await bot.process_commands(message)
        if messageEventHandler is not None and not message.content.startswith('$'):
            await messageEventHandler.on_message(message, author_roles_names)
        else:
            logger.warning("❌MessageEventHandler is null or The message starts with '$'. Ommitting message notification.")

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
        return [role.name for role in message.author.roles if role.name != '@everyone'] 
    
    bot.run(settings.DISCORD_API_SECRET, root_logger=True)

if __name__ == "__main__":
    run()
    