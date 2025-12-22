from numb3rs import validate

def test_word():
    assert validate("cat") == False
    assert validate("cat.cat.cat.cat") == False
    assert validate("hello.world.foo.bar") == False

def test_num():
    assert validate("1234") == False
    assert validate("-1.-2.-3.-4") == False
    assert validate("256.256.256.256") == False

def test_valid():
    assert validate("1.2.3.4") == True
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("140.247.235.144") == True

def test_out_of_range():
    assert validate("256.255.255.255") == False
    assert validate("255.256.255.255") == False
    assert validate("255.255.256.255") == False
    assert validate("255.255.255.256") == False
    assert validate("64.128.256.512") == False
    assert validate("512.512.512.512") == False
    assert validate("999.999.999.999") == False

def test_first_byte_only():
    assert validate("1.999.999.999") == False
    assert validate("200.300.1.1") == False
    assert validate("1.2.3.256") == False
    assert validate("255.255.255.300") == False

def test_wrong_format():
    assert validate("8.8.8") == False  # Only 3 octets
    assert validate("10.10.10.10.10") == False  # 5 octets
    assert validate("1.2.3.4.5.6") == False  # 6 octets
    assert validate("1.2") == False  # Only 2 octets
    assert validate("....") == False  # Only dots
    assert validate("1..2.3") == False  # Empty octet

