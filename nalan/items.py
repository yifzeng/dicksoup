# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NalanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    volume = scrapy.Field()
    postdate = scrapy.Field()
    gender = scrapy.Field()
    idnum = scrapy.Field()
#    wechat = scrapy.Field()
#    age = scrapy.Field()
#    heigh = scrapy.Field()
    city = scrapy.Field()
    dec = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
