from plates import is_valid

def test_first_char_letter():
    assert is_valid("1ABC") == False
    assert is_valid("9CS50") == False
    assert is_valid("C") == False

def test_second_char_letter():
    assert is_valid("A1BC") == False
    assert is_valid("Z2") == False
    assert is_valid("B9XYZ") == False

def test_length():
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False

def test_numbers_position():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS5A") == False
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False

def test_no_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("CS-50") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS50!") == False

