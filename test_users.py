from users import create_user, is_valid_email


def test_valid_email():
    assert is_valid_email("user@example.com") is True


def test_create_user():
    assert create_user("Asha", "asha@example.com")["name"] == "Asha"
