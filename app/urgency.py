from datetime import date
from enum import StrEnum

SOON_THRESHOLD_DAYS = 3


class Urgency(StrEnum):
    EXPIRED = "expired"
    SOON = "soon"
    OK = "ok"
