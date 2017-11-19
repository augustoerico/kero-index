# -*- coding: utf-8 -*-
import scrapy
import re
from functools import partial


class StoreSpider(scrapy.Spider):
    name = 'store_spider'
    # allowed_domains = ['www.queromania.com/loja']
    start_urls = ['https://www.queromania.com/loja/']

    @staticmethod
    def parse_product(response):
        body = response.body.decode('utf-8')
        matcher = re.search('<script\s+type=\"application/ld\+json\">(.+)</script>', body)
        product_details = matcher.group(1)
        yield {
            'product': product_details
        }

    @staticmethod
    def parse_product_page(product, response):
        body = response.body.decode('utf-8')
        matcher = re.search('"appDefinitionName":"Wix Stores","instance":"(.+?)"', body)
        url = 'https://ecom.wix.com/storefront/product/' + product + '?instance=' + matcher.group(1)
        yield scrapy.Request(url=url, callback=StoreSpider.parse_product)

    @staticmethod
    def parse_gallery(response):
        body = response.body.decode('utf-8')
        matches = re.findall('"urlPart":"(.+?)"', body)

        for m in matches:
            url = 'https://www.queromania.com/product-page/' + m
            callback = partial(StoreSpider.parse_product_page, m)
            yield scrapy.Request(url=url, callback=callback)

    def parse(self, response):
        body = response.body.decode('utf-8')
        matcher = re.search('"appDefinitionName":"Wix Stores","instance":"(.+?)"', body)
        url = 'https://ecom.wix.com/storefront/gallery?instance=' + matcher.group(1)
        yield scrapy.Request(url=url, callback=StoreSpider.parse_gallery)

        # TODO yield "See more"
