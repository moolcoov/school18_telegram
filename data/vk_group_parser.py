import vk
from data import constants as const


class VkGroupParser:
    def __init__(self):
        self.vk_api = vk.API("d7e332aed7e332aed7e332aebbd4f150acdd7e3d7e332aeb430954dc2e2b174ca537e09")
        self.last_post_id = open("./data/last_post.txt").read()

    def get_last_post(self):
        post = self.vk_api.wall.get(owner_id=const.GROUP_ID, count=2, v=const.V)['items'][0]
        post_id = post['id']

        if int(post_id) != int(self.last_post_id):
            self.last_post_id = post_id
            with open("./data/last_post.txt", "w") as f:
                f.write(str(self.last_post_id))

            return post

        return False

    def update(self):
        return self.get_last_post()
