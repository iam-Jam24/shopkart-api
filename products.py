def search_products(products, query):
    """Return products whose name contains the query, case-insensitive.

    products: list of dicts with a "name" key.
    An empty query returns all products.
    """
    q = query.strip().lower()
    return [p for p in products if q in p["name"].lower()]
