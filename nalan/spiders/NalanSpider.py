# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 15:07:31 2017

@author: Evan
"""
import scrapy
from nalan.items import NalanItem
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re
from random import choice
from scrapy.conf import settings
    
class NalanSpider(scrapy.Spider):
    name = "nalan"
    count = 1
    allowed_domains = ["sogou.com","mp.weixin.qq.com"]
    settings.overrides['DOWNLOAD_TIMEOUT'] = 5
    settings.overrides['CONCURRENT_REQUESTS'] = 1
    start_urls = [
'http://mp.weixin.qq.com/s?src=3&timestamp=1501427299&ver=1&signature=gTucpmC3hASxHDpyL1BbgwFJrTxekR5kVAxoZtTMOUYzOMKXyIcwzdyJx3XnQK2HW8jHG0zvVpyqpwLO03*QRaANS*9ZI*4wh0DA-tno8ir9txCiI-ov0toQF8cfBPoSSiL-aLQGJwm1mzZfbRKezA=='
    ]
#    start_urls = [url.strip() for url in f.readlines()]
    tmpnum = 10000

            
    def parse(self,response):
        print("爬单独页面开始")
        print("第"+str(self.count)+"个爬虫开始")
        self.count = self.count + 1
       
        title = response.xpath('string(//*[@id="activity-name"])').extract_first().replace('\n','').replace('\r','').strip()
        postdate = response.xpath('string(//*[@id="post-date"])').extract_first().strip()
        print(title) 
        
        if(title.find("男生场")!=-1):             
            gender = "male"
        else:
            gender = "female"
        i = len(response.xpath('//img/@data-src').extract())
        print("len(response.xpath('//img/@data-src'):  ",i)
        i = i - 2
        print("iiiii:  ",i)
        if(gender == "female"):
            i = i - 15
        else:
            i = i - 10
        print("iiiii2:  ",i)
        i=0
#        for sel in response.xpath('//*[@id="js_content"]/section/section[section/section[not(contains(.,"dicksoup"))]]'):
        for sel in response.xpath('//*[@id="js_content"]'):
            item = NalanItem()            
            item['volume'] = title
            item['postdate'] = postdate
            item['gender'] = gender
            dec = sel.xpath('string(.)').extract_first()
            print('dec===',dec)
            pos = dec.find('—微')
            if(pos!=-1):
                item['idnum'] = dec[0:pos]
            else:
                self.tmpnum = self.tmpnum-1
                item['idnum'] = str(self.tmpnum)
            print('idnum', item['idnum'])
            
            pos1 = dec.find('城市')
            if(pos1!=-1):
                if(dec[pos1+2]==":" or dec[pos1+2]=="："):
                    tmp = dec[pos1+3:]
                    logging.info('1111111---'+tmp)
                    pos2 = tmp.find('职业')
                    if(pos2==-1):
                        pos2 = tmp.find(' ')
                        if(pos2==-1):
                            pos2 = tmp.find(' ')
                    item['city'] = tmp[0:pos2]
                else:
                    tmp = dec[pos1+2:].lstrip()
                    logging.info('2222222---'+tmp)
                    pos2 = tmp.find('职业')
                    if(pos2==-1):
                        pos2 = tmp.find(' ')
                        if(pos2==-1):
                            pos2 = tmp.find(' ')
                    item['city'] = tmp[0:pos2]
            elif(dec.find('坐标')!=-1):
                pos1 = dec.find('坐标')
                if(dec[pos1+2]==":" or dec[pos1+2]=="："):
                    tmp = dec[pos1+2:]
                    logging.info('33333333---'+tmp)
                    pos2 = tmp.find('职业')
                    if(pos2==-1):
                        pos2 = tmp.find(' ')
                        if(pos2==-1):
                            pos2 = tmp.find(' ')
                    item['city'] = tmp[0:pos2]
                else:
                    tmp = dec[pos1+2:].lstrip()
                    logging.info('44444444---'+tmp)
                    pos2 = tmp.find('职业')
                    if(pos2==-1):
                        pos2 = tmp.find(' ')
                        if(pos2==-1):
                            pos2 = tmp.find(' ')
                    item['city'] = tmp[0:pos2]
            
            
                
                
            item['dec'] = dec   
#            item['image_urls'] = [response.xpath('//*[@id="js_content"]//section[@style=" text-align: center;  box-sizing: border-box; "]/img/@data-src').extract()[i]]         
            item['image_urls'] = [response.xpath('//img/@data-src').extract()[i]]
            if(str(item['image_urls']).find("wx_fmt=gif")!=-1):
                i = i+1
                item['image_urls'] = [response.xpath('//img/@data-src').extract()[i]]
            print("i=  ",i)
            print("imageurl:",item['image_urls'])    
            print("==================================================")
            print("==================================================")
#            item['idnum'] = sel.xpath('string(.//p[not(contains(.,"请把这个号"))][1])').extract_first()            
#            item['gender'] = gender
#            item['wechat'] = sel.xpath('string(.//p[not(contains(.,"请把这个号"))][2])').extract_first()
#            item['age'] = sel.xpath('string(.//p[not(contains(.,"请把这个号"))][3])').extract_first()
#            item['heigh'] = sel.xpath('string(.//p[not(contains(.,"请把这个号"))][4])').extract_first()
#            item['city'] = sel.xpath('string(.//p[not(contains(.,"请把这个号"))][5])').extract_first()
                              
            i=i+1           
            
#            if(item['wechat'] ==''):                
#                item['idnum'] = sel.xpath('string(.//section/section[contains(@style,"font-size:")]/section[1])').extract_first()            
#                item['wechat'] = sel.xpath('string(.//section/section[contains(@style,"font-size:")]/section[2])').extract_first()
#                item['age'] = sel.xpath('string(.//section/section[contains(@style,"font-size:")]/section[3])').extract_first()
#                item['heigh'] = sel.xpath('string(.//section/section[contains(@style,"font-size:")]/section[4])').extract_first()
#                item['city'] = sel.xpath('string(.//section/section[contains(@style,"font-size:")]/section[5])').extract_first()
#                item['dec'] = sel.xpath('string(.)').extract_first()
#                logging.info(item)
            yield item
         