
PRODUCTS = ["Apple Watch", "Banana", "Pineapple Juice"]

def search_products(query):
    return [p for p in PRODUCTS if query in p]
