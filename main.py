from time import sleep
from data import vk_group_parser, tg_channel_updater


def main():
    vk = vk_group_parser.VkGroupParser()
    tg = tg_channel_updater.TelegramBot()

    while True:
        response = vk.update()
        if response:
            tg.send_post(response)
        sleep(60)


if __name__ == '__main__':
    main()
