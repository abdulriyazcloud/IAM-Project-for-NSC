
def validate_username(username):
    if not username:
        return False

    if len(username) < 3:
        return False

    return True
