# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SchoolershipscraperItem(scrapy.Item):
    name = scrapy.Field()
    tentative_date = scrapy.Field()
    award = scrapy.Field()
    eligibility = scrapy.Field()
    last_updated = scrapy.Field()
    image = scrapy.Field()
    link = scrapy.Field()

