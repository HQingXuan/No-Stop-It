from app import users


def ban(uid):
    return f"banned {users.get_user(uid)}"
