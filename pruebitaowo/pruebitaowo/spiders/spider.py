import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import CloseSpider
from pruebitaowo.items import PruebitaowoItem

class PruebitaSpider(CrawlSpider):
	name = 'pruebita'
	item_count = 0 #contador para no hacer hasta el infnito :V
	allowed_domain = ['www.mercadolibre.com.pe']
	start_urls = ['https://listado.mercadolibre.com.pe/page1-televisores']

	rules = {
		Rule(LinkExtractor(allow = (), restrict_xpaths = ('//li[@class="andes-pagination__button andes-pagination__button--next shops__pagination-button"]/a'))),
		Rule(LinkExtractor(allow =(), restrict_xpaths = ('//div[@class="ui-search-item__group ui-search-item__group--title shops__items-group"]/a[1]')),
							callback = 'parse_item', follow = False)
	}

	def parse_item(self, response):
		ml_item = PruebitaowoItem()
		#info del producto
		ml_item['titulo'] = response.xpath('normalize-space(//div/h1[@class="ui-pdp-title"]/text())').extract_first()
		ml_item['modelo'] = response.xpath('normalize-space(//*[@id=":R2jfpasdbp7k:"]/span/text())').extract()
		ml_item['marca'] = response.xpath('normalize-space(//*[@id=":R2j7pasdbp7k:"]/span/text())').extract()
	#	ml_item['tecnologia'] = response.xpath('normalize-space(/html/body/main/div/div/div[1]/div[1]/section[1]/div/section[2]/ul/li[1]/span)').extract()
	#	ml_item['tipo'] = response.xpath('normalize-space(/html/body/main/div/div/div[1]/div[1]/section[1]/div/section[2]/ul/li[2]/span)').extract()
		ml_item['precio'] = response.xpath('normalize-space(//div[@class="ui-pdp-price__second-line"]/span/span[@class="andes-visually-hidden"]/text())').extract()
		ml_item['condicion'] = response.xpath('normalize-space(//div[@class="ui-pdp-header"]/div/span[1]/text())').extract()
		ml_item['envio'] = response.xpath('normalize-space(//*[@id="buybox-form"]/div[1]/div/div/p[1]/span/text())').extract()
	#	ml_item['ubicacion'] = response.xpath('normalize-space(//p[contains(@class, "card-description")])').extract()
		ml_item['opiniones'] = response.xpath('normalize-space(//div[@class="ui-review-capability__rating"]/div/p/text())').extract()

		#info de la tienda o vendedor
		ml_item['vendedor_url'] = response.xpath('//*[@id="ui-pdp-main-container"]/div[2]/div/div[2]/div[1]/a/@href').extract()
	#	ml_item['tipo_vendedor'] = response.xpath('normalize-space(//p[contains(@class, "power-seller")]/text())').extract()
		ml_item['ventas_vendedor'] = response.xpath('normalize-space(//div[@class="ui-pdp-seller__reputation-info"]/ul/li[1]/strong/text())').extract()
		
		
		self.item_count += 1
		if self.item_count > 300:
			raise CloseSpider('item_exceeded')
		yield ml_item
