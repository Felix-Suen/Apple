import scrapy
from apple.items import AppleItem

class Apple(scrapy.Spider):
    name = 'macbook pro'
    start_urls = ['https://www.apple.com/shop/buy-mac/macbook-pro']

    # list of valid country codes obtained from country_code.py
    codes = ['/', '/ae/', '/au/', '/cn/', '/hk/', '/jp/',
             '/kr/', '/my/', '/nz/', '/ph/', '/sg/', '/tw/', '/th/',
             '/cz/', '/dk/', '/de/', '/es/', '/fr/', '/ie/', '/it/',
             '/lu/', '/hu/', '/nl/', '/no/', '/at/', '/pl/',
             '/pt/', '/ru/', '/fi/', '/se/', '/tr/', '/uk/',
             '/br/', '/mx/', '/ca/']

    def parse(self, response):
        for next_code in Apple.codes:
            next_country = 'https://www.apple.com' + next_code + 'shop/buy-mac/macbook-pro'
            yield response.follow(next_country, callback=self.next_price)

    def next_price(self, response):
        item = AppleItem()
        price = response.css('.as-price-currentprice span::text')[0].re('[^\s-].*[^\s-]')
        location = response.css('title::text').re('\(.+\)')

        item['price'] = price

        # two websites have exceptions
        if price == ['$1,299.00']:
            item['location'] = ['(US)']
        elif price == ['￥142,800 (税別)']:
            item['location'] = ['(JP)']
        else:
            item['location'] = location

        yield item
