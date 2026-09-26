# ShopKart API

![tests](https://github.com/iam-Jam24/shopkart-api/actions/workflows/tests.yml/badge.svg)

Backend for ShopKart, a small online store: cart totals, GST invoices, user signup, orders and product search.

## Modules

| File | What it does |
| --- | --- |
| `cart.py` | Cart total with a percentage discount |
| `invoice.py` | Invoice total with 18% GST |
| `users.py` | Email validation, user creation, display names |
| `orders.py` | Allowed order status transitions |
| `products.py` | Case-insensitive product search |

## Running the tests

```
pip install -r requirements-dev.txt
python -m pytest -v
```

Tests also run on every push and pull request through GitHub Actions.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
