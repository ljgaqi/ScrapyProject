import sys
sys.path.append('..')
import scrapy
from Javimage.items import JavimageItem
from scrapy.linkextractors import LinkExtractor


class ImageloadSpider(scrapy.Spider):
    name = 'imageload'
    #allowed_domains = ['https://www.fanbus.in/']
    start_urls = ['https://www.fanbus.in/']

    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//*[@id="waterfall"]')
        links = le.extract_links(response)
        for link in links:
            yield scrapy.Request(url=link.url, callback=self.parsedown)

        next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

    def parsedown(self,response):
        item=JavimageItem()
        item['url']=response.url
        #image_urls 必须是一个list，所以赋值时要加[]
        item['image_urls']=[response.xpath('//*[@class="bigImage"]/@href').extract_first()]
        item['sn']=response.xpath('//*[@class="row movie"]/div/p/span/text()').extract()[1]
        item['time']=response.xpath('//*[@class="col-md-3 info"]/p/text()').extract()[3]
        yield item