import telebot
from data import constants as const


class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(const.BOT_TOKEN)

    def send_post(self, post):
        attachments = []

        text = post['text']
        media = post['attachments']

        for index, attachment in enumerate(media):
            if attachment['type'] == 'photo':
                photos = attachment['photo']
                sizes = dict()

                for photo_size in photos['sizes']:
                    sizes[int(photo_size['height'])] = photo_size['url']

                photo = telebot.types.InputMediaPhoto(sizes[max(sizes)])

                if index == 0:
                    photo.caption = text
                attachments.append(photo)

        if attachments:
            self.bot.send_media_group(const.CHANNEL_ID, attachments)
        else:
            self.bot.send_message(const.CHANNEL_ID, text)
