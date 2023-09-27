import discord, settings, json

logger = settings.logging.getLogger("bot")

class MessageHandler():
    def __init__(self, notifications_channel):
        self.notifications_channel = notifications_channel

    async def send_notification_str(self, message):
        logger.info(f'(str)Message from \'{message.author.display_name}\' in channel \'{message.channel}\' with content \'{message.content}\'')
        message_content = self.format_message_for_str(message)
        return await self.notifications_channel.send(f'\'{message.author.display_name}\' in channel \'{message.channel}\' with content \'{message_content}\'')
        
    async def send_notification_json(self, message, author_roles_names):
        logger.info(f'(json)Message from \'{message.author.display_name}\' in channel \'{message.channel}\' with content \'{message.content}\'')
        message_content = message.content
        mentioned_roles = message.mentions
        message_obj = {
            "author": message.author.display_name,
            "mentioned_roles": mentioned_roles,
            "channel": message.channel.name,
            "author_roles": author_roles_names,
            "content": message_content
        }

        message_json = json.dumps(message_obj, indent=4, separators=(". ", " = "), ensure_ascii=False)  # Use ensure_ascii=False to handle non-ASCII characters)
        logger.info(f"Sending message json:")
        logger.info(message_json)
        return await self.notifications_channel.send(message_json)
    
    def format_message_for_str(self, message):
        message_words = message.content.split()
        if len(message_words) > 10:
            message_content = ' '.join(message_words[:10]) + '...'
        else:
            message_content = message.content
        return message_content
    
    async def on_message(self, message, author_roles_names):
        await self.send_notification_str(message)
        await self.send_notification_json(message, author_roles_names)

# TO-DO:

# Dodaj komende '-history' historie kola
# Powitanie nowych czlonkow

# wyslij notification ze ktos dolaczyl.

# What if role changes? will it fetch new data? Or once started it will have those values? YES it fetches changes! :=D