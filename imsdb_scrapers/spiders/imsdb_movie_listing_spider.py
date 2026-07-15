# example:
# ```
#     scrapy crawl imsdb_movie_listing -o movie_listings.jsonl
# ```
import scrapy

class IMSDBMovieListingSpider(scrapy.Spider):
    name = "imsdb_movie_listing"

    async def start(self):
        target_urls = [
            "https://imsdb.com/genre/Action",
            "https://imsdb.com/genre/Adventure",
            "https://imsdb.com/genre/Animation",
            "https://imsdb.com/genre/Comedy",
            "https://imsdb.com/genre/Crime",
            "https://imsdb.com/genre/Drama",
            "https://imsdb.com/genre/Family",
            "https://imsdb.com/genre/Fantasy",
            "https://imsdb.com/genre/Film-Noir",
            "https://imsdb.com/genre/Horror",
            "https://imsdb.com/genre/Musical",
            "https://imsdb.com/genre/Mystery",
            "https://imsdb.com/genre/Romance",
            "https://imsdb.com/genre/Sci-Fi",
            "https://imsdb.com/genre/Short",
            "https://imsdb.com/genre/Thriller",
            "https://imsdb.com/genre/War",
            "https://imsdb.com/genre/Western",
        ]
        for url in target_urls:
            yield scrapy.Request(url, callback=self.parse_genrepage)

    def parse_genrepage(self, response):
        for href in response.css("p a::attr(href)").getall():
            yield response.follow(href, callback=self.parse_moviepage)

    def parse_moviepage(self, response):
        href = response.css("p a::attr(href)").get()
        yield {
            "script_url": response.urljoin(href)
        }
