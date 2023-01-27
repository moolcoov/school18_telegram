import telebot
from data import constants as const


class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(const.BOT_TOKEN)

    def send_post(self, post):
        attachments = []

        text = post['items'][0]['text']
        media = post['items'][0]['attachments']

        for i, el in enumerate(media):
            if el['type'] == 'photo':
                print(el['image'][-1]['url'])
                photo = telebot.types.InputMediaPhoto(el['image'][-1]['url'])
                if i == 0:
                    photo.caption = text
                attachments.append(photo)

        if attachments:
            self.bot.send_media_group(const.CHANNEL_ID, attachments)
        else:
            self.bot.send_message(const.CHANNEL_ID, text)
