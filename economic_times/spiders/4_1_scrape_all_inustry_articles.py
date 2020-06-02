#goto each link of a page, then open it, then scrape inside data

#all 6 subtopics of topic auto sector are scraped here
import scrapy

from ..items import EconomicTimesItem

class amazon_spider(scrapy.Spider):
    name = 'et_all_industry_article'
    start_urls = ['https://economictimes.indiatimes.com/industry/auto/auto-news/articlelist/64829342.cms',
    'https://economictimes.indiatimes.com/industry/auto/cars-uvs/articlelist/64829336.cms',
    'https://economictimes.indiatimes.com/industry/auto/two-wheelers-three-wheelers/articlelist/64829323.cms',
    'https://economictimes.indiatimes.com/industry/auto/lcv-hcv/articlelist/64829321.cms',
    'https://economictimes.indiatimes.com/industry/auto/auto-components/articlelist/64829316.cms',
    'https://economictimes.indiatimes.com/industry/auto/tyres/articlelist/64829311.cms']
    
    
    def parse(self,response): #parse method is like a main function
        #first store all links of page in a list, then traverse them one by one
        links = response.css('.tabdata , .eachStory h3 a::attr(href)')[1:]
        for href in links:
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback = self.parse_dir_contents)

    
    #now we visit each linkand extract scrape data of link page
    def parse_dir_contents(self, response):
        items = EconomicTimesItem()
        
        heading = response.css('h1.clearfix::text').extract() 
        sub_heading = response.css('.title2::text').extract()
        time = response.css('.publish_on::text').extract()
        publisher = response.css('.publisher::text').extract()
        article = response.css('.Normal::text , .Normal a::text').extract()
        tags = response.css('span.readanchore  div.rdMrBulDiv a::text').extract() 

        
        items['heading'] = heading,
        items['sub_heading'] = sub_heading,
        items['time'] = time,
        items['publisher'] = publisher,
        items['article'] = article,
        items['tags'] = tags
        
        yield items
