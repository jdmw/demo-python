import scrapy

class MovieSpider(scrapy.Spider):
    name = 'blogspider'
    # start_urls = ['https://blog.scrapinghub.com']

    def start_requests(self):
        yield scrapy.Request('https://www.baidu.com/s?wd=' % urllib.quote(wd))
        
    def parse(self, response):
        for title in response.css('h2.t'):
            yield {'title': title.css('a ::text').get()}

        # for next_page in response.css('a.next-posts-link'):
            # yield response.follow(next_page, self.parse)

# run: scrapy crawl spider1 -a wd=electronics