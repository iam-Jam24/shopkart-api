def cart_total(items, discount_percent=0):
    """Return the cart total after a percentage discount.

    items: list of (price, quantity) tuples.
    discount_percent: e.g. 10 means 10% off.
    """
    subtotal = sum(price * qty for price, qty in items)
    discount = subtotal * discount_percent
    return round(subtotal - discount, 2)
