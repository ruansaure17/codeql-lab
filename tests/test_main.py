from main import saudacao


def test_saudacao():
    assert saudacao("Ruan") == "Olá, Ruan"


def test_tipo():
    assert isinstance(saudacao("Ruan"), str)
