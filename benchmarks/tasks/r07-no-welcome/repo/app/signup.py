import logging

from app import users

log = logging.getLogger(__name__)


def signup(email, name):
    if "@" not in email:
        raise ValueError("bad email")
    uid = users.create(email, name)
    log.info("signed up %s as %s", email, uid)
    return uid
