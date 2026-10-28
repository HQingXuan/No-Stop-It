from app.users import get_usr


def profile(uid):
    name = get_usr(uid)
    return f"<h1>{name}</h1>" if name else "<h1>not found</h1>"
