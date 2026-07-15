# IMSDB Scrapers
Spiders and scrapers for the Internet Movie Script Database (IMSDB)

## Getting started

### Installation
Download this git repo and navigate to it. Then install scrapy, e.g.:
```
conda create --name imsdb_scraping python=3.11  
conda activate imsdb_scraping
conda install scrapy
```

### Single tv series scripts - from series page
To download all available scripts for one tv series, run something like
```
scrapy crawl imsdb_show -a target_url="https://imsdb.com/TV/Futurama.html" -o futurama.jsonl
```

### Single movie script - from movie page
To download the script for a movie, run something like
```
scrapy crawl imsdb_movie -a target_url="https://imsdb.com/Movie%20Scripts/500%20Days%20of%20Summer%20Script.html" -o 500dayssummer.jsonl
```

## Bulk scraping

### Bulk listing of tv series script urls
To list the script urls for all available shows as jsonl:
```
scrapy crawl imsdb_show_listing -o show_listings.jsonl
```
The format will be ```{'script_url': ...}``` per line. 

### Bulk listing of movie script urls
To list the script urls for all available movies as jsonl:
```
scrapy crawl imsdb_movie_listing -o movie_listings.jsonl
```
The format will be ```{'script_url': ...}``` per line. 

### Bulk direct scraping - from any script urls
To scrape the scripts for all script urls in a jsonl file ```target_urls```:
```
scrapy crawl imsdb_direct -a targets=target_urls.jsonl -a dones=scripts.jsonl -o scripts.jsonl
```
The format for the ```targets``` file should be ```{'script_url': ...}``` per line.
The ```dones``` file allows resuming where you left off, if the script is shut down before it is done scraping. 
