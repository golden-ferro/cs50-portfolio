import seasons


def test_value_in_words():
    assert seasons.value_in_words(1440) == "One thousand, four hundred forty minutes"
    assert seasons.value_in_words(1).endswith("One minutes")

def test_date_input_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "2004-07-22")
    assert seasons.date_input() == "2004-07-22"
