import scrapy
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from learn_scrapy.items import LearnScrapyItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class LearnScrapySpider(Spider):
    """docstring for LearnScrapySpider"""

    name = "ls"
    allowed_domains = ["jd.com"]
    items = []
    start_urls = [
        "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=1",
        # "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=3",
    ]

    page_number = 1
    MAX_PAGE_NUMBER = 3

    url = "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=%d"

    def parse(self, response):
        next_page = response.xpath(
            "//a[contains(@class, 'fp-next')]/@onclick").extract()
        print next_page

        for item in response.xpath("//div[contains(@id, 'J_goodsList')]//li"):
            ls = LearnScrapyItem()
            ls['name'] = item
            self.items.append(ls)

        if next_page and self.page_number < self.MAX_PAGE_NUMBER:
            self.page_number += 1
            next_page = self.url % int(
                next_page[0].split('(').pop().split(')')[0])

            return scrapy.Request(next_page, callback=self.parse)

        print len(self.items), self.items
        return self.items
