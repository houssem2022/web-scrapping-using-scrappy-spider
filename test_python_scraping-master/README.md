In this project we will start a new scrapy project and build a spider that crawls the webpage below,
extracting the products names, and the breadcrumb in a list format. Make sure to take
advantage of Scrapy.Items to output the products.
Test your spider and save the results in a csv file.
Webpage:
```
https://www.woolworths.com.au/shop/browse/drinks/cordials-juices-iced-teas/iced-teas
```
Breadcrumb :
```
Home > Drinks > Cordials, Juices & Iced Teas > Iced Teas
```
The desired format:
```
[“Home”, “Drinks”, “Cordials, Juices & Iced Teas”, “ Iced Teas”]
```
