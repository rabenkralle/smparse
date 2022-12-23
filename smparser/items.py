# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SmparserItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    _id = scrapy.Field()
    owner_id = scrapy.Field()
    text = scrapy.Field()
    photo = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    post_type = scrapy.Field()
    pass
