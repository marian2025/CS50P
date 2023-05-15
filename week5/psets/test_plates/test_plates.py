from plates import is_valid


#“All vanity plates must start with at least two letters.”
def test_start_letters():
    assert is_valid("CS50") == True
    assert is_valid("AB") == True
    assert is_valid("22") == False
    assert is_valid("1") == False


#“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def test_length():
    assert is_valid("QWDS42") == True
    assert is_valid("ABC") == True
    assert is_valid("C") == False
    assert is_valid("AS1234567") == False


#“Numbers cannot be used in the middle of a plate; they must come at the end.
#For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.”
def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False


#“No periods, spaces, or punctuation marks are allowed.”
def test_marks():
    assert is_valid("CS.42 ") == False
    assert is_valid(" CS 50") == False