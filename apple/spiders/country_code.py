import scrapy

# using scrapy to find all apple websites around the world

class Country(scrapy.Spider):
    name = 'country'
    start_urls = ['https://www.apple.com/choose-country-region/']

    def parse(self, response):
        for countries in response.css('li.countrylist-item'):
            country = countries.css('.block-link::text')[0].extract()
            code = countries.css('a.block::attr(href)')[0].re('\/[a-z]+\/')
            yield {country: code}
