import scrapy
from scrapy.item import Item, Field
from selenium import webdriver
from selenium.common.exceptions import  NoSuchElementException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductItem(Item):
    name = Field()
    breadcrumb = Field()


class WoolworthsSpider(scrapy.Spider):
    name = "woolworths"
    allowed_domains = ["woolworths.com.au"]
    start_urls = ["https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas"]
    item_scraped_count = 0
    def parse(self, response):
    
        driver = webdriver.Chrome()
        # navigate to the page
        driver.get("https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas")

        # wait for the breadcrumb to appear
        wait = WebDriverWait(driver, 60)
        breadcrumb = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "breadcrumbs"))).text.split(sep="\n")
        breadcrumb = breadcrumb[1:]  # skip the "Home" link
        # extract product information from each product card
        product_grid = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-grid-v2")))

        # extract product information from each product card
        product_cards = product_grid.find_elements(By.CLASS_NAME, "product-grid-v2--tile")

        # Close the browser
        L=[]
        for product in product_cards[:len(product_cards)]:
            try:
                product_name = product.find_element(By.CLASS_NAME, "product-title-link").text
                item = ProductItem()
                item["name"]=product_name
                item["breadcrumb"]=breadcrumb
                L.append(product_name)
                yield item
            except NoSuchElementException:
                product_name="error"




