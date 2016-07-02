import scrapy
from scrapy.contrib.spiders import BaseSpider
import time
# from scrapy.http import Request


class LearnScrapySpider(BaseSpider):
    """docstring for LearnScrapySpider"""

    name = "ls"
    allowed_domains = ["jd.com"]
    start_urls = [
        "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=1",
        # "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=3",
    ]

    page_number = 1
    MAX_PAGE_NUMBER  = 3

    url = "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=%d"

    def parse(self, response):
        print self.page_number
        print "url : %s " % response.url
        next_page = response.xpath(
            "//a[contains(@class, 'fp-next')]/@onclick").extract()
        print next_page
        if next_page and self.page_number <= self.MAX_PAGE_NUMBER:
            self.page_number += 1
            next_page = self.url % int(
                next_page[0].split('(').pop().split(')')[0])
            print "==========>%s<===========" % next_page

            yield scrapy.Request(next_page, callback=self.parse)
