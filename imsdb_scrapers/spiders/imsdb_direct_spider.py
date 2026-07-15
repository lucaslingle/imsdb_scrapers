# example:
# ```
#     scrapy crawl imsdb_direct -a targets=target_urls.jsonl -a dones=scripts.jsonl -o scripts.jsonl
# ```

import scrapy
import json

class IMSDBDirectSpider(scrapy.Spider):
    name = "imsdb_direct"

    async def start(self):
        target_urls = self.read_jsonl(self.targets)
        done_urls = set[str](self.read_jsonl(self.dones))
        for url in target_urls:
            if url not in done_urls:
                yield scrapy.Request(url, callback=self.parse_scriptpage)

    def read_jsonl(self, fname):
        urls = []
        with open(fname, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    urls.append(json.loads(line)['script_url'])
        return urls

    def parse_scriptpage(self, response):
        yield {
            "script_url": response.url,
            "script_text": response.css("pre").get()
        }
