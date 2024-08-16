# Explain concept below
import scrapy

class ProxyScraperSpider(scrapy.Spider):
    # identidade
    name = 'proxyscraper'

    # Request
    def start_requests(self):
        urls = ['https://www.us-proxy.org/']

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse,meta={'next_url':urls[0]})

    # Response
    def parse(self, response):

        for quote in response.xpath("//table[@class='table table-striped table-bordered']//tr"):
            yield {
                'ip_address': quote.xpath("./td[1]/text()").get(),
                'port': quote.xpath("./td[2]/text()").get(),
                'code': quote.xpath("./td[3]/text()").get(),
                'country': quote.xpath("./td[4]/text()").get(),
                'anonimity': quote.xpath("./td[5]/text()").get(),
                'google': quote.xpath("./td[6]/text()").get(),
                'https': quote.xpath("./td[7]/text()").get(),
                'last_checked': quote.xpath("./td[8]/text()").get()
            }