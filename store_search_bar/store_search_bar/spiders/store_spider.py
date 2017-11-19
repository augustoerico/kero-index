# -*- coding: utf-8 -*-
import scrapy
import re


class StoreSpider(scrapy.Spider):
    name = 'store_spider'
    # allowed_domains = ['www.queromania.com/loja']
    start_urls = ['https://www.queromania.com/loja/']

    @staticmethod
    def parse_product(response):
        body = response.body.decode('utf-8')
        matcher = re.search('"appDefinitionName":"Wix Stores","instance":"(.+?)"', body)


    @staticmethod
    def parse_gallery(response):
        body = response.body.decode('utf-8')
        matches = re.findall('"urlPart":"(.+?)"', body)

        for m in matches:
            url = "https://www.queromania.com/product-page/" + m
            yield scrapy.Request(url=url, callback=StoreSpider.parse_product)

    def parse(self, response):
        body = response.body.decode('utf-8')
        matcher = re.search('"appDefinitionName":"Wix Stores","instance":"(.+?)"', body)
        url = "https://ecom.wix.com/storefront/gallery?instance=" + matcher.group(1)
        yield scrapy.Request(url=url, callback=StoreSpider.parse_gallery)
