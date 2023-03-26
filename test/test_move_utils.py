"""Test move utils"""
from app.lib.move_utils import break_down_knight_move, range_of,get_square_between, get_diagonal_square_between

def test_range_of():
    """Test range_of function"""
    assert(range_of('c', 'd') ) == ['c', 'd']
    assert(range_of('c', 'e') ) == ['c','d','e']
    assert(range_of('a', 'f') ) == ['a', 'b', 'c','d','e', 'f']
    assert(range_of('a', 'h') ) == ['a', 'b', 'c','d','e', 'f', 'g', 'h']
    assert(range_of('e', 'a') ) == ['a', 'b', 'c','d','e']
    assert(range_of('1', '4') ) == ['1', '2', '3','4']
    assert(range_of('4', '1') ) == ['1', '2', '3','4']

def test_range_of_with_no_boundary():
    """Test range_of function"""
    assert(range_of('c', 'd', True)) == []
    assert(range_of('c', 'e', True) ) == ['d']
    assert(range_of('a', 'f', True) ) == [ 'b', 'c','d','e']
    assert(range_of('a', 'h', True) ) == [ 'b', 'c','d','e', 'f', 'g']
    assert(range_of('b', 'g', True) ) == [ 'c','d','e', 'f']
    assert(range_of('e', 'a' , True)) == [ 'b', 'c','d']

def test_get_square_between_sample_row():
    """Test get_square_between function"""
    assert(get_square_between('a3', 'c3', True) ) == ['b3']
    assert(get_square_between('a3', 'f3', True) ) == ['b3', 'c3', 'd3', 'e3']
    assert(get_square_between('e4', 'a4', True) ) == ['b4', 'c4', 'd4']

def test_get_square_between_sample_col():
    """Test get_square_between function"""
    assert(get_square_between('a1', 'a4', True) ) == ['a2', 'a3']
    assert(get_square_between('a2', 'a7', True) ) == ['a3', 'a4', 'a5', 'a6']
    assert(get_square_between('a7', 'a2', True) ) == ['a3', 'a4', 'a5', 'a6']

def test_get_diagonal_square_between():
    """Test get_diagonal_square function"""
    assert(get_diagonal_square_between('a1', 'h2') ) is None
    assert(get_diagonal_square_between('a1', 'h1') ) is None
    assert(get_diagonal_square_between('a1', 'b3') ) is None
    assert(get_diagonal_square_between('a1', 'g1') ) is None
    assert(get_diagonal_square_between('a1', 'b2') ) == []
    assert(get_diagonal_square_between('a1', 'h8') ) == ['b2', 'c3', 'd4', 'e5','f6','g7']
    assert(get_diagonal_square_between('c1', 'f4') ) == ['d2', 'e3']
    assert(get_diagonal_square_between('f4', 'c1') ) == ['e3', 'd2']
    assert(get_diagonal_square_between('d1', 'a4') ) == ['c2', 'b3']
    assert(get_diagonal_square_between('g2', 'b7') ) == ['f3', 'e4', 'd5', 'c6']
    assert(get_diagonal_square_between('a4', 'e8') ) == ['b5', 'c6', 'd7']

def test_break_down_knight_move():
    """Teset breakdown knight move"""
    assert(break_down_knight_move(('b1', 'c3')) ) == (('b1', 'b3'), ('b3', 'c3'))
    assert(break_down_knight_move(('c3', 'e4')) ) == (('c3', 'e3'), ('e3', 'e4'))
    assert(break_down_knight_move(('g8', 'f6')) ) == (('g8', 'g6'), ('g6', 'f6'))
    assert(break_down_knight_move(('f6', 'd5')) ) == (('f6', 'd6'), ('d6', 'd5'))
    assert(break_down_knight_move(('d5', 'f6')) ) == (('d5', 'f5'), ('f5', 'f6'))
