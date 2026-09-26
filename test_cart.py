from cart import cart_total


def test_total_without_discount():
    assert cart_total([(100, 2), (50, 1)]) == 250
