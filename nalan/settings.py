# -*- coding: utf-8 -*-

# Scrapy settings for nalan project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
import random
BOT_NAME = 'nalan'

SPIDER_MODULES = ['nalan.spiders']
NEWSPIDER_MODULE = 'nalan.spiders'

ITEM_PIPELINES = {
    'nalan.pipelines.NalanPipeline': 300,
    'nalan.pipelines.DuplicatesPipeline': 500,
    'nalan.pipelines.JsonWriterPipeline': 800,
    'nalan.pipelines.personImagePipeline':1000    
}

LOG_FILE = 'scrapy.log'
LOG_LEVEL = 'INFO'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'nalan (+http://www.yourdomain.com)'
IMAGES_STORE='./pic'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1
RANDOMIZE_DOWNLOAD_DELAY = True

USER_AGENTS = [
                "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
                "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36",
                #"Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1",
                "Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1"
             ]



COOKIES_ENABLED = False

DOWNLOADER_MIDDLEWARES = {
    'nalan.middlewares.RandomUserAgent': 1,
}


#def getCookie():
#    cookie_list = [
#        'SUV=0048178A7144F73C58C548F37176C591; ABTEST=0|1489324292|v1; SNUID=4D86360071743BF924141B9C722D204B; IPLOC=CN4401; SUID=3CF74471771A910A0000000058C54904; wuid=AAHDo0R5FwAAAAqRIiVPwQsAZAM=; SUID=3CF744713220910A0000000058C54AE9; weixinIndexVisited=1; sct=3; SUIR=4D86360071743BF924141B9C722D204B; JSESSIONID=aaaRbKc6tXRCWc7_uwoQv; ld=Xetn4lllll2YeUrclllllV04Da7llllltUFT5lllll9lllllRklll5@@@@@@@@@@; wapsogou_qq_nickname=%E6%99%A8%E4%B8%B4%E9%9B%BE%E9%80%9D; w_userid=kb4IorcRo8oLkb1ekrsNlcoImbteorpblr8Qk7YIk79Y0vcG0OVA1qR7zOM=_-1717911180; wapsogou_qq_headimg=http%3A%2F%2Fq.qlogo.cn%2Fqqapp%2F100294784%2F080A19BD307F1554D085FA4C59820029%2F100; usid=fTCCUletTYtNDtFt; gpsloc=%E5%B9%BF%E4%B8%9C%E7%9C%81%09%E5%B9%BF%E5%B7%9E%E5%B8%82', #自己从不同浏览器中获取cookie在添加到这
#        'SUV=0048178A7144F73C58C548F37176C591; ABTEST=0|1489324292|v1; SNUID=4D86360071743BF924141B9C722D204B; IPLOC=CN4401; SUID=3CF74471771A910A0000000058C54904; SUID=3CF744713220910A0000000058C54AE9; weixinIndexVisited=1; sct=3; SUIR=4D86360071743BF924141B9C722D204B; JSESSIONID=aaaRbKc6tXRCWc7_uwoQv; ld=Xetn4lllll2YeUrclllllV04Da7llllltUFT5lllll9lllllRklll5@@@@@@@@@@; wapsogou_qq_nickname=%E6%99%A8%E4%B8%B4%E9%9B%BE%E9%80%9D; w_userid=kb4IorcRo8oLkb1ekrsNlcoImbteorpblr8Qk7YIk79Y0vcG0OVA1qR7zOM=_-1717911180; wapsogou_qq_headimg=http%3A%2F%2Fq.qlogo.cn%2Fqqapp%2F100294784%2F080A19BD307F1554D085FA4C59820029%2F100; gpsloc=%E5%B9%BF%E4%B8%9C%E7%9C%81%09%E5%B9%BF%E5%B7%9E%E5%B8%82; sgid=30-27037745-AVjHibibuQhYDX3Tvxs6AELa8; usid=fTCCUletTYtNDtFt; wuid=AAF2Ac6DFwAAAAqRGnm+2gcA1wA='
#        ]
#    cookie = random.choice(cookie_list)
#    return cookie
#
#
#
#DEFAULT_REQUEST_HEADERS = {   'Accept':'application/json',
#    'Accept-Encoding':'gzip, deflate, sdch',
#    'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2',
#    'Cache-Control':'max-age=0',
#    'Connection':'keep-alive',
#    'Host':'weixin.sogou.com',
#    'RA-Sid':'7739A016-20140918-030243-3adabf-48f828',
#    'RA-Ver':'3.0.7',
#    'Upgrade-Insecure-Requests':'1',
#    'Cookie':'%s' % getCookie()
#}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'nalan.middlewares.NalanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'nalan.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'nalan.pipelines.NalanPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
