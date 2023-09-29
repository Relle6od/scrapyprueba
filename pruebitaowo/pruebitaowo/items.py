# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class PruebitaowoItem(scrapy.Item):

    #info de producto
    titulo = scrapy.Field()
    modelo = scrapy.Field()
    marca = scrapy.Field()
    #tecnologia = scrapy.Field()
    #tipo = scrapy.Field()
    precio = scrapy.Field()
    condicion = scrapy.Field()
    envio = scrapy.Field()
    #ubicacion = scrapy.Field()
    opiniones = scrapy.Field()

    #info de la tienda o vendedor
    vendedor_url = scrapy.Field()
   # tipo_vendedor = scrapy.Field()
    ventas_vendedor = scrapy.Field()
    
