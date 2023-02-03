import vk

from data import constants as const


class VkGroupParser:
    def __init__(self):
        self.vk_api = vk.API(const.API_KEY)
        self.last_post_id = open("./data/last_post.txt").read()

    def get_last_post(self):
        try:
            post = self.vk_api.wall.get(owner_id=const.GROUP_ID, count=2, v=const.V)['items'][0]
            post_id = post['id']
        except Exception as e:
            print(e)
            self.vk_api = vk.API(const.API_KEY)
            self.get_last_post()

        if int(post_id) != int(self.last_post_id):
            self.last_post_id = post_id
            with open("./data/last_post.txt", "w") as f:
                f.write(str(self.last_post_id))

            if 'copy_history' in post:
                base_text = post['text'] + "\n\n"
                post = post['copy_history'][0]
                post['text'] = base_text + post['text']

            return post

        return False

    def update(self):
        return self.get_last_post()
