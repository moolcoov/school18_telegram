import vk
from data import constants as const


class VkGroupParser:
    def __init__(self):
        self.vk_api = vk.API("d7e332aed7e332aed7e332aebbd4f150acdd7e3d7e332aeb430954dc2e2b174ca537e09")
        self.last_post_id = None

    def get_last_post(self):
        post = self.vk_api.wall.get(owner_id=const.GROUP_ID, count=1, v=const.V)
        post_id = post['items'][0]['id']

        if post_id != self.last_post_id:
            self.last_post_id = post_id
            return post

        return False

    def update(self):
        return self.get_last_post()
