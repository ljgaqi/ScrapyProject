# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JavbusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Jav_sn = scrapy.Field()
    Jav_date = scrapy.Field()
    Jav_url = scrapy.Field()
    #Jav_image_small = scrapy.Field()
    Jav_image_big = scrapy.Field()
    #images_urls=scrapy.Field()
    Jav_title = scrapy.Field()
    Jav_time=scrapy.Field()
