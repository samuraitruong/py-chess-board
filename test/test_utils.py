"""Test util"""
from app.lib.utils import get_index_of_square, reverse_index_to_square

def test_get_index_of_square():
    """Test get_index_of_square"""
    assert(get_index_of_square("a1")) == 0
    assert(get_index_of_square("a8")) == 56
    assert(get_index_of_square("a2")) == 8
    assert(get_index_of_square("b8")) == 57
    assert(get_index_of_square("h8")) ==  63
    assert(get_index_of_square("e4")) ==  28
    assert(get_index_of_square("d5")) ==  35

def test_reverse_index_to_square():
    """test reverse index"""
    assert(reverse_index_to_square(35)) ==  "d5"
    assert(reverse_index_to_square(63)) ==  "h8"
    assert(reverse_index_to_square(8)) ==  "a2"
