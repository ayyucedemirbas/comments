import scrapy
import pymongo
import sys
from pymongo import MongoClient
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
        connection = MongoClient("URI") 
    
        db = connection.yeni
        people = db.yeni
        
        text = response.xpath('//p[@class="review-text"]/text()').extract() 
        while text:
        
            content={"file_name": response.xpath('//p[@class="review-text"]/text()').extract(), "contents" : text }

            
            people.insert(content)
                   
        
        
  