from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from smparser import settings
from smparser.spiders.vkcom import VkcomSpider


if __name__ == '__main__':
	crawler_settings = Settings()
	crawler_settings.setmodule(settings)
	
	process = CrawlerProcess(settings = crawler_settings)
	process.crawl(VkcomSpider, text = '')
	process.start()