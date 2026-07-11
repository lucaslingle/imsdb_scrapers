# example:
# ```
#     scrapy crawl imsdb_genre_listing -a target_url="https://imsdb.com/genre/Comedy" -o comedy_movies_listing.jsonl
# ```
import scrapy

class IMSDBGenreListingSpider(scrapy.Spider):
    name = "imsdb_genre_listing"

    async def start(self):
        yield scrapy.Request(self.target_url, callback=self.parse_genrepage)
    
    def parse_genrepage(self, response):
        for href in response.css("p a::attr(href)").getall():
            yield {
                "movie_url": response.urljoin(href)
            }
