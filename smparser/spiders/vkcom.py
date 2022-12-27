import scrapy
import vk_api
from smparser.items import SmparserItem

class VkcomSpider(scrapy.Spider):
    name = 'vkcom'
    allowed_domains = ['vk.com']
    start_urls = ['http://vk.com/']
    

    def __init__(self, login, password, group_link):
        self.login = login
        self.password = password
        self.group_link = group_link
    def parse(self, response):
        API_VERSION = 5.131
        vk_session = vk_api.VkApi(self.login, self.password)
        vk_session.auth()

        vk = vk_session.get_api()
        posts = vk.wall.get(domain=self.group_link, v=API_VERSION)
      
        for i in range(len(posts['items'])):
            post_id = posts['items'][i]['id']
            owner_id = posts['items'][i]['owner_id']
            text = posts['items'][i]['text']
            from_id = posts['items'][i]['from_id']
            yield SmparserItem(_id = post_id, owner_id = owner_id, text = text,)
            comments = vk.wall.getComments(owner_id=owner_id, post_id=post_id)
            for j in range(len(comments['items'])):
                comment_id = comments['items'][j]['id']
                owner_id = comments['items'][j]['owner_id']
                text = comments['items'][j]['text']
                from_id = comments['items'][j]['from_id']
                yield SmparserItem(_id=comment_id,  owner_id = owner_id, text = text)
        pass
