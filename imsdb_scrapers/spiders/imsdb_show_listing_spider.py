# example:
# ```
#     scrapy crawl imsdb_show_listing -o show_listings.jsonl
# ```
import scrapy

class IMSDBShowListingSpider(scrapy.Spider):
    name = "imsdb_show_listing"

    async def start(self):
        target_urls = [
            "https://imsdb.com/TV/Futurama.html",
            "https://imsdb.com/TV/Seinfeld.html",
            "https://imsdb.com/TV/South%20Park.html",
            "https://imsdb.com/TV/Stargate%20SG1.html",
            "https://imsdb.com/TV/Lost.html",
            "https://imsdb.com/TV/The%204400.html",
        ]
        for url in target_urls:
            yield scrapy.Request(url, callback=self.parse_showpage)

    def parse_showpage(self, response):
        for href in response.css("p a::attr(href)").getall():
            yield response.follow(href, callback=self.parse_episodepage)
    
    def parse_episodepage(self, response):
        href = response.css("p a::attr(href)").get()
        yield {
            "script_url": response.urljoin(href)
        }
