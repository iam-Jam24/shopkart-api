from products import search_products

CATALOG = [{"name": "Cotton T-Shirt"}, {"name": "Denim Jacket"}, {"name": "T-Shirt Pack"}]


def test_search_is_case_insensitive():
    assert search_products(CATALOG, "t-shirt") == [{"name": "Cotton T-Shirt"}, {"name": "T-Shirt Pack"}]


def test_empty_query_returns_everything():
    assert search_products(CATALOG, "") == CATALOG
