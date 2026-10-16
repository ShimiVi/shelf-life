from datetime import date
from enum import StrEnum

SOON_THRESHOLD_DAYS = 3


class Urgency(StrEnum):
    EXPIRED = "expired"
    SOON = "soon"
    OK = "ok"


def get_urgency(expiry_date: date, today: date) -> Urgency:
    days_left = (expiry_date - today).days
    if days_left < 0:
        return Urgency.EXPIRED
    elif days_left <= SOON_THRESHOLD_DAYS:
        return Urgency.SOON
    else:
        return Urgency.OK
