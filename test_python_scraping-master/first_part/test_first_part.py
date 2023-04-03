#part1
def exercise_one():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("ThreeFive")
        elif num % 3 == 0:
            print("Three")
        elif num % 5 == 0:
            print("Five")
        else:
            print(num)


def is_colorful(num):
    digits = [int(d) for d in str(num)]  # Convert the number to a list of digits
    products = set()  # Keep track of all the products we've seen so far
    for i in range(len(digits)):
        for j in range(i, len(digits)):
            product = 1
            for k in range(i, j+1):
                product *= digits[k]  # Compute the product of the current subset of digits
            if product in products:
                return False  # If we've already seen this product, the number is not colorful
            products.add(product)  # Add the product to our set of seen products
    return True  # If we make it through all the subsets without finding a repeated product, the number is colorful


def calculate(lst):
    total = 0
    if not isinstance(lst, list):
        return False
    for item in lst:
        if isinstance(item, str):
            try:
                total += int(item)
            except ValueError:
                pass
        
    if total == 0:
        return False
    else:
        return total
def find_anagrams(word, lst):
    anagrams = []
    sorted_word = sorted(word.lower())
    for item in lst:
        sorted_item = sorted(item.lower())
        if sorted_item == sorted_word and item.lower() != word.lower():
            anagrams.append(item)
    return anagrams


#part2
def random_gen():
    while True:
        num = random.randint(10, 20)
        if num == 15:
            return
        yield num

def decorator_to_str(func):
    def func(*args, **kwargs):
        result = func(*args, **kwargs)
        return str(result)
    return func


@decorator_to_str
def add(a, b):
    return a + b


@decorator_to_str
def get_info(d):
    return d['info']

def ignore_exception(exception):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception:
                return None
        return wrapper
    return decorator


@ignore_exception(ZeroDivisionError)
def div(a, b):
    return a / b


@ignore_exception(TypeError)
def raise_something(exception):
    raise exception


# exercise 4

class CacheDecorator:
    """Saves the results of a function according to its parameters"""
    def __init__(self):
        self.cache = {}

    def __call__(self, func):
        def _wrap(*a, **kw):
            if a[0] not in self.cache:
                self.cache[a[0]] = func(*a, **kw)
            return self.cache[a[0]]

        return _wrap
def test_cache_decorator():
    # Create a new CacheDecorator object
    cache_decorator = CacheDecorator()

    # Define a test function that will be cached
    @cache_decorator
    def test_function(n):
        return n ** 2

    # Test the cached function with different input values
    assert test_function(5) == 25
    assert test_function(2) == 4
    assert test_function(7) == 49

    # Test that the function is actually being cached
    assert cache_decorator.cache == {5: 25, 2: 4, 7: 49}

    # Redefine the test function with a new implementation
    @cache_decorator
    def test_function(n):
        return n ** 3

    # Test that the new implementation is being used
    assert test_function(5) == 125
    assert test_function(2) == 8
    assert test_function(7) == 343

    # Test that the cache is still being used
    assert cache_decorator.cache == {5: 125, 2: 8, 7: 343}

    # Test the behavior when calling the function with the same input value twice
    assert test_function(5) == 125
    assert cache_decorator.cache == {5: 125, 2: 8, 7: 343}

    # Test the behavior when calling the function with a new input value
    assert test_function(3) == 27
    assert cache_decorator.cache == {5: 125, 2: 8, 7: 343, 3: 27}


class MetaInherList(type):
    def __new__(cls, clsname, bases, attrs):
        attrs['__bases__'] = (list,) + bases
        return super().__new__(cls, clsname, bases, attrs)


class Ex:
    x = 4


class ForceToList(Ex, metaclass=MetaInherList):
    pass

#exercice6
class ProcessChecker(type):
    def __init__(cls, name, bases, attrs):
        if 'process' in attrs:
            process_method = attrs['process']
            if not callable(process_method) or len(process_method.__code__.co_varnames) != 3:
                raise TypeError(f"{name}.process must be a method that takes 3 arguments")
        super().__init__(name, bases, attrs)


#part3
#exercice 1 
import requests

def http_request():
    # define the request parameters
    params = {
        'isadmin': 1
    }
    url = 'https://httpbin.org/anything'
    headers = {
        'User-Agent': 'My User Agent'
    }
    
    # send the POST request with parameters and headers
    response = requests.post(url, data=params, headers=headers)
    
    # return the response body
    return response.text
#To send the same request with a different user-agent, we can simply modify the headers dictionary to include the desired user-agent string

def http_request():
    params = {
        'isadmin': 1
    }
    url = 'https://httpbin.org/anything'
    headers = {
        'User-Agent': 'My New User Agent'
    }
    response = requests.post(url, data=params, headers=headers) 
    return response.text



















