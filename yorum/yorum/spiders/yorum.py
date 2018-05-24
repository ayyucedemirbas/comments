import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class deneme(CrawlSpider):
    name = 'yorum'
    allowed_domains = ['hepsiburada.com']
    start_urls = ['https://www.hepsiburada.com/']
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    
   
    def parse_item(self, response):
       
        
        '''filename = 'yorumlar.txt'   '''
        
        print(response.xpath('//p[@class="review-text"]/text()').extract())
        '''text_file = open(filename, "w")
        text_file.write('+'.join([str(x) for x in pos]))
        text_file.close()'''
