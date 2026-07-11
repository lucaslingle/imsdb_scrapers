# imsdb_scrapers
Spiders and scrapers for the Internet Movie Script Database (IMSDB)

## getting started

Install scrapy, e.g.:
```
conda create --name imsdb_scraping python=3.11  
conda activate imsdb_scraping
conda install scrapy
```

To download all scripts for one tv show:
```
scrapy crawl imsdb_show -a target_url="https://imsdb.com/TV/Futurama.html" -o futurama.jsonl
```

To download the script for one movie:
```
scrapy crawl imsdb_movie -a target_url="https://imsdb.com/Movie%20Scripts/500%20Days%20of%20Summer%20Script.html" -o 500dayssummer.jsonl
```

To download the scripts for all movies in a genre:
```
scrapy crawl imsdb_genre -a target_url="https://imsdb.com/genre/Comedy" -o comedy_movies.jsonl
```
