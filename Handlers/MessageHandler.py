import discord, settings

logger = settings.logging.getLogger("bot")

class MessageHandler():
    def __init__(self, notifications_channel):
        self.notifications_channel = notifications_channel

    async def notify(self, message):
        message_words = message.content.split()
        if len(message_words) > 10:
            message_content = ' '.join(message_words[:10]) + '...'
        else:
            message_content = message.content
        
        await self.notifications_channel.send(
            f'New message from \'{message.author}\' in channel \'{message.channel}\' with content \'{message_content}\'')

    async def on_message(self, message):
        logger.info(f'Message from \'{message.author}\' in channel \'{message.channel}\' {message.content}')
        await self.notify(message)

# to-do
# jesli message od zarzadu, opiekunow - dodaj pattern
# 
