# import the necessary packages
from timecoverspider.items import MagazineCover
import datetime
import scrapy
from PIL import Image

class CoverSpider(scrapy.Spider):
    name = "pyimagesearch-cover-spider"
    start_urls = ["http://www.zumiez.com/mens/t-shirts.html"]

    def parse(self,response):
        list1 = response.css("div.category-products")

        #for img in list1:
        list2 = list1.css('img ::attr(src)').extract_first()

        self.log("TESTTTTTTTTTTTT    LIS" + list2)

        yield MagazineCover(file_urls=list2)
