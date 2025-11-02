import scrapy
class ExampleSpider(scrapy.Spider):
    name = "example"
    start_urls = ["https://example.org"]
    async def parse(self, response):
        yield {"title": response.css("title::text").get(), "url": response.url}
