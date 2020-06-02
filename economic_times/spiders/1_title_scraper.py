#to start project, use : scrapy startproject amazon_scrapper

#in just 1 upper folder of this file, type : $ scrapy crawl quotes
#it will display yield fed results

# goto inspect and click on mouse button to layout select mode

# use 'view page source' and then ctrl + f to find req stuff

# use $ scrapy shell "http://quotes.toscrape.com/" to open website inside a shell
    
    #css selectors .....................................................

    # $ response.css('title')

    # $ response.css('title').extract()

    # $ response.css('title::text').extract()
    # ::text to added to extract only text

    # $ response.css('title::text')[0].extract()

    # $ response.css('title::text').extract_first()  # this is same as above (does not return error if list gets empty)

    # <span class="text" itemprop="text">“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”</span>
    # $ response.css('span.text').extract()
    # here span is tag name, text is class name
    # . is used bt classname (eg -> .text)

    # $ response.css('span.text::text').extract()

    #if we had id instead of a class then we used # instead of .

    # $ response.css('span.text::text')[0].extract()

    # use chrome extention, we found -> .author
    # $ response.css('.author::text').extract()

    # $ response.css('.author::text')[2].extract()

    #x path selector .................................................
    #x path is better, coz it makes selection of next button href easy, and more

    # if you use double quotes outside, make sure to use single quotes inside, vice versa

    # to select title tag
    # $ response.xpath("//title").extract()

    #to select text of title tag
    # $ response.xpath("//title/text()").extract()

    # # to extract data of 'span' tag with class name 'text'
    # $ response.xpath("//span[@class='text']").extract()

    #to only extract text part of above code
    # $ response.xpath("//span[@class='text']/text()").extract()

    #to only select first one of the list
    # $ response.xpath("//span[@class='text']/text()")[0].extract()

    #to select id instead of class , use @id instead of @class

    #combining both x path and css selectors ......................................

    #<a href="/page/2/">Next <span aria-hidden="true">→</span></a>
    # this is the outer html of next button
    #just one line above, given : <li class="next">
        #<a href="/page/2/" class="selectorgadget_selected">Next <span aria-hidden="true">→</span></a></li>
    # $ response.css("li.next a").extract()
    #it means select 'li' tag with class 'text' that contains 'a' tag within it
    #always make a habit of searching outside to inside

    #to only select 'href' from above code (this is a combination of css and xpath selectors)
    # $ response.css("li.next a").xpath("@href").extract()
    # note : only a tag contains href

    #to find all the href tags of the source code
    # response.css(".a").xpath("@href").extract()
import scrapy

#class of spider
class amazon_spider(scrapy.Spider):
    #name of spider
    name = 'et_article_title'

    #add list of urls you want to scrape here
    start_urls = ['https://economictimes.indiatimes.com/industry/auto/auto-news/mahindra-mahindra-unveils-online-car-owning-platform/articleshow/75617731.cms']

    #name and start_url are variables defined in class




    #response contains source code of website we want to scrape
    #self is used for an object to refer itself

    def parse(self, response):
        #storing title in title variable using 'title' tag.

        #1) complete titile with source
        title = response.css('title').extract()

        #2) only text of tag
        title_text = response.css('title::text').extract()

        #3)

        #dictionary (database representation)
        yield {'title_text':title_text} #yeild is similar to return
