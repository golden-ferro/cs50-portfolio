from working import convert
import pytest

def test_with_minutes():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12:30 PM to 1:45 PM") == "12:30 to 13:45"

def test_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("12 PM to 1 PM") == "12:00 to 13:00"

def test_mixed_format():
    assert convert("9:15 AM to 5 PM") == "09:15 to 17:00"
    assert convert("9 AM to 5:45 PM") == "09:00 to 17:45"

def test_valid_times():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"

def test_invalid_hour_start():
    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

def test_invalid_hour_end():
    with pytest.raises(ValueError):
        convert("9:00 AM to 15:00 PM")

def test_invalid_minute_start():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5:00 PM")

def test_invalid_minute_end():
    with pytest.raises(ValueError):
        convert("9:00 AM to 7:61 PM")

def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")
