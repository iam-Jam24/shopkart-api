VALID_TRANSITIONS = {
    "pending": {"paid", "cancelled"},
    "paid": {"shipped", "refunded"},
    "shipped": {"delivered"},
    "delivered": set(),
    "cancelled": set(),
    "refunded": set(),
}


def next_status(current, new):
    """Return the new order status if the transition is allowed, otherwise raise ValueError."""
    if new not in VALID_TRANSITIONS.get(current, set()):
        raise ValueError(f"Cannot move order from {current} to {new}")
    return new
