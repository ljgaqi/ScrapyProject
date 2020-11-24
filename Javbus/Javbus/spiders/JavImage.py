import sys
sys.path.append('..')
import scrapy
from Javbus.items import JavbusItem
from scrapy.linkextractors import LinkExtractor

class JavimageSpider(scrapy.Spider):
    name = 'JavImage'
    start_urls = ['https://www.fanbus.in/']
    #item=JavbusItem()

    def parse(self, response):
        le=LinkExtractor(restrict_xpaths='//*[@id="waterfall"]')
        links=le.extract_links(response)
        for link in links:
            yield scrapy.Request(url=link.url,callback=self.parsedown)
        next_url = response.xpath('//*[@id="next"]/@href').extract_first()


        if next_url:
            next_url = response.urljoin(next_url)
            yield scrapy.Request(next_url, callback=self.parse)

    def parsedown(self,response):
        item=JavbusItem()
        item['Jav_url']=response.url
        item['Jav_image_big']=response.xpath('//*[@class="bigImage"]/@href').extract_first()
        #item['image_urls']=response.xpath('//*[@class="bigImage"]/@href').extract_first()
        item['Jav_sn']=response.xpath('//*[@class="row movie"]/div/p/span/text()').extract()[1]
        item['Jav_time']=response.xpath('//*[@class="col-md-3 info"]/p/text()').extract()[3]
        item['Jav_date']=response.xpath('//*[@class="col-md-3 info"]/p/text()').extract()[2]
        item['Jav_title']=response.xpath('//*[@class="row movie"]/div/a/img/@title').extract_first()
        yield item




        # for avweb in response.xpath('//*[@id="waterfall"]/div'):
        #     item = JavbusItem
        #     av_url = avweb.xpath('./a/@href').extract_first()
        #     av_img = avweb.xpath('./a/div/img/@src').extract_first()
        #     av_title = avweb.xpath('./a/div/img/@title').extract_first()
        #     av_sn = avweb.xpath('./a/div[2]/span/date[1]/text()').extract_first()
        #     av_date = avweb.xpath('./a/div[2]/span/date[2]/text()').extract_first()
        #     if av_url != None:  # 判断爬下来的内容不为空，再继续...
        #         item['Jav_url'] = av_url
        #         item['Jav_date'] = av_date
        #         item['Jav_image_small'] = av_img
        #         item['Jav_sn'] = av_sn
        #         item['Jav_title'] = av_title
        #
        #         print('this is tyr')
        #         print(av_url)
        #         print(item['Jav_url'])
        #         print({'item': item})
        #
        #         yield scrapy.Request(url=item['Jav_url'], meta={'item': item}, callback=self.parse_deep)
                # meta参数是为了传参存在的，为了是把item传递给下一个函数。
        # next_url = response.xpath('//*[@id="next"]/@href').extract_first()
        # if next_url:
        #     next_url = response.urljoin(next_url)
        #     yield scrapy.Request(next_url, callback=self.parse)

    # def parse_deep(self, response):
    #     item = response.meta['item']  # 我被这个中括号折磨致死，以后一定要记住[]是字典，{}不是
    #     item['Jav_image_big'] = response.xpath('//*[@class="bigImage"]/img/@src').extract_first()
    #     yield item

        # yield {
        #     'av_sn': av_sn,
        #     'av_date': av_date,
        #     'av_url':av_url,
        #     'av_img':av_img,
        #     'av_title':av_title
        # }
