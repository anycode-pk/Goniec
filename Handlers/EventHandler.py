from Handlers.MessageHandler import MessageHandler
import settings, discord
from Commands import CommandManager
from discord.ext import commands
from Utilities import Utilities

logger = settings.logging.getLogger("bot")

class EventHandlers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global messageEventHandler
        global welcome_channel
        global rules_channel

        get_notification_from_those_channel_names, all_server_text_channels, all_server_text_channels_object = Utilities.Utilities.get_channels(self.bot)
        all_roles_object, not_important_roles_objects = Utilities.Utilities.get_roles(self.bot)

        for text_channel in all_server_text_channels_object:
            if text_channel.name.lower() == 'welcome':
                welcome_channel = text_channel
            if text_channel.name.lower() == 'rules':
                rules_channel = text_channel
        if get_notification_from_those_channel_names:
            messageEventHandler = MessageHandler(get_notification_from_those_channel_names[1])
        else:
            logger.warning(f"❌The \"{get_notification_from_those_channel_names}\" channel(s) w not found.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        author_roles_names = Utilities.Utilities.get_author_roles(message)
        if any([author_role_name in author_roles_names for author_role_name in Utilities.defined_not_important_roles]):
            not_important_author_roles = [role for role in author_roles_names if role in Utilities.defined_not_important_roles]
            logger.warning(f"❌{message.author.display_name} of message has ({len(not_important_author_roles)}) not important role(s): {not_important_author_roles}. Ommitting message.")
            return
        logger.info(f"{message.author.display_name} of message has ({len(author_roles_names)}) role(s) and they are important: {author_roles_names}")
        await self.bot.process_commands(message)
        if messageEventHandler is not None and not message.content.startswith('$'):
            await messageEventHandler.on_message(message, author_roles_names)
        else:
            logger.warning("❌MessageEventHandler is null or The message starts with '$'. Ommitting message notification.")
  
    @commands.Cog.listener()
    async def on_member_join(self, member):
        logger.info(f"User \'{member.name}\' has joined the server!")
        if welcome_channel is not None:
            welcome_message = (
                        f"👋 **Welcome to the server, {member.mention}!** 🎉\n\n"
                        f"🌟 We're excited to have you as part of our community. "
                        f"Please take a moment to read the rules in {rules_channel.mention} and feel free to introduce yourself in the chat. "
                        f"**Please change your nick to your first and last name 👤**, so that we can know who you are! 🤝"
                        f"If you have any questions, don't hesitate to ask. Enjoy your time here! 😊"
                    )            
            await welcome_channel.send(welcome_message)
        else:
            logger.warning("Welcome channel is not set!")

    @commands.Cog.listener()
    async def on_member_remove(self, member):
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


async def setup(bot):
    await bot.add_cog(EventHandlers(bot))