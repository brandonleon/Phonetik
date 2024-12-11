import sys
import os
from icecream import ic

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from phonetik import get_phonetic_representation


def test_alpha():
    assert get_phonetic_representation("A").plain == "Alpha"

def test_number():
    assert get_phonetic_representation("1").plain == "One"

def test_symbol():
    assert get_phonetic_representation("@").plain == "At"
