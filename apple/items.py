# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AppleItem(scrapy.Item):
    location = scrapy.Field()
    price = scrapy.Field()

class Imac_proItem(scrapy.Item):
    location = scrapy.Field()
    price = scrapy.Field()