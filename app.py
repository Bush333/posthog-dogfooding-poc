
PRODUCTS = ["Apple Watch", "Banana", "Pineapple Juice"]

def search_products(query):
    query = query.casefold()
    return [p for p in PRODUCTS if query in p.casefold()]
