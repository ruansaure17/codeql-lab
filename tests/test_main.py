from main import saudacao

def test_saudacao():
    assert saudacao("Saure") == "Olá, Saure"

def test_tipo():
    assert isinstance(saudacao("Saure"), str)