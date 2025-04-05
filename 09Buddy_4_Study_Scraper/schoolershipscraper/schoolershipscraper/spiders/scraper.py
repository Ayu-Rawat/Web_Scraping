import scrapy
from bs4 import BeautifulSoup
from schoolershipscraper.items import SchoolershipscraperItem

class BSSpider(scrapy.Spider):
    name = 'scraper'
    start_urls = ['http://127.0.0.1:5500/09Buddy_4_Study_Scraper/offlineFile.html']
    
    custom_settings = {
        'FEEDS': {
            'scholarship.json': {'format': 'json', 'overwrite': True},
        }
    }
    
    def parse(self, response):
        # Parse with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find scholarship boxes
        cards = soup.select('a.Listing_categoriesBox__CiGvQ')
        self.logger.info(f"Found {len(cards)} cards with BeautifulSoup")
        
        for card in cards:
            item = SchoolershipscraperItem()
            
            # Extract scholarship name
            name_elem = card.select_one('h4.Listing_scholarshipName__VLFMj p')
            item['name'] = name_elem.text.strip() if name_elem else ''
            
            # Extract tentative date
            date_elem = card.select_one('h4.Listing_tentative__DyeVG')
            item['tentative_date'] = date_elem.text.strip() if date_elem else ''
            
            # Extract award and eligibility
            award_blocks = card.select('div.Listing_awardCont__qnjQK')
            
            if len(award_blocks) >= 1:
                award_text = award_blocks[0].select_one('div.Listing_rightAward__DxMQV p span')
                item['award'] = award_text.text.strip() if award_text else ''
            else:
                item['award'] = ''
                
            if len(award_blocks) >= 2:
                elig_text = award_blocks[1].select_one('div.Listing_rightAward__DxMQV p span')
                item['eligibility'] = elig_text.text.strip() if elig_text else ''
            else:
                item['eligibility'] = ''
            
            # Extract last updated
            updated_elem = card.select_one('div.Listing_categoriesRight__7Zjyu p span')
            item['last_updated'] = updated_elem.text.strip() if updated_elem else ''
            
            # Extract image URL
            img_elem = card.select_one('div.Listing_categoriesPart__kpHTV img')
            item['image'] = img_elem.get('src') if img_elem else ''
            
            # Extract link
            item['link'] = response.urljoin(card.get('href', ''))
            
            self.logger.info(f"Extracted: {item['name']}")
            yield item