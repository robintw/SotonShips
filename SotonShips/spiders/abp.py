# -*- coding: utf-8 -*-
import scrapy
import logging

class AbpSpider(scrapy.Spider):
    name = "abp"
    allowed_domains = ["http://www.southamptonvts.co.uk"]
    start_urls = (
        r'http://www.southamptonvts.co.uk/BackgroundSite/Ajax/LoadXmlFileWithTransform?xmlFilePath=D:\ftp\southampton\Ships_Along_Side\sotberthed.xml&xslFilePath=D:\wwwroot\CMS_Southampton\content\files\assets\sotberthed.xsl&w=43',
    )

    def extract_with_blank(self, col):
        print(col)
        try:
            text = col.xpath('./text()').extract()[0]
        except IndexError:
            text = ""

        return text

    def parse(self, response):
        rows = response.xpath('//tr')
        items = []

        for row in rows[1:]:
            cols = row.xpath('.//td')
            col_text = [self.extract_with_blank(col) for col in cols]

            item = {}
            item['ShipName'] = col_text[0]
            item['LloydsNumber'] = col_text[1]
            item['Type'] = col_text[2]

            print(item)
            items.append(item)
