import vk
import settings
import time


session = vk.Session(access_token=settings.user_access_token)

vk_api = vk.API(session, v=settings.vk_api_version)

while True:
    posts = vk_api.wall.get(owner_id=settings.owner_id,
                            count=100)
    if posts['count'] == 0:
        break

    post_ids = [post['id'] for post in posts['items']]
    for post_id in post_ids:
        vk_api.wall.delete(owner_id=settings.owner_id,
                           post_id=post_id)
        time.sleep(settings.requests_interval)
