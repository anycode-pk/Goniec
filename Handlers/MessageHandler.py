import discord, settings, json

logger = settings.logging.getLogger("bot")

class MessageHandler():
    def __init__(self, notifications_channel):
        self.notifications_channel = notifications_channel

    async def send_notification_str(self, message):
        message_content = self.format_message(message)
        return await self.notifications_channel.send(f'\'{message.author.display_name}\' in channel \
                                              \'{message.channel}\' with content \'{message_content}\'')
        
    async def send_notification_json(self, message):
        message_content = self.format_message(message)
        message_obj = {
            "author": message.author.display_name,
            "channel": message.channel,
            "content": message_content
        }

        message_json = json.dumps(message_obj)
        logger.info(f"Sending message json: {message_json}")
        return await self.notifications_channel.send(f'\'{message.author.display_name}\' in channel \
                                              \'{message.channel}\' with content \'{message_content}\'')
        

    def format_message(message):
        message_words = message.content.split()
        if len(message_words) > 10:
            message_content = ' '.join(message_words[:10]) + '...'
        else:
            message_content = message.content
        return message_content

    async def on_message(self, message):
        logger.info(f'Message from \'{message.author.display_name}\' in channel \'{message.channel}\' with content \'{message.content}\'')
        await self.send_notification_str(message)
        await self.send_notification_json(message)

# TO-DO:

# WYSLIJ JSON'A
# importujesz dwie biblioteki czy jedna i masz cztery metody

# jesli message od zarzadu, opiekunow - dodaj pattern
# jesli oznaczony @Czlonek to wtedy koniecznie wyslij powiadomienie.

# dodaj komende '--help' ktora daje info o bocie.
# powitanie nowych czlonkow
# dodaj komende historie kola

# what if has both role "swiezak" and "czlonek" ???