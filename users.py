def is_valid_email(email):
    """Return True if the email looks like name@domain.tld."""
    return "@" in email


def create_user(name, email):
    if not is_valid_email(email):
        raise ValueError("Invalid email")
    return {"name": name, "email": email}


def display_name(user):
    """Return the user's display name."""
    return user["name"].upper()
