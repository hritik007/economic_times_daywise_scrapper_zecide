import scrapy
from ..items import EconomicTimesItem

class amazon_spider(scrapy.Spider):
    name = 'et_article_scraper'
    start_urls = ['https://economictimes.indiatimes.com/industry/auto/auto-news/mahindra-mahindra-unveils-online-car-owning-platform/articleshow/75617731.cms']

    def parse(self, response):
        items = EconomicTimesItem()
        
        heading = response.css('h1.clearfix::text').extract() 
        sub_heading = response.css('.title2::text').extract()
        time = response.css('.publish_on::text').extract()
        publisher = response.css('.publisher::text').extract()
        article = response.css('.Normal::text').extract()
        tags = response.css('span.readanchore  div.rdMrBulDiv a::text').extract() 

        
        items['heading'] = heading,
        items['sub_heading'] = sub_heading,
        items['time'] = time,
        items['publisher'] = publisher,
        items['article'] = article,
        items['tags'] = tags
        

        yield items