import scrapy

class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        books = response.css('article.product_pod')

        for book in books:
            relevent_url = book.css('h3 a').attrib['href']
            if relevent_url is not None:
                if "catalogue/" not in relevent_url:
                    book_url = "https://books.toscrape.com/catalogue/" + relevent_url
                    yield response.follow(book_url,callback = self.parse_book_page)
                else:
                    book_url = "https://books.toscrape.com/" + relevent_url
                    yield response.follow(book_url,callback = self.parse_book_page)

        next_page = response.css('li.next a').attrib['href']
        if next_page is not None:
            if "catalogue/" not in next_page:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
                yield response.follow(next_page_url,callback = self.parse)
            else:
                next_page_url = "https://books.toscrape.com/" + next_page
                yield response.follow(next_page_url,callback = self.parse)

    def parse_book_page(self,response):
        page = response.css('article.product_page')
        table_row = response.css("table tr")

        for content in page:
            yield {
                'Title' : content.css('.product_main h1::text').get(),
                'Price' : content.css('.product_main p.price_color::text').get(),
                'Genre' : response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
                'Discription' : response.xpath("//article[@class='product_page']/p/text()").get(),
                'Availablity' : table_row[6].css("td ::text").get(),
            }