import telebot
from data import constants as const


class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(const.BOT_TOKEN)

    def send_post(self, post):
        attachments = []

        text = post['text']
        media = post['attachments']

        for i, el in enumerate(media):
            if el['type'] == 'photo':
                photo = telebot.types.InputMediaPhoto(el['photo']['sizes'][-1]['url'])
                if i == 0:
                    photo.caption = text
                attachments.append(photo)

        if attachments:
            self.bot.send_media_group(const.CHANNEL_ID, attachments)
        else:
            self.bot.send_message(const.CHANNEL_ID, text)
