#import necessary packages
from timecoverspider.items import Tshirt
import datetime
import scrapy


class TshirtSpider(scrapy.Spider):
	name = "webstore-tshirt-spider"
	start_urls = ["http://www.asos.com/men/t-shirts-vests/cat/?cid=7616"]

	def parse(self, response):
		productList = response.css("div.product-list")
		ulList = productList.css("li")
		for li in ulList:
			#imageURL = li.xpath('//img[@class="product-img"]/@src').extract()
			imageURL = li.css('img ::attr(src)').extract_first()
			itemURL = li.xpath("a/@href").extract_first()
			price = li.xpath("//span[@class='price']/text()").extract_first()
			title = li.xpath("//span[@class='name']/text()").extract_first()
			yield Tshirt(title=title, price=price, file_urls=[imageURL], item_url=itemURL)

		NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
		next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
		if next_page:
			yield scrapy.Request(
				response.urljoin(next_page),
				callback = self.parse
			)
		else:
			print("No more pages")
