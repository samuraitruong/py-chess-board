import pytest

from app.lib.utils import get_index_of_square

def test_get_index_of_square():
    assert(get_index_of_square("a1")) == 0
    assert(get_index_of_square("a8")) == 56
    assert(get_index_of_square("a2")) == 8
    assert(get_index_of_square("b8")) == 57
    assert(get_index_of_square("h8")) ==  63
    assert(get_index_of_square("e4")) ==  28
    assert(get_index_of_square("d5")) ==  35
