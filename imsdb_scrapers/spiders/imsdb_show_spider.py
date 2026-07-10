# example:
# ```
#     scrapy crawl imsdb_show -a target_url="https://imsdb.com/TV/Futurama.html" -o futurama.jsonl
# ```
import scrapy

class IMSDBShowSpider(scrapy.Spider):
    name = "imsdb_show"

    async def start(self):
        yield scrapy.Request(self.target_url, callback=self.parse_showpage)
    
    def parse_showpage(self, response):
        for href in response.css("p a::attr(href)").getall():
            yield response.follow(href, callback=self.parse_episodepage)
    
    def parse_episodepage(self, response):
        href = response.css("p a::attr(href)").get()
        yield response.follow(href, callback=self.parse_scriptpage)
    
    def parse_scriptpage(self, response):
        script_text = response.css("pre").get()
        yield {"text": script_text}
