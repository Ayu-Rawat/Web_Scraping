import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            yield {
                'Name': book.css('h3 a::text').get(),
                'Price': book.css('div.product_price .price_color::text').get(),
                'Url' : book.css('h3 a').attrib['href'],
            }

        next_page = response.css('li.next a').attrib['href']
        if next_page is not None:
            if "catalogue/" not in next_page:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
                yield response.follow(next_page_url,callback = self.parse)
            else:
                next_page_url = "https://books.toscrape.com/" + next_page
                yield response.follow(next_page_url,callback = self.parse)

