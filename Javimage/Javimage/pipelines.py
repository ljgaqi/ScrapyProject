# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
from Javimage.settings import IMAGES_STORE
import os
import re

class JavimagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield Request(image_url)
    # def process_item(self, item, spider):
    #     return item
    # def get_media_requests(self, item, info):
    #     for image_url in item['image_urls']:
    #         filename=item['sn']
    #         print('aaaaaaaaaaaaaaaaaaaaaaaaaaa')
    #         print(filename)
    #         yield Request(image_url,meta={'filename':filename})

    # def file_path(self, request, response=None, info=None):
    #     name=Request.meta['filename']+'.jpg'
    #     print(name)
    #     filepath=IMAGES_STORE
    #     filename = os.path.join(filepath, name)
    #     print(filename)
    #     return filename

    def item_completed(self, results, item, info):
        image_paths=[x['path']for ok,x in results if ok]
        newname=item['sn']+'.jpg'
        print(image_paths)
        print(newname)
        filepath=IMAGES_STORE
        os.rename(filepath+'/'+image_paths[0],filepath+'/'+newname)
        return item


        # name=Request.meta['filename']
        # imagepath=os.path.join('/',name)
        # return imagepath

    # def file_path(self,request,response=None,info=None,*,item):#设置图片存储路径及名称
    #     name=request.meta['name']
    #     path=item['time']
    #     image_path=os.path.join(path,name)
    #     return image_path
    # def file_path(self, request, response=None, info=None, *, item):
    #     filepath=IMAGES_STORE
    #     image_name=item['sn']
    #     return "%s/%s"%(filepath,image_name)