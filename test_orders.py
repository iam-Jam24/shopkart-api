import pytest

from orders import next_status


def test_pending_order_can_be_paid():
    assert next_status("pending", "paid") == "paid"


def test_delivered_order_cannot_go_back_to_pending():
    with pytest.raises(ValueError):
        next_status("delivered", "pending")


def test_unknown_status_is_rejected():
    with pytest.raises(ValueError):
        next_status("lost", "paid")
