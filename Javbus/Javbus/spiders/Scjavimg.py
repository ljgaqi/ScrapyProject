import sys
sys.path.append('..')
import scrapy
from Javbus.javitems import javItem
from scrapy.linkextractors import LinkExtractor

class JavimageSpider(scrapy.Spider):
    name = 'Sji'
    start_urls = ['https://www.fanbus.in/']
    #item=JavbusItem()

    def parse(self, response):
        le=LinkExtractor(restrict_xpaths='//*[@id="waterfall"]')
        links=le.extract_links(response)
        for link in links:
            yield scrapy.Request(url=link.url,callback=self.parsedown)

        # next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)

    def parsedown(self,response):
        item=javItem()
        # item['Jav_url']=response.url
        # item['Jav_image_big']=response.xpath('//*[@class="bigImage"]/@href').extract_first()
        item['image_urls']=response.xpath('//*[@class="bigImage"]/@href').extract_first()
        item['Jav_sn']=response.xpath('//*[@class="row movie"]/div/p/span/text()').extract()[1]
        item['Jav_time']=response.xpath('//*[@class="col-md-3 info"]/p/text()').extract()[3]
        # item['Jav_date']=response.xpath('//*[@class="col-md-3 info"]/p/text()').extract()[2]
        # item['Jav_title']=response.xpath('//*[@class="row movie"]/div/a/img/@title').extract_first()
        yield item
