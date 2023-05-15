from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("hi") == 20
    assert value("hey") == 20
    assert value("Hey") == 20

def test_non_h():
    assert value("Good morning") == 100
    assert value("What's up") == 100