# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Tshirt(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    item_url = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    
