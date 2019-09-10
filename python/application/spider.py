# scrapy runspider spider.py
# a crawler to download pictures from xnxx.com

import scrapy

class PornPicturesSpider(scrapy.Spider):
    name = 'PornPictures'
    start_urls = ['http://multi.xnxx.com']
    page_num = 1
    custom_settings = {
        'CONCURRENT_REQUESTS_PER_IP': 10
    }

    def parse(self, response):
        for href in response.css('.boxImg a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_gallery)
        self.page_num = self.page_num + 1
        next_page = '%sp-%d' % (self.start_urls[0], self.page_num)
        yield scrapy.Request(next_page, self.parse)

    def parse_gallery(self, response):
        for href in response.css('.boxImg img::attr(src)'):
            full_img_url = response.urljoin(href.extract()).replace('new_small', 'full')
            print full_img_url
            yield scrapy.Request(full_img_url, callback=self.dl_img)

    def dl_img(self, response):
        print response.url
        filename = '_'.join(response.url.split("/")[5:])
        path = 'out/' + filename
        with open(path, 'wb') as f:
            f.write(response.body)
