from app.users import get_user


def profile(uid):
    name = get_user(uid)
    return f"<h1>{name}</h1>" if name else "<h1>not found</h1>"
