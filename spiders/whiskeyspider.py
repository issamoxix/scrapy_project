import scrapy

class WhiskeySpider(scrapy.Spider):
    name = 'whsikey'
    start_urls= ["https://www.whiskyshop.com/scotch-whisky?p=1"]

    def _parse(self,response):
        for products in response.css('div.product-item-info'):
            yield {
                'name':products.css('a.product-item-link::text').get(),
                'price':products.css('span.price::text').get(),
                'link':products.css('a.product-item-link').attrib['href']
            }
        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,callback=self._parse)