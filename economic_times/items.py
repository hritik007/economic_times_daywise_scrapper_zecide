# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EconomicTimesItem(scrapy.Item):
    heading = scrapy.Field()
    sub_heading = scrapy.Field()
    time = scrapy.Field()
    publisher = scrapy.Field()
    article = scrapy.Field()
    tags = scrapy.Field()
