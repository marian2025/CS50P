import pytest

from working import convert


def main():
    test_wrong_format()
    test_wrong_hour()
    test_wrong_minute()
    test_time()


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("10 AM - 4 PM")


def test_wrong_hour():
    with pytest.raises(ValueError):
        convert("15 PM to 20 PM")


def test_wrong_minute():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_time():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"


if __name__ == "__main__":
    main()