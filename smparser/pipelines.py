# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import scrapy
from pymongo import MongoClient
from scrapy.pipelines.images import ImagesPipeline
import hashlib
import os
from scrapy.utils.python import to_bytes

class SmparserPipeline:

    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.vkdb

    def process_item(self, item, spider):
        collection = self.mongo_base[spider.name]
        collection.insert_one(item)
        return item
        
