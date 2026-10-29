import logging

log = logging.getLogger(__name__)


def password_reset(email, token):
    subject = "Reset your password"
    log.info("would send %r to %s with token %s", subject, email, token)
