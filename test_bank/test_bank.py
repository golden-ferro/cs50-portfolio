from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0
    assert value("   hello   ") == 0  

def test_h():
    assert value("h") == 20
    assert value("hi") == 20
    assert value("Hey") == 20

def test_other():
    assert value("abc") == 100
    assert value("good morning") == 100
    assert value("123hello") == 100



