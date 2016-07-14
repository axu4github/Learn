import scrapy
from scrapy.spiders import Spider
from scrapy.loader import ItemLoader
from learn_scrapy.items import LearnScrapyItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class LearnScrapySpider(Spider):
    """docstring for LearnScrapySpider"""

    name = "ls"
    allowed_domains = ["amazon.cn"]
    items = []
    handle_httpstatus_list = [301, 302]
    start_urls = [
        # "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=1",
        # "http://search.jd.com/Search?keyword=apple&enc=utf-8&stock=1&wtype=1&psort=3&page=3",
        "https://www.amazon.cn/s/rh=i%3Aaps%2Ck%3Aapple%2Cp_n_fulfilled_by_amazon%3A326314071&keywords=apple"
    ]

    page_number = 1
    MAX_PAGE_NUMBER = 3

    url = "https://www.amazon.cn/s/rh=i%3Aaps%2Ck%3Aapple%2Cp_n_fulfilled_by_amazon%3A326314071&keywords=beoplay&page={page}"

    def parse(self, response):
        print "RESPONSE_URL ==========> %s" % response.url
        # if response.url != "https://www.amazon.cn/s/rh=i%3Aaps%2Ck%3Aapple%2Cp_n_fulfilled_by_amazon%3A326314071&keywords=apple" :
        #     pass
        # else : 
        #     print "1"
        next_page = response.xpath("//span[@class='pagnRA']").extract()

        print next_page
        # for item in response.xpath("//div[contains(@id, 'J_goodsList')]//li"):
        #     ls = LearnScrapyItem()
        #     ls['name'] = item
        #     self.items.append(ls)

        if next_page and self.page_number < self.MAX_PAGE_NUMBER:
            self.page_number += 1
            next_page = self.url.format(page=self.page_number)

            return scrapy.Request(next_page, callback=self.parse)

        # print len(self.items), self.items
        # return self.items
