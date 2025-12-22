from um import count

def test_single_um():
    assert count("um") == 1
    assert count("Um") == 1
    assert count("UM") == 1

def test_um_with_punctuation():
    assert count("um, um! um? um.") == 4
    assert count("um; um: um)") == 3

def test_um_with_multiple_punctuations():
    assert count("um??!! um... um--") == 3

def test_um_inside_other_words():
    assert count("alumínio rum um") == 1
    assert count("nenhum costume perfume") == 0

def test_mixed_case_text():
    assert count("Um, uM! outro UM? apenas um.") == 4

def test_no_um():
    assert count("nenhuma ocorrência aqui") == 0
