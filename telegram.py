import requests
import json
import logit


class telegramBot:

    def __init__(self, token):
        self.token = token
        self.offset = None
        self.api_url = 'https://api.telegram.org/bot{}/'.format(token)

    def _make_request(self, method_name, method = 'get', params = None):
        if method == 'post':
            resp = requests.post(self.api_url + method_name, params)
        else:
            resp = requests.get(self.api_url + method_name, params)
        return resp

    def get_updates(self, offset=None, timeout=30):
        resp = self._make_request('getUpdates', 'get' , {'timeout': timeout, 'offset': offset})
        return resp.json()['result']

    @logit.logit
    def get_last_update_id(self, update):
        return max( [int(item['update_id']) for item in update] )

    def get_last_chat_id_and_text(self, updates):
        last_update_n = len(updates) - 1
        return (updates[last_update_n]['message']['chat']['id'], updates[last_update_n]['message']['text'])

    @logit.logit
    def send_message(self, text, chat_id, reply_markup = None):
        return self._make_request('sendMessage', 'post', {'chat_id': chat_id, 'text': text, "reply_markup": reply_markup})

    def build_keyboard(self, items):
        keyboard = [[item] for item in items]
        reply_markup = {"keyboard":keyboard, "one_time_keyboard": True}
        return json.dumps(reply_markup)

    """
    def handle_updates(self, updates):
        for update in updates:
            if update["message"]["chat"]["type"] != "private":
                continue

            chat, message_text = update["message"]["chat"]["id"], update["message"]["text"]
            if message_text == "/start":
                self.send_message(chat, "Welcome to my bot", )
    """

            





