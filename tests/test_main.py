import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..')
    )
)

from main import saudacao

def test_saudacao():
    assert saudacao("Ruan") == "Olá, Ruan"

def test_tipo():
    assert isinstance(saudacao("Ruan"), str)