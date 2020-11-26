import scrapy


class javItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Jav_sn = scrapy.Field()
    Jav_time=scrapy.Field()
    image_urls=scrapy.Field()