import settings, discord
from Commands import CommandManager
from discord.ext import commands

logger = settings.logging.getLogger("bot")
defined_not_important_roles = ["Freshman", "Game Developer", "dupa", "User", "USER"]
all_roles = []
all_server_text_channels_object = []
messageEventHandler = None

class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

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

    def get_roles(bot):
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
    
def setup(bot):
    bot.add_cog(Utilities(bot))