# underscored functions not to be used outside the class
# fun fact: python doesnt have private funcs!

import json
import settings
import requests

logger = settings.logging.getLogger("bot")

class FacebookInterface():
    def __init__(self):
        self._page_access_token = settings.FB_PAGE_ACCESS_TOKEN
        self._page_id = settings.FB_PAGE_ID
        self._graph_endpoint = "https://graph.facebook.com/v18.0/" + self._page_id + "/"

    # string helpers

    # i yoinked this from paul
    # no problem, I yoinked this from ChatGPT 
    def _trim_message_content(self, message):
        message_words = message.split()
        if len(message_words) > 10:
            message_trimmed = ' '.join(message_words[:10]) + '...'
        else:
            message_trimmed = message
        return message_trimmed


    def _format_message(self, message_obj):
        message_trimmed = self._trim_message_content(message_obj['content'])
        return f"{message_obj['author']} ({message_obj['channel']}): {message_trimmed}"

    # http requests

    def _graph_get(self, payload_obj, endpoint_suffix):
        return requests.get(self._graph_endpoint + endpoint_suffix, params=payload_obj)
    
    def _graph_post(self, payload_obj, endpoint_suffix):
        return requests.post(self._graph_endpoint + endpoint_suffix, json=payload_obj)


    # request helper functions

    def _get_users(self):
        user_id_list = []
        payload = {
                "fields": "participants",
                "access_token": self._page_access_token
                }
        response = self._graph_get(payload, "conversations")
        users = response.json()
        for convo in users['data']:
            user_id_list.append(convo['participants']['data'][0]['id'])
        return user_id_list



    def _create_message_payload(self, message_string, user_id):
        payload_obj = {
                "recipient":  {
                    "id": user_id
                    },
                "message": {
                    "text": message_string
                    },
                "messaging_type": "MESSAGE_TAG",
                "tag": "CONFIRMED_EVENT_UPDATE",
                "access_token": self._page_access_token
                }
        return payload_obj
        
        fb_payload_json = json.dumps(fb_payload)
        return fb_payload_json


    # actual interface

    def send_privmessage(self, message_obj, user_id):
        logger.info(f"{__name__}: sending private message to Facebook user {user_id}")
        message_string = self._format_message(message_obj)
        payload_obj = self._create_message_payload(message_string, user_id) 
        try:
            response = self._graph_post(payload_obj, "messages")
        except:
            logger.error(f"{__name__}: could not send message to Facebook user {user_id}")
        return 


    def broadcast_message(self, message_obj):
        logger.info(f"{__name__}: received message broadcast request")
       
        user_id_list = self._get_users()
        for user_id in user_id_list:
            self.send_privmessage(message_obj, user_id)

        logger.info(f"{__name__}: broadcast finished")
        return 
