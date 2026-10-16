from datetime import date

from app.urgency import Urgency, get_urgency

TODAY = date(2026, 10, 16)


def test_expired_yesterday_is_expired():
    assert get_urgency(date(2026, 10, 15), TODAY) == Urgency.EXPIRED


def test_expires_today_is_soon():
    assert get_urgency(date(2026, 10, 16), TODAY) == Urgency.SOON


def test_expires_in_3_days_is_soon():
    assert get_urgency(date(2026, 10, 19), TODAY) == Urgency.SOON


def test_expires_in_4_days_is_ok():
    assert get_urgency(date(2026, 10, 20), TODAY) == Urgency.OK
