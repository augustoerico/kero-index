# -*- coding: utf-8 -*-
import scrapy
import re
from functools import partial
import json


class StoreSpider(scrapy.Spider):
    name = 'store_spider'
    start_urls = [
        'https://www.queromania.com/product-page/camisola-demillus-soltinha',
        'https://www.queromania.com/product-page/sutiã-maternal',
        'https://www.queromania.com/product-page/sutiã-modellare',
        'https://www.queromania.com/product-page/calça-cavada-nova-gallard',
        'https://www.queromania.com/product-page/sutiã-flautim',
        'https://www.queromania.com/product-page/anágua-chantal',
        'https://www.queromania.com/product-page/sutiã-colonial',
        'https://www.queromania.com/product-page/calça-nova-chanson',
        'https://www.queromania.com/product-page/sutiã-novo-violão',
        'https://www.queromania.com/product-page/calça-clássica-safira',
        'https://www.queromania.com/product-page/sutiã-safira',
        'https://www.queromania.com/product-page/sutiã-gallard-control',
        'https://www.queromania.com/product-page/sutiã-novo-badine',
        'https://www.queromania.com/product-page/calça-baixa-fofita',
        'https://www.queromania.com/product-page/sutiã-fofita',
        'https://www.queromania.com/product-page/calça-baixa-recreio',
        'https://www.queromania.com/product-page/sutiã-recreio',
        'https://www.queromania.com/product-page/calça-baixa-demillus-menina',
        'https://www.queromania.com/product-page/sutiã-demillus-menina',
        'https://www.queromania.com/product-page/calça-cavada-candence',
        'https://www.queromania.com/product-page/taça-c-baroneza',
        'https://www.queromania.com/product-page/calça-cavada-cítara',
        'https://www.queromania.com/product-page/taça-c-support',
        'https://www.queromania.com/product-page/calça-nova-bibelô',
        'https://www.queromania.com/product-page/sutiã-bibelô',
        'https://www.queromania.com/product-page/calça-cavada-poás',
        'https://www.queromania.com/product-page/sutiã-poás',
        'https://www.queromania.com/product-page/calça-cavada-olimpo',
        'https://www.queromania.com/product-page/sutiã-olimpo-anizete',
        'https://www.queromania.com/product-page/calça-cavada-firantela',
        'https://www.queromania.com/product-page/sutiã-olimpo-firantela',
        'https://www.queromania.com/product-page/calça-cavada-abrupt',
        'https://www.queromania.com/product-page/sutiã-bourbon',
        'https://www.queromania.com/product-page/calça-nova-bourbon',
        'https://www.queromania.com/product-page/sutiã-olimpo-bourbon',
        'https://www.queromania.com/product-page/camisola-roterdam',
        'https://www.queromania.com/product-page/robe-curto-roterdam',
        'https://www.queromania.com/product-page/calça-cavada-sunflower',
        'https://www.queromania.com/product-page/sutiã-olimpo-sunflower',
        'https://www.queromania.com/product-page/sutiã-sunflower',
        'https://www.queromania.com/product-page/fio-dental-candence',
        'https://www.queromania.com/product-page/sutiã-invejja',
        'https://www.queromania.com/product-page/calça-cavada-pele-de-seda',
        'https://www.queromania.com/product-page/sutiã-sensa',
        'https://www.queromania.com/product-page/sutiã-moderato',
        'https://www.queromania.com/product-page/top-esportivo-ultraleve',
        'https://www.queromania.com/product-page/calça-short-ultraleve',
        'https://www.queromania.com/product-page/bustiê-faixa-ultraleve',
        'https://www.queromania.com/product-page/calça-alta-ultraleve',
        'https://www.queromania.com/product-page/calça-cavada-nova-ultraleve',
        'https://www.queromania.com/product-page/biquíni-ultraleve',
        'https://www.queromania.com/product-page/sutiã-nadador-ultraleve',
        'https://www.queromania.com/product-page/calça-clássica-secret',
        'https://www.queromania.com/product-page/calça-clássica-cotton',
        'https://www.queromania.com/product-page/sutiã-secret',
        'https://www.queromania.com/product-page/calça-cavada-secret-cotton',
        'https://www.queromania.com/product-page/calça-cavada-lithos-cotton',
        'https://www.queromania.com/product-page/sutiã-olimpo-cotton',
        'https://www.queromania.com/product-page/biquíni-arazul',
        'https://www.queromania.com/product-page/blusa-vendome',
        'https://www.queromania.com/product-page/calça-baixa-aubade',
        'https://www.queromania.com/product-page/sutiã-top-aubade',
        'https://www.queromania.com/product-page/biquíni-demillus-bali',
        'https://www.queromania.com/product-page/sutiã-novo-ultraleve',
        'https://www.queromania.com/product-page/liga-demillus',
        'https://www.queromania.com/product-page/biquíni-gerbe',
        'https://www.queromania.com/product-page/sutiã-gerbe',
        'https://www.queromania.com/product-page/biquíni-caribdis',
        'https://www.queromania.com/product-page/sutiã-caribdis',
        'https://www.queromania.com/product-page/fio-dental-cálice',
        'https://www.queromania.com/product-page/sutiã-cálice',
        'https://www.queromania.com/product-page/extensor-costas-decotadas',
        'https://www.queromania.com/product-page/lave-calcinha',
        'https://www.queromania.com/product-page/extensor-triplo',
        'https://www.queromania.com/product-page/extensor-duplo',
        'https://www.queromania.com/product-page/biquíni-sensa',
        'https://www.queromania.com/product-page/sutiã-nadador-sensa',
        'https://www.queromania.com/product-page/calça-baixa-invejja',
        'https://www.queromania.com/product-page/bermuda-rendada-virtuel',
        'https://www.queromania.com/product-page/bermuda-espumada-virtuel',
        'https://www.queromania.com/product-page/bermuda-virtuel',
        'https://www.queromania.com/product-page/combinação-virtuel',
        'https://www.queromania.com/product-page/sutiã-super-up-miracle',
        'https://www.queromania.com/product-page/bustiê-marilyn',
        'https://www.queromania.com/product-page/bustiê-sibari',
        'https://www.queromania.com/product-page/bustiê-vertigem',
        'https://www.queromania.com/product-page/bustiê-arpa',
        'https://www.queromania.com/product-page/calça-baixa-virtuel',
        'https://www.queromania.com/product-page/biquíni-virtuel',
        'https://www.queromania.com/product-page/calça-short-nova-promenade',
        'https://www.queromania.com/product-page/sutiã-promenade',
        'https://www.queromania.com/product-page/calça-cavada-nova-habella',
        'https://www.queromania.com/product-page/sutiã-habella',
        'https://www.queromania.com/product-page/boxer-kid-ultraleve',
        'https://www.queromania.com/product-page/cueca-slip-kid',
        'https://www.queromania.com/product-page/calcinha-demillus-girl',
        'https://www.queromania.com/product-page/pijama-kids-âncora',
        'https://www.queromania.com/product-page/pijama-kit-skate',
        'https://www.queromania.com/product-page/shortdoll-unicórnio',
        'https://www.queromania.com/product-page/bermuda-alta-modeladora',
        'https://www.queromania.com/product-page/cinturita-ritmo',
        'https://www.queromania.com/product-page/calça-comprida-oncinha',
        'https://www.queromania.com/product-page/top-oncinha',
        'https://www.queromania.com/product-page/saia-short-estampa-jeans',
        'https://www.queromania.com/product-page/calça-comprida-estampa-jeans',
        'https://www.queromania.com/product-page/blusa-demillus-cintilante',
        'https://www.queromania.com/product-page/top-demillus-poás',
        'https://www.queromania.com/product-page/mochila-saco',
        'https://www.queromania.com/product-page/meia-ritmo',
        'https://www.queromania.com/product-page/calça-comprida-demillus-poás',
        'https://www.queromania.com/product-page/top-guinee',
        'https://www.queromania.com/product-page/camiseta-nadador-hipslip',
        'https://www.queromania.com/product-page/calça-comprida-guinee',
        'https://www.queromania.com/product-page/top-2-em-1-ultraleve',
        'https://www.queromania.com/product-page/modelador-saudável',
        'https://www.queromania.com/product-page/cinta-modellare',
        'https://www.queromania.com/product-page/calça-abdominal-ultraleve',
        'https://www.queromania.com/product-page/calça-cinturita-ultraleve',
        'https://www.queromania.com/product-page/cinta-abdominal-modeladora',
        'https://www.queromania.com/product-page/camisete-support',
        'https://www.queromania.com/product-page/blusa-modellare',
        'https://www.queromania.com/product-page/modelador-violino',
        'https://www.queromania.com/product-page/modelador-support',
        'https://www.queromania.com/product-page/cinta-nova-violão',
        'https://www.queromania.com/product-page/cinta-nova-shadow',
        'https://www.queromania.com/product-page/cinta-massaggio-control',
        'https://www.queromania.com/product-page/cinta-abdominal-desejo',
        'https://www.queromania.com/product-page/sunga-zeus',
        'https://www.queromania.com/product-page/slip-zeus',
        'https://www.queromania.com/product-page/sungão-zeus',
        'https://www.queromania.com/product-page/boxer-ritmo',
        'https://www.queromania.com/product-page/boxer-vik',
        'https://www.queromania.com/product-page/boxer-celta-ultraleve',
        'https://www.queromania.com/product-page/miniboxer-barra',
        'https://www.queromania.com/product-page/miniboxer-rantelli',
        'https://www.queromania.com/product-page/slip-rantelli',
        'https://www.queromania.com/product-page/sungão-vik',
        'https://www.queromania.com/product-page/boxer-zeus-esportiva',
        'https://www.queromania.com/product-page/miniboxer-vik-anatômica',
        'https://www.queromania.com/product-page/boxer-lover',
        'https://www.queromania.com/product-page/boxer-júnior-ultraleve',
        'https://www.queromania.com/product-page/boxer-adulto-ultraleve',
        'https://www.queromania.com/product-page/boxer-átila-ultraleve',
        'https://www.queromania.com/product-page/pijama-bermuda-zeus',
        'https://www.queromania.com/product-page/pijama-curto-âncora',
        'https://www.queromania.com/product-page/shortdoll-lybito',
        'https://www.queromania.com/product-page/camisola-lybito',
        'https://www.queromania.com/product-page/robe-demillus-canela',
        'https://www.queromania.com/product-page/camisola-demillus-canela',
        'https://www.queromania.com/product-page/shortdoll-demillus-canela',
        'https://www.queromania.com/product-page/camisola-travessia',
        'https://www.queromania.com/product-page/shortdoll-infantil-demillus-travessia',
        'https://www.queromania.com/product-page/shortdoll-travessia',
        'https://www.queromania.com/product-page/pantufa-atoalhada',
        'https://www.queromania.com/product-page/pijama-longo-pointelle',
        'https://www.queromania.com/product-page/shortdoll-pointelle',
        'https://www.queromania.com/product-page/camisola-arpa',
        'https://www.queromania.com/product-page/robe-nupcial',
        'https://www.queromania.com/product-page/calça-clássica-cecille',
        'https://www.queromania.com/product-page/sutiã-cecille',
        'https://www.queromania.com/product-page/sutiã-pudique',
        'https://www.queromania.com/product-page/bustiê-lieve',
        'https://www.queromania.com/product-page/clip-magic-up',
        'https://www.queromania.com/product-page/biquíni-demillus-gueixa',
        'https://www.queromania.com/product-page/sutiã-demillus-gueixa',
        'https://www.queromania.com/product-page/shortdoll-demillus-gueixa',
        'https://www.queromania.com/product-page/calça-clássica-canção',
        'https://www.queromania.com/product-page/sutiã-canção',
        'https://www.queromania.com/product-page/biquíni-chansonete',
        'https://www.queromania.com/product-page/sutiã-chansonete',
        'https://www.queromania.com/product-page/sutiã-super-up-desejo-plus',
        'https://www.queromania.com/product-page/biquíni-demillus-fashion',
        'https://www.queromania.com/product-page/sutiã-demillus-fashion',
        'https://www.queromania.com/product-page/body-danube',
        'https://www.queromania.com/product-page/biquíni-danube',
        'https://www.queromania.com/product-page/top-danube',
        'https://www.queromania.com/product-page/sutiã-nadador-jil',
        'https://www.queromania.com/product-page/biquíni-jil',
        'https://www.queromania.com/product-page/sutiã-top-jil',
        'https://www.queromania.com/product-page/shortdoll-gradisca',
        'https://www.queromania.com/product-page/camisola-nova-gradisca',
        'https://www.queromania.com/product-page/biquíni-gradisca',
        'https://www.queromania.com/product-page/sutiã-gradisca',
        'https://www.queromania.com/product-page/calça-baixa-nova-candide',
        'https://www.queromania.com/product-page/sutiã-candide',
        'https://www.queromania.com/product-page/fio-dental-novo-idylle',
        'https://www.queromania.com/product-page/sutiã-super-up-intenção',
        'https://www.queromania.com/product-page/liga-support',
        'https://www.queromania.com/product-page/gargantilha-demillus',
        'https://www.queromania.com/product-page/calça-baixa-gemma',
        'https://www.queromania.com/product-page/sutiã-gemma',
        'https://www.queromania.com/product-page/camisola-ferveur',
        'https://www.queromania.com/product-page/bracelete-cabaret',
        'https://www.queromania.com/product-page/biquíni-kismet',
        'https://www.queromania.com/product-page/sutiã-nadador-kismet',
        'https://www.queromania.com/product-page/fio-dental-chic-demillus',
        'https://www.queromania.com/product-page/sutiã-grenade',
        'https://www.queromania.com/product-page/máscara-chic-demillus',
        'https://www.queromania.com/product-page/fio-dental-xamego',
        'https://www.queromania.com/product-page/biquíni-copacabana',
        'https://www.queromania.com/product-page/fio-dental-purisme',
        'https://www.queromania.com/product-page/calça-baixa-purisme',
        'https://www.queromania.com/product-page/sutiã-purisme',
        'https://www.queromania.com/product-page/fio-dental-di-carla',
        'https://www.queromania.com/product-page/sutiã-top-di-carla',
        'https://www.queromania.com/product-page/camisola-di-carla',
        'https://www.queromania.com/product-page/fio-dental-aubade',
        'https://www.queromania.com/product-page/sutiã-aubade',
        'https://www.queromania.com/product-page/tanga-demillus-brilho',
        'https://www.queromania.com/product-page/body-aubade',
        'https://www.queromania.com/product-page/fio-dental-demillus-flor',
        'https://www.queromania.com/product-page/sutiã-demillus-flor',
        'https://www.queromania.com/product-page/biquíni-dido',
        'https://www.queromania.com/product-page/sutiã-nadador-dido',
        'https://www.queromania.com/product-page/tanga-candy-baby',
        'https://www.queromania.com/product-page/sutiã-candy-baby',
        'https://www.queromania.com/product-page/fio-dental-miótis',
        'https://www.queromania.com/product-page/camisola-miótis',
        'https://www.queromania.com/product-page/calça-baixa-miótis',
        'https://www.queromania.com/product-page/sutiã-miótis',
        'https://www.queromania.com/product-page/calça-baixa-tatiana',
        'https://www.queromania.com/product-page/sutiã-top-tatiana',
        'https://www.queromania.com/product-page/camisola-tatiana',
        'https://www.queromania.com/product-page/legging-jeans',
        'https://www.queromania.com/product-page/body-novo-modellare',
        'https://www.queromania.com/product-page/body-vectra',
        'https://www.queromania.com/product-page/legging-bordada-jeans',
        'https://www.queromania.com/product-page/tanga-lousane',
        'https://www.queromania.com/product-page/calça-baixa-lousane',
        'https://www.queromania.com/product-page/sutiã-top-lousane',
        'https://www.queromania.com/product-page/fio-dental-nova-rivali',
        'https://www.queromania.com/product-page/sutiã-nova-rivali',
        'https://www.queromania.com/product-page/fio-dental-poeme',
        'https://www.queromania.com/product-page/camisola-poeme',
        'https://www.queromania.com/product-page/calça-baixa-poeme',
        'https://www.queromania.com/product-page/sutiã-poeme',
        'https://www.queromania.com/product-page/sutiã-meia-noite',
        'https://www.queromania.com/product-page/biquíni-antínea',
        'https://www.queromania.com/product-page/corselete-antínea',
        'https://www.queromania.com/product-page/fio-dental-demillus-biscuit',
        'https://www.queromania.com/product-page/corselete-demillus-biscuit',
        'https://www.queromania.com/product-page/calça-clássica-merlot',
        'https://www.queromania.com/product-page/sutiã-merlot',
        'https://www.queromania.com/product-page/biquíni-demillus-negri',
        'https://www.queromania.com/product-page/sutiã-nadador-demillus-negri',
        'https://www.queromania.com/product-page/camisola-demillus-negri',
        'https://www.queromania.com/product-page/fio-dental-sonata',
        'https://www.queromania.com/product-page/sutiã-sonata',
        'https://www.queromania.com/product-page/calça-baixa-demillus-bolero',
        'https://www.queromania.com/product-page/sutiã-demillus-bolero',
        'https://www.queromania.com/product-page/biquíni-nytelle',
        'https://www.queromania.com/product-page/sutiã-top-nytelle',
        'https://www.queromania.com/product-page/sutiã-tirinhas-frontais',
        'https://www.queromania.com/product-page/top-cabaret',
        'https://www.queromania.com/product-page/top-amarração-floresta',
        'https://www.queromania.com/product-page/top-cortinão-floresta',
        'https://www.queromania.com/product-page/maiô-floresta',
        'https://www.queromania.com/product-page/calça-torcida-floresta',
        'https://www.queromania.com/product-page/calça-hot-pants-floresta',
        'https://www.queromania.com/product-page/top-listras',
        'https://www.queromania.com/product-page/calça-listras',
        'https://www.queromania.com/product-page/maiô-listras',
        'https://www.queromania.com/product-page/top-hibisco',
        'https://www.queromania.com/product-page/calça-babado-hibisco',
        'https://www.queromania.com/product-page/maiô-babado-hibisco',
        'https://www.queromania.com/product-page/top-alongado-palmeira',
        'https://www.queromania.com/product-page/top-babado-palmeira',
        'https://www.queromania.com/product-page/calça-fru-fru-palmeira',
        'https://www.queromania.com/product-page/calça-hot-pants-palmeira',
        'https://www.queromania.com/product-page/top-com-aro-xadrez',
        'https://www.queromania.com/product-page/top-conforto-xadrez',
        'https://www.queromania.com/product-page/calça-com-drapeado-xadrez',
        'https://www.queromania.com/product-page/calça-hot-pants-xadrez',
        'https://www.queromania.com/product-page/top-cortinão-zig-zag',
        'https://www.queromania.com/product-page/top-alto-zig-zag',
        'https://www.queromania.com/product-page/calça-fru-fru-zig-zag',
        'https://www.queromania.com/product-page/calça-amarrados-zig-zag',
        'https://www.queromania.com/product-page/maiô-zig-zag',
        'https://www.queromania.com/product-page/saída-de-praia-zig-zag',
        'https://www.queromania.com/product-page/sacola-frente-estampada',
        'https://www.queromania.com/product-page/sandália-paris'
    ]

    @staticmethod
    def parse_product(url, response):
        body = response.body.decode('utf-8')
        matcher = re.search('<script\s+type=\"application/ld\+json\">(.+)</script>', body)

        product = json.loads(matcher.group(1))
        name = product['name']
        price = product['offers']['price']
        description = product['description']
        image = product['image']

        yield {
            'url': url,
            'price': price,
            'name': name,
            'description': description,
            'image': image
            # 'product': product
        }

    def parse(self, response):
        body = response.body.decode('utf-8')

        product_matcher = re.search(r'https://www\.queromania\.com/product-page/(.+)', response.url)
        instance_matcher = re.search('"appDefinitionName":"Wix Stores","instance":"(.+?)"', body)

        url = 'https://ecom.wix.com/storefront/product/' + product_matcher.group(1) + '?instance=' + \
              instance_matcher.group(1)
        callback = partial(StoreSpider.parse_product, response.url)

        yield scrapy.Request(url=url, callback=callback)
