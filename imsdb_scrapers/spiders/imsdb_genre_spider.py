# example:
# ```
#     scrapy crawl imsdb_genre -a target_url="https://imsdb.com/genre/Comedy" -o comedy_movies.jsonl
# ```
import scrapy

class IMSDBGenreSpider(scrapy.Spider):
    name = "imsdb_genre"

    async def start(self):
        yield scrapy.Request(self.target_url, callback=self.parse_genrepage)
    
    def parse_genrepage(self, response):
        for href in response.css("p a::attr(href)").getall():
            yield response.follow(href, callback=self.parse_moviepage)
    
    def parse_moviepage(self, response):
        href = response.css("p a::attr(href)").get()
        yield response.follow(href, callback=self.parse_scriptpage)
    
    def parse_scriptpage(self, response):
        yield {
            "script_url": response.url,
            "script_text": response.css("pre").get()
        }
