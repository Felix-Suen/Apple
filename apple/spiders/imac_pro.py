import scrapy
from apple.items import Imac_proItem

class Imac_pro(scrapy.Spider):
    name = 'imac pro'
    start_urls = ['https://www.apple.com/shop/buy-mac/imac-pro']

    # list of valid country codes obtained from country_code.py
    codes = ['/', '/ae/', '/au/', '/cn/', '/hk/', '/jp/',
             '/kr/', '/my/', '/nz/', '/ph/', '/sg/', '/tw/', '/th/',
             '/cz/', '/dk/', '/de/', '/es/', '/fr/', '/ie/', '/it/',
             '/lu/', '/hu/', '/nl/', '/no/', '/at/', '/pl/',
             '/pt/', '/ru/', '/fi/', '/se/', '/tr/', '/uk/',
             '/br/', '/mx/', '/ca/']

    def parse(self, response):
        for next_code in Imac_pro.codes:
            next_country = 'https://www.apple.com' + next_code + 'shop/buy-mac/imac-pro'
            yield response.follow(next_country, callback=self.next_price)

    def next_price(self, response):
        imac_item = Imac_proItem()
        price = response.css('.as-price-currentprice span::text').re('[^\s-].*[^\s-]')
        location = response.css('title::text').re('\(.+\)')
        imac_item['price'] = price
        if price == ['$4,999.00']:
            imac_item['location'] = ['(US)']
        elif price == ['￥558,800 (税別)']:
            imac_item['location'] = ['(JP)']
        else:
            imac_item['location'] = location

        yield imac_item


