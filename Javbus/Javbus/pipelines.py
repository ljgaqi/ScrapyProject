# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

from scrapy.exceptions import DropItem
import scrapy


class JavbusPipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        # image_paths = [x['path'] for ok, x in results if ok]
        # if not image_paths:
        #     raise DropItem("Item contains no images")
        # item['image_paths'] = image_paths
        return item

    # def get_media_requests(self, item, info):
    #     for image_urls in item['Jav_image_big']:
    #         yield Request(image_urls)
    #
    # def item_completed(self, results, item, info):
    #     return item
