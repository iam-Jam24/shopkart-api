GST_RATE = 0.18


def invoice_total(subtotal):
    """Return the subtotal plus 18% GST, rounded to the nearest paisa."""
    tax = int(subtotal * GST_RATE * 100) / 100
    return round(subtotal + tax, 2)
