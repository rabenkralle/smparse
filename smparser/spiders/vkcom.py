import scrapy
import vk_api

class VkcomSpider(scrapy.Spider):
    name = 'vkcom'
    allowed_domains = ['vk.com']
    start_urls = ['http://vk.com/']

    def parse(self, response):
        pass
