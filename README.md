# imsdb_scrapers
Spiders and scrapers for the Internet Movie Script Database (IMSDB)

## getting started

Install scrapy, e.g.:
```
conda create --name imsdb_scraping python=3.11  
conda activate imsdb_scraping
conda install scrapy
```

Download scripts from a show, e.g.:
```
scrapy crawl imsdb_show -a target_url="https://imsdb.com/TV/Futurama.html" -o futurama.jsonl
```
