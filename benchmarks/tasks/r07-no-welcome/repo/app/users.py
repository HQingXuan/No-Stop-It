USERS = {}


def create(email, name):
    uid = len(USERS) + 1
    USERS[uid] = {"email": email, "name": name}
    return uid
