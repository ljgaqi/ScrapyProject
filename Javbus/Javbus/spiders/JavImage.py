import scrapy


class JavimageSpider(scrapy.Spider):
    name = 'JavImage'
    allowed_domains = ['https://www.fanbus.in/']
    start_urls = ['https://www.fanbus.in/']

    def parse(self, response):
        pass
