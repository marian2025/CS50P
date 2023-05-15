import pytest

from numb3rs import validate


def main():
    test_first_byte()
    test_five_byte()
    test_str()


def test_first_byte():
    assert validate("127.700.200.1") == False


def test_five_byte():
    assert validate("125.2.2.2.2") == False


def test_str():
    assert validate("cat") == False


if __name__ == "__main__":
    main()