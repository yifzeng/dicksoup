# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json 
import codecs 
import os
import re
import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline
import logging
class NalanPipeline(object):
    def process_item(self, item, spider): 
        if(item['idnum'].startswith('鉴于时至今日')):
            raise DropItem("Invalid item found : %s" % item)
        item['dec'] = item['dec'].replace('请把这个号推荐给你比较好看的朋友', '').lstrip()       
        non_decimal = re.compile(r'[^\d]+')
        item['idnum'] = non_decimal.sub('',item['idnum'])
        if(item['idnum']==''):
            pos = item['dec'].find('微信')
            if(pos!=-1):
                item['idnum'] = item['dec'][0:pos]
            else:
                pos = item['dec'].find('信号')
                if(pos!=-1):
                    item['idnum'] = item['dec'][0:pos]
        logging.info(item['idnum'])
        non_decimal = re.compile(r'[^\d]+')
        item['idnum'] = non_decimal.sub('',item['idnum'])
        if(item['city'].replace(' ', '').replace('\n','').replace('：','').replace(':','')!=''):
            item['city'] = item['city'].replace(' ', '').replace('\n','').replace('：','').replace(':','')
            return item
        else:
            raise DropItem("----------------------Invalid--------------- item found : %s" % item)
            
class JsonWriterPipeline(object):

    def __init__(self):
        self.file_female = codecs.open('scraped_femaledata_utf8.json', 'w', encoding='utf-8')
        self.file_female.write('[')
        self.file_male = codecs.open('scraped_maledata_utf8.json', 'w', encoding='utf-8')
        self.file_male.write('[')

    def process_item(self, item, spider):
        if(item['gender']=="female"):
            line = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file_female.write(line+',')
        else:
            line = json.dumps(dict(item),ensure_ascii=False) + "\n"
            self.file_male.write(line+',')
        return item
    
    def close_spider(self, spider):
        self.file_female.seek(-1, os.SEEK_END)
        self.file_female.truncate();
        self.file_female.write(']')
        self.file_female.close()
        self.file_male.seek(-1, os.SEEK_END)
        self.file_male.truncate();
        self.file_male.write(']')
        self.file_male.close()
        
class DuplicatesPipeline(object):

    def __init__(self):
        self.wechat_seen = set()
        self.idnum_seen = set()

    def process_item(self, item, spider):
        if item['idnum'] in self.wechat_seen:
#            if item['idnum'] in self.idnum_seen:
                raise DropItem("++++++++++++++++++++Duplicate item found: %s" % item)
        else:
#            self.wechat_seen.add(item['wechat'])
            self.idnum_seen.add(item['idnum'])
            return item

class personImagePipeline(ImagesPipeline):
    
     def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url,meta={'item': item})
     
     def item_completed(self, results, item, info):
                        
        return item
    
     def file_path(self, request, response=None, info=None):
        item = request.meta['item']         
        filename = item['idnum']+'.jpeg'
        return filename
            
            
            
            