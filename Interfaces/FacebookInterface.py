# underscored functions not to be used outside the class
# fun fact: python doesnt have private funcs!

import json
import settings
import requests

logger = settings.logging.getLogger("bot")

class FacebookInterface():
    def __init__(self):
        # set up stuff like api keys and user ids here
        self.fbpage_api_access_token = settings.FBPAGE_API_SECRET
        self.fbpage_page_id = settings.FBPAGE_ID

        # should this be set up here or in env?
        self.fb_user_id_list = []
        self.fb_graph_endpoint = "https://graph.facebook.com/v18.0/" + self.fbpage_api_key
    pass

    # string helpers

    # i yoinked this from paul
    def _trim_message_content(self, message):
        message_words = message.content.split()
        if len(message_words) > 10:
            message_trimmed = ' '.join(message_words[:10]) + '...'
        else:
            message_trimmed = message.content
        return message_trimmed


    def _format_message(self, message_json):
        message_trimmed = self._trim_message_content(message_json.content)
        return f"{message_json.author} ({message_json.channel}): {message_trimmed}"

    # https helpers

    def _create_message_payload(self, message_string, user_id):
        fb_payload_json = {
                "recipient" = "\{id:{user_id}\}",
                "message" = message_string,
                "access_token" = self.fbpage_api_access_token
                }
        return fb_payload_json

    def _fb_graph_post(self, fb_payload_json, endpoint_suffix):
        return requests.get(self.fb_graph_endpoint + endpoint_suffix, json=fb_payload_json)
    
    def _fb_graph_post(self, fb_payload_json, endpoint_suffix):
        requests.post(self.fb_graph_endpoint + endpoint_suffix, json=fb_payload_json)


    # actual interface

    async def fb_send_privmessage(self, message_json, user_id):
        logger.info(f"{__name__}: sending private message to Facebook user {user_id}")
        message_string = self._format_message(message_json)
        payload_json = self._create_message_payload(message_string, user_id) 
        try:
            self._fb_graph_post(payload_json, "messages")
        except:
            logger.error(f"{__name__}: could not send message to Facebook user {user_id}")
        return 


    async def fb_broadcast_message(self, message_json):
        logger.info(f"{__name__}: received message broadcast request")
        
        for user_id in self.fb_user_id_list:
            self.fb_send_privmessage(message_json, user_id)

        logger.info(f"{__name__}: broadcast finished")
        return 
