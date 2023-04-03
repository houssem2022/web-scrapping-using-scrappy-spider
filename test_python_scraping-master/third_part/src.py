import json
import gzip
import csv
import logging


class ProductCatalog:
    def __init__(self, data_file):
        self.products = []
        self.logger = logging.getLogger(__name__)
        try:
            with gzip.open(data_file, 'r') as f:
                data = json.load(f)
                for product in data['Bundles']:
                    if 'Products' in product:         
                        if  len(product["Products"])==1:     
                            if  'Price' in product["Products"][0] and 'IsInStock' in product["Products"][0]:   
                                self.products.append(product)

        except Exception as e:
            self.logger.error(f"Failed to load data from file {data_file}: {e}")

    def print_products(self):
        for product in self.products:
            if product["Products"][0]['IsInStock']==True:
                name = product['Name'][:30]
                price = round(product["Products"][0]["Price"], 1)
                print(f"You can buy {name} at our store at {price}$")
            else:
                name = product['Name'][:30]
                id = product["Products"][0]["Stockcode"]
                print(f"{name}  {id}")


    def save_available_products_to_csv(self, csv_file):
        try:
            with open(csv_file, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(['Product Name', 'Product Price'])
                for product in self.products:
                    if product["Products"][0]['IsInStock']==True:
                        name = product['Name']
                        price = product["Products"][0]["Price"]
                        writer.writerow([name, price])
        except Exception as e:
            self.logger.error(f"Failed to save available products to CSV file {csv_file}: {e}")


catalog = ProductCatalog('data/data.json.gz')
catalog.print_products()
catalog.save_available_products_to_csv('available_products.csv')