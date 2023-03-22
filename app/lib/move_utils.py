"""Move validation """
from app.lib.utils import reverse_index_to_square, get_index_of_square

def range_of(start, end, exclude_boundary=False):
    """Create range of character from 2 char"""
    start_i = min(ord(start),  ord(end))
    end_i = max(ord(end), ord(start))
    result= [chr(i) for i in range(start_i, end_i +1)]

    if exclude_boundary:
        return [x for x in result if x not in [start, end]]
    return result

def get_square_between(start_square, end_square, exclude_boundary=True):
    """Find all the square between 2 square for a2 and a7 or b8  c8"""
    start_col = start_square[0]
    start_row = int(start_square[1])
    end_col= end_square[0]
    end_row = int(end_square[1])
    # sample row
    if start_row == end_row:
        cols = range_of(start_col, end_col, exclude_boundary)
        return [x + str(end_row) for x in cols]

    #sample column
    if start_col == end_col:
        rows = range_of(str(start_row), str(end_row), exclude_boundary)
        return [start_col +x for x in rows]

    # check diagnal
    return None

def get_diagonal_square_between(start_square, end_square):
    """Get diagonal square between 2 square"""
    start_index = get_index_of_square(start_square)
    end_index = get_index_of_square(end_square)
    diff_row = abs(ord(start_square[0]) - ord(end_square[0]))
    diff_col = abs(ord(start_square[1]) - ord(end_square[1]))

    if diff_col != diff_row:
        return None

    # print(start_square, end_square, start_index, end_index)

    diff = end_index - start_index
    dianonal_squares = []
    # print(diff, diff % 7 != 0, diff % 9 != 0)
    if diff % 7 != 0 and diff %9 != 0:
        return None

    steps = 7

    if diff % 9 == 0:
        steps = 9

    check_index = start_index

    if start_index < end_index:
        while check_index <  end_index:
            check_index = check_index + steps
            dianonal_squares.append(reverse_index_to_square(check_index))

    else:
        while check_index > end_index:
            check_index = check_index - steps
            dianonal_squares.append(reverse_index_to_square(check_index))

    return [x for x in dianonal_squares if x not in [start_square, end_square]]

def check_move_in_straight_lines(possitions, start_square, end_square):
    """Check if the piece can move between 2 squares without any blockade"""
    squares = get_square_between(start_square, end_square)

    #  if 2 cell is not connected on the straight lines, return FALSE
    if squares is None:
        return False
    print('_______________ >square_between', start_square, end_square, squares)
    blocked_square = [x for x in squares if possitions[get_index_of_square(x)] != '' ]
    return len(blocked_square) == 0

def check_move_in_diagonal_lines(possitions, start_square, end_square):
    """Check if the piece can move between 2 squares without any blockade"""
    squares = get_diagonal_square_between(start_square, end_square)

    #  if 2 cell is not connected on the straight lines, return FALSE
    if squares is None:
        return False
    print('_______________ >diagonal line ', start_square, end_square, squares)
    blocked_square = [x for x in squares if possitions[get_index_of_square(x)] != '' ]
    return len(blocked_square) == 0

def can_bishop_moves(positions, start_index, end_index):
    """Validate bishop move from 2 index positions"""

    start_square = reverse_index_to_square(start_index)
    end_square = reverse_index_to_square(end_index)

    return check_move_in_diagonal_lines(positions, start_square, end_square)

def can_root_moves(positions, start_index, end_index):
    """Validate if root can move
        Check if the rook can move between 2 squares
    """
    start_square = reverse_index_to_square(start_index)
    end_square = reverse_index_to_square(end_index)

    return check_move_in_straight_lines(positions, start_square, end_square)


def can_queen_moves(positions, start_index, end_index):
    """Validate if queen can move"""

    start_square = reverse_index_to_square(start_index)
    end_square = reverse_index_to_square(end_index)

    return (
        check_move_in_diagonal_lines(positions, start_square, end_square)
        or check_move_in_straight_lines(positions, start_square, end_square)
    )

def can_knight_move( start_index, end_index,):
    """Validate if knight can move"""
    start_square = reverse_index_to_square(start_index)
    end_square = reverse_index_to_square(end_index)

    diff_row = abs(ord(start_square[0]) - ord(end_square[0]))

    diff_col = abs(int(start_square[1]) - int(end_square[1]))

    # print('************ **** knight move check', start_square, end_square, diff_row, diff_col)
    if diff_row ==1 and diff_col ==2:
        return True

    if diff_row ==2 and diff_col ==1:
        return True

    # check move like Bishop
    return False
