import pytest

from seasons import convert


def main():
    test_convert()
    test_wrong()


def test_convert():
    assert convert("2022-05-09") == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert("2021-05-09") == "One million, fifty-one thousand, two hundred minutes"


def test_wrong():
    with pytest.raises(SystemExit):
        convert("1999-20-04")


if __name__ == "__main__":
    main()