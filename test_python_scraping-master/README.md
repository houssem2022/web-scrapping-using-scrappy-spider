# Test scraping python
## Before starting
 * Fork the project in your Gitlab namespace
 * **Caution! very important:** Change project visibility: 
   * Click on `Settings` bottom left, when you see your project 
   * Select `General`
   * Click on expend `Visibility, project features, permissions` 
   * Change project visibility from public to private
## After pushing your codes
 * Add it@dataimpact.fr as **reporter** in `members`
 * Answer the email with your project link in it 
 
# Test
Some really important tips:
 * Comments and code quality are a big plus
 * You need to implement unit tests whenever it is possible
 * You might need pytest (and you can use any other package)
 * There are three parts (algorithm, advanced, scraping)
 * You can use internet
 

## First Part (python algorithm)

### Exercise 1
(I repeat myself I will not correct your test if you don't change visibility of the project from public to private, so please start with this)


In the function exercise_one on first_part.src module:
print every number between 1 and 100 as follows:
 * For every multiple of 3 print "Three".
 * For every multiple of 5 print "Five".
 * And for every multiple of both 3 and 5 print "ThreeFive"

*The output should be as follows:*

```
1
2
Three
4
Five
Three
7
8
Three
Five
11
Three
13
14
ThreeFive
16
```

### Exercise 2 (15 min)
Determine whether a positive integer number is colorful or not.

263 is a colorful number because [2, 6, 3, 2x6, 6x3, 2x6x3] are all different; whereas 236 is not colorful, because [2, 3, 6, 2x3, 3x6, 2x3x6] have 6 twice.

So take all consecutive subsets of digits, take their product and ensure all the products are different.
Examples:
```
263  -->  true
236  -->  false
2532 -->  false
```

### Exercise 3 (10 min)

Write a function calculate that takes a list of strings a returns the sum of the list items that represents an integer (skipping the other items).
Examples
```
calculate(['4', '3', '-2']) ➞ 5
calculate(453) ➞ False
calculate(['nothing', 3, '8', 2, '1']) ➞ 9
calculate('54') ➞ False
```

### Exercise 4 (25 min)
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none.

Examples:

```
anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
```

## Second Part (python advanced)

### Exercise 1 (5 min)

Create a generator named random_gen that generates random numbers (use random module) between 10 and 20 and stops just after giving 15

### Exercise 2 (10 min)

Rewrite decorator_to_str to force the functions "add" and "get_info" to return string values 

### Exercise 3 (10 min)

Rewrite `ignore_exception` so that it ignores the exception in its argument and returns None if this exception raises

### Exercise 4 (20 min)

Write the tests for the class `CacheDecorator` without touching it, some of your tests should not pass because this class is a little buggy. 

### Exercise 5 (10 min)

Write the metaclass `MetaInherList` so that the class `ForceToList` inherits from `list` built-in. (read `test_meta_list` in the tests for more information)

### Exercise 6 (15 min)
Create a metaclass that checks if classes have an attribute named 'process' which must be a method taking 3 arguments

## Third Part (scraping)

### Exercise 1 (5 min)
Create a function http_request that sends a post request to this url https://httpbin.org/anything with this parameters:
```msg=welcomeuser
isadmin=1
```
and return the response body.
Now, send the same request this time by changing the user-agent

### Exercise 2 (20 min)
In src module, create a python class with the following constraints:
  * it imports the data.json.gz file which is located in the third_part/data folder. The file holds information about a category including the products.
  * it prints each available product in this particular format:
“You can buy Product_Name at our store at Product_Price”
where :
    - Product_Name is the product name truncated at 30 .
    - Abbotts Village Bakery Ghrainy Wolemeal 850g ==> Abbotts Village Bakery Grainy
    - Product_Price is the rounded product price in dd.d format
    - Example: 13.34 ==> 13.3

  * if the product is unavailable, it logs the product id and product name.
  * if a clue of the product’s availability can’t be found, it logs an error.
  * it saves the available products in a csv file.
###### P.S :

  * Use any tool/language/method/website to find the products in the json file.
  * To "truncate" means "to shorten by cutting off the top or end".

### Exercise 3 (35 min)
In the third_part folder, start a new scrapy project and build a spider that crawls the webpage below,
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
