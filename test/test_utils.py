"""Test util"""
from app.lib.utils import (
    get_index_of_square,
    reverse_index_to_square,
    get_square_coordinates
)

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

def test_get_square_coordinates():
    """Test get_square_coordinates"""
    assert(get_square_coordinates('a1', 100)) ==  (0, 700)
    assert(get_square_coordinates('a2', 100)) ==  (0, 600)
    assert(get_square_coordinates('a8', 100)) ==  (0, 0)
    assert(get_square_coordinates('b1', 100)) ==  (100, 700)
    assert(get_square_coordinates('b2', 100)) ==  (100, 600)
    assert(get_square_coordinates('e5', 100)) ==  (400, 300)
    assert(get_square_coordinates('h8', 100)) ==  (700, 0)
