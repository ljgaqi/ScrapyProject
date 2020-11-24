
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request

class MyImagePiplines(ImagesPipeline):

    def process_item(self, item, spider):
        return item

    def get_media_requests(self, item, info):
        for image_url in item['Jav_image_big']:
            yield Request(image_url)

    def item_completed(self, results, item, info):
        return item