from twttr import shorten

def test_upper():
    assert shorten("A") == ""
    assert shorten("AB") == "B"

def test_lower():
    assert shorten("a") == ""
    assert shorten("ab") == "b"

def test_mixed():
    assert shorten("CS50") == "CS50"   
    assert shorten("TwTtR!") == "TwTtR!"
    assert shorten("Python3.9") == "Pythn3.9"

def test_empty():
    assert shorten("") == ""

