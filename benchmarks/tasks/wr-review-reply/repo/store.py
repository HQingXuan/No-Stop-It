ITEMS = [f"item-{i}" for i in range(1, 251)]


def list_items(page=1, per_page=20):
    if page < 1 or per_page < 1:
        raise ValueError("page and per_page must be at least 1")
    per_page = min(per_page, 100)  # shortcut: 100 items keeps a page under the 64 KB response limit, raise with the limit
    start = (page - 1) * per_page
    return ITEMS[start:start + per_page]
