from datetime import date
from enum import StrEnum

SOON_THRESHOLD_DAYS = 3


class Urgency(StrEnum):
    EXPIRED = "expired"
    SOON = "soon"
    OK = "ok"


def get_urgency(expiry_date: date, today: date) -> Urgency:
    """Return how urgent an item is, based on its expiry date.

    - EXPIRED: the expiry date is before today.
    - SOON: the item expires today or within SOON_THRESHOLD_DAYS days.
    - OK: the item expires later than that.

    `today` is passed in instead of calling date.today() inside the function,
    so the result depends only on the inputs. This makes the function
    predictable and easy to test.
    """
    days_left = (expiry_date - today).days
    if days_left < 0:
        return Urgency.EXPIRED
    elif days_left <= SOON_THRESHOLD_DAYS:
        return Urgency.SOON
    else:
        return Urgency.OK
