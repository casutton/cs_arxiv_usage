__author__ = 'Kay'
import sys
sys.path.append("/Users/Kay/Project/Scraper/conference")

import scrapy
from conference.items import ConferenceItem


class PLDISpider(scrapy.Spider):

    name = "pldi"
    allowed_domains = ["www.pldi.org"]
    start_urls = [
        "file:///Users/Kay/Project/webpage/pldi06.html"
    ]

    def parse(self, response):
        i = 1
        for x in response.xpath('//table[@class=\'text12\']//tr'):

            record = response.xpath('//table[@class=\'text12\']//tr[position()=%d]'%i)
            if record.xpath('td[2]/span/a[not(@title)]'):
                data = record.xpath('td[2]/span/a[not(@title)]/text()').extract()
                item = ConferenceItem()
                item['year'] = '2006'
                item['title'] = data[0]
                print data
                authors = record.xpath('following-sibling::tr[1]//a/text()').extract()
                print authors
                item['authors'] = authors
                yield item
                i += 2
            else:
                i += 1
