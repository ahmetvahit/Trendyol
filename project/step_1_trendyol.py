import json
import scrapy
from scrapy.crawler import CrawlerProcess


class crawl(scrapy.Spider):
    name = "crawl"
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }
    output = []
    url = "https://www.trendyol.com/atari/retro-mini-620-mario-oyunlu-av-retro-mini-oyun-konsolu-scart-basliksiz-p-36587919"

    def start_requests(self):
        yield scrapy.Request(self.url, callback=self.continues,
                             headers=self.headers,
                             dont_filter=True)

    def continues(self, response):

        pname = response.xpath("//h3[@class='detail-name']/text()").get()
        price_org = response.xpath("//span[@class='prc-org']/text()").get()
        price_dsc = response.xpath("//span[@class='prc-dsc']/text()").get()

        if price_org == '':
            sellingPrice = price_org
            discountedPrice = price_dsc
            is_promoted = True
        else:
            sellingPrice = price_dsc
            discountedPrice = 0
            is_promoted = False

        sellingPrice = float(sellingPrice.replace('TL', '').replace(',', '.').strip()) if sellingPrice else 0
        discountedPrice = float(
            str(discountedPrice).replace('TL', '').replace(',', '.').strip()) if discountedPrice else 0

        category = response.xpath("//div[@id='marketing-product-detail-breadcrumb']/div/a/@title").getall()
        breadcrump = '. '.join(category)

        m_name = response.xpath("//div[@class='merchant-box-wrapper']/a/text()").get()
        m_city = 'İstanbul'
        m_sellerScore = 9.3

        detail = response.xpath("//script[@type='application/javascript']/text()")[1].get()
        seller_names = [i.split("merchantBadges")[1].split("name")[-1].replace('":"', "").replace('","', "") for i in
                        detail.split("officialName")[:-1]]
        city_names = [i.split(":")[1].split(",")[0].replace('"', "") for i in detail.split("cityName")[1:]]
        seller_scores = [float(i.split('sellerScore":')[1].replace(",", "")) for i in
                         detail.split('"sellerScoreColor"')[:-1]]

        self.output.append({
            "product_name": pname,
            "brand": None,
            "product_price": sellingPrice,
            "product_discount_price": discountedPrice,
            "product_is_promoted": is_promoted,
            "sub_category_name": breadcrump,
            "sales_ch": m_name,
            "city": m_city,
            "score": m_sellerScore,
            "sellers_name": seller_names,
            "city_names": city_names,
            "seller_scores": seller_scores,

        })

    def close(self, spider, reason):
        with open("samples.json", "w", encoding="utf-8") as f:
            json.dump(self.output, f, ensure_ascii=False)
            #
            # df = pd.read_json(json.dumps(self.output, ensure_ascii=False), encoding="utf-8")
            # df.to_excel("sample.xlsx",encoding="utf-8", index=False)


process = CrawlerProcess()
process.crawl(crawl)
process.start()
