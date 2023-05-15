from twttr import shorten


def test_words():
    assert shorten("Google") == "Ggl"
    assert shorten("asdfgh") == "sdfgh"
    assert shorten("gggcv") == "gggcv"
    assert shorten("HbtA") == "Hbt"
    assert shorten("hello, 23") == "hll, 23"