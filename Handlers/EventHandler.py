from Handlers.MessageHandler import MessageHandler
import settings, discord, datetime
from Commands import Informations, Tools
from discord.ext import commands
from Utilities import Utilities

logger = settings.logging.getLogger("bot")
global feedback_channel

class EventHandlers(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        global messageEventHandler
        global welcome_channel
        global rules_channel
        global general_channel
        global user_role
        global member_role


        get_notification_from_those_channel_names, all_server_text_channels, all_server_text_channels_object = Utilities.Utilities.get_channels(self.bot)
        all_roles_object, not_important_roles_objects = Utilities.Utilities.get_roles(self.bot)

        for text_channel in all_server_text_channels_object:
            if text_channel.name.lower() == 'welcome':
                welcome_channel = text_channel
                logger.info(f"channel '{text_channel.name}' assigned to {welcome_channel} variable")
            if text_channel.name.lower() == 'rules':
                rules_channel = text_channel
                logger.info(f"channel '{text_channel.name}' assigned to {rules_channel} variable")
            if text_channel.name.lower() == 'feedback':
                feedback_channel = text_channel
                logger.info(f"channel '{text_channel.name}' assigned to {feedback_channel} variable")
            if text_channel.name.lower() == 'general':
                general_channel = text_channel
                logger.info(f"channel '{text_channel.name}' assigned to {general_channel} variable")
        if get_notification_from_those_channel_names:
            messageEventHandler = MessageHandler(get_notification_from_those_channel_names[1])
        else:
            logger.warning(f"❌The \"{get_notification_from_those_channel_names}\" channel(s) w not found.")

        for role in all_roles_object:
            if role.name.lower() == 'user':
                user_role = role
                logger.info(f'Role {role} assigned to a variable user_role')
            if role.name.lower() == 'member':
                member_role = role
                logger.info(f'Role {role} assigned to a variable member_role')
            if member_role == None:
                logger.error('❌member_role not assigned')
            if user_role == None:
                logger.error('❌user_role not assigned')


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
        #await self.bot.process_commands(message)
        if messageEventHandler is not None and not message.content.startswith('$'):
            await messageEventHandler.on_message(message, author_roles_names)
        else:
            logger.warning("❌MessageEventHandler is null or The message starts with '$'. Ommitting message notification.")
  
    @commands.Cog.listener()
    async def on_member_join(self, member):
        logger.info(f"User \'{member.name}\' has joined the server!")
        if welcome_channel is not None:
            welcome_message = (
                        f"🎉 **Welcome to the server, {member.mention}!** 🎉\n\n"
                        f"🌟 We're excited to have you as part of our coding community!🌟\n"
                        f"**Please change your nick to your first and last name 👤**, so that we can know who you are! 🤝\n"
                        f"If you have any questions, don't hesitate to ask here. Enjoy your time with us!"
                    )
            message_listener = await welcome_channel.send(welcome_message)
            await message_listener.add_reaction("👋")
        else:
            logger.warning("Welcome channel is not set!")


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if payload.channel_id == rules_channel.id:
            if payload.emoji.name == "✅":
                if user_role:
                    freshman = payload.member
                    if freshman:
                        await payload.member.add_roles(user_role, reason=f"Role assigned by Goniec because {payload.member.display_name} accepted the rules" )
                        logger.info(f"User '{freshman.name}' reacted to a welcome message and bot assigned to him role '{user_role}'")
            else:
                logger.info(f"Deleting react emoji in '{payload.channel_id}' for '{payload.member.display_name}' because it is other than '✅'")
                message = await rules_channel.fetch_message(payload.message_id)
                user = payload.member
                if user and message:
                    await message.remove_reaction(payload.emoji, user)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        logger.info(f"User \'{member.name}\' has left the server :((")
        if welcome_channel is not None:
            farewell_message = (
                f"😢 **{member.display_name} has left the server.**\n\n"
                f"We'll miss you! If you ever decide to return, you're always welcome here. "
                f"Take care!👋 "
            )
            await welcome_channel.send(farewell_message)
        else:
            logger.warning("Welcome channel is not set!")

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        channel = before.channel or after.channel
        if "Meetings" in channel.name: # Insert voice channel ID
            if (before.channel is None and after.channel is not None): # Member joins the defined channel
                await general_channel.send(f"{member.display_name} joined voice channel {channel.name}")
            elif ("Meetings" in channel.name) and (before.channel != after.channel):
                await general_channel.send(f"{member.display_name} joined voice channel {after.channel.name}")

async def setup(bot):
    await bot.add_cog(EventHandlers(bot))