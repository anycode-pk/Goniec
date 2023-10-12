import discord, settings, json
from Interfaces.FacebookInterface import FacebookInterface

logger = settings.logging.getLogger("bot")

class MessageHandler:
    
    def __init__(self, notifications_channel):
        self.notifications_channel = notifications_channel
        self.fb_interface = FacebookInterface()

    # async def send_notification_str(self, message):
    #     logger.info(f'(str)Message from \'{message.author.display_name}\' in channel \'{message.channel}\' with content \'{message.content}\'')
    #     message_content = self.format_message_for_str(message)
    #     return await self.notifications_channel.send(f'\'{message.author.display_name}\' in channel \'{message.channel}\' with content \'{message_content}\'')
        
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

        message_json = json.dumps(message_obj, indent=4, separators=(". ", " = "), ensure_ascii=False)
        logger.info(f"Sending message json:")
        logger.info(message_json)
        #return await self.notifications_channel.send(message_json)
        self.fb_interface.broadcast_message(message_obj)

    
    def format_message_for_str(self, message):
        message_words = message.content.split()
        if len(message_words) > 10:
            message_content = ' '.join(message_words[:10]) + '...'
        else:
            message_content = message.content
        return message_content
    
    async def on_message(self, message, author_roles_names):
        #await self.send_notification_str(message)
        await self.send_notification_json(message, author_roles_names)

# TO-DO:

# dodaj komendy:
# '-history' history of our organization
# '-members' info about our members

# sprawdz czy rola "Freshman" (swiezak) moze ustawiac sobie nick 

# wyslij obrazek podczas witania nowych czlonkow