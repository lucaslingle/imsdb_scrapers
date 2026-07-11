# example:
# ```
#     scrapy crawl imsdb_movie -a target_url="https://imsdb.com/Movie%20Scripts/500%20Days%20of%20Summer%20Script.html" -o 500dayssummer.jsonl
# ```
import scrapy

class IMSDBMovieSpider(scrapy.Spider):
    name = "imsdb_movie"

    async def start(self):
        yield scrapy.Request(self.target_url, callback=self.parse_moviepage)
    
    def parse_moviepage(self, response):
        href = response.css("p a::attr(href)").get()
        yield response.follow(href, callback=self.parse_scriptpage)
    
    def parse_scriptpage(self, response):
        script_text = response.css("pre").get()
        yield {"text": script_text}
