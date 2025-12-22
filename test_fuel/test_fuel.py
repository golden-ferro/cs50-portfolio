import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("1/4") == 25
    assert convert("3/4") == 75

def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("2/1")

def test_gauge_E():
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_gauge_percentage():
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"

def test_convert_negative():
    with pytest.raises(ValueError):
        convert("-1/2")  
    with pytest.raises(ValueError):
        convert("1/-2")
    with pytest.raises(ValueError):
        convert("-1/-2")
