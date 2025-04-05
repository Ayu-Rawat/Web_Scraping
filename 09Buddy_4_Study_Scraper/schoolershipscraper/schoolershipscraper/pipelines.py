# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SchoolershipscraperPipeline:
    def process_item(self, item, spider):
        
        adapter = ItemAdapter(item)

        # To remove /r/n from data
        adapter['name'] = adapter['name'].replace('\r\n', '')
        adapter['tentative_date'] = adapter['tentative_date'].replace('\r\n', '')
        adapter['award'] = adapter['award'].replace('\r\n', '')
        adapter['eligibility'] = adapter['eligibility'].replace('\r\n', '')
        adapter['last_updated'] = adapter['last_updated'].replace('\r\n', '')

        # To remove extra space
        adapter['eligibility'] = adapter['eligibility'].replace('                                    ', ' ')
        adapter['tentative_date'] = adapter['tentative_date'].replace('                                    ', ' ')
        adapter['name'] = adapter['name'].replace('                                    ', ' ')
        adapter['award'] = adapter['award'].replace('                                    ', ' ')
        adapter['name'] = adapter['name'].replace('                                ', ' ')

        # To remove local path
        adapter['link'] = adapter['link'].replace('http://127.0.0.1:5500','https://www.buddy4study.com')

        return item