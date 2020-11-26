# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from Javimage.Javimage.settings import IMAGES_STORE

class JavimagePipeline(ImagesPipeline):
    def process_item(self, item, spider):
        return item
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)
    # def file_path(self, request, response=None, info=None, *, item):
    #     filepath=IMAGES_STORE
    #     image_name=item['sn']
    #     return "%s/%s"%(filepath,image_name)