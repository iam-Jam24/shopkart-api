from invoice import invoice_total


def test_invoice_round_number():
    assert invoice_total(100) == 118.0
