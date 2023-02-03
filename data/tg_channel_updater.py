import telebot
from data import constants as const


class TelegramBot:
    def __init__(self):
        self.bot = telebot.TeleBot(const.BOT_TOKEN, parse_mode="Markdown")

    def send_post(self, post):
        media = []
        polls = []

        text = post['text']
        attachments = post['media']

        for index, attachment in enumerate(attachments):
            if attachment['type'] == 'photo':
                photos = attachment['photo']
                sizes = dict()

                for photo_size in photos['sizes']:
                    sizes[int(photo_size['height'])] = photo_size['url']

                photo = telebot.types.InputMediaPhoto(sizes[max(sizes)])
                photo.url = sizes[max(sizes)]

                if index == 0:
                    photo.caption = text
                media.append(photo)

        if media:
            if len(media) == 1:
                text = f"[⁠]({media[0].url})" + text.strip()
                print(text)
                self.bot.send_message(const.CHANNEL_ID, text)
            else:
                self.bot.send_media_group(const.CHANNEL_ID, media)
        else:
            self.bot.send_message(const.CHANNEL_ID, text)
