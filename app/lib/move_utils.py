"""Move validation """
from app.lib.utils import reverse_index_to_square


def can_bishop_moves(positions, start_index, end_index):
    """Validate bishop move from 2 index positions"""

    # print("***********bitshop check", start_index, end_index, end_index - start_index)
    # start_square = reverse_index_to_square(start_index)
    # end_square = reverse_index_to_square(end_index)
    diff = end_index - start_index
    if diff % 7!= 0 and diff %9 !=0:
        # print('invalid bitshop move')
        return False

    steps = 9

    if (end_index - start_index) % 7==0:
        steps = 7
    check_index = start_index
    if start_index < end_index:

        while check_index< end_index:
            check_index = check_index + steps
            if positions[check_index] != '' and check_index< end_index:
                return False

    if start_index > end_index:
        while check_index > end_index:
            check_index = check_index - steps
            if positions[check_index] != '' and check_index > end_index:
                return False

    return True

def can_root_moves(positions, start_index, end_index):
    """Validate if root can move
        Check if the rook can move between 2 squares
    """
    start_square = reverse_index_to_square(start_index)
    end_square = reverse_index_to_square(end_index)
    can_move = True
    # print('checking rook move ', start_square, start_index, end_square, end_index)

    ## Not on the same row or column , root will not able to move
    if start_square[0] != end_square[0] and start_square[1] != end_square[1]:
        return False
    # same column a7 to c7 for example
    if start_square[0] == end_square[0]:
        # print('check the same column')

        # 1 steps move
        if abs(start_index - end_index) <= 8:
            return True

        if start_index <  end_index:
            for check_index in range(start_index+8 , end_index-8, 8):
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False

        if start_index >  end_index:
            for check_index in range(start_index-8 , end_index+ 8, 8):
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False



    if start_square[1] == end_square[1]:
        # print('check the same row', start_index - end_index)
        if abs(start_index - end_index) <= 1:
            return True

        if start_index <  end_index:
            for check_index in range(start_index+1 , end_index, 1):
                # print("index loop", check_index, reverse_index_to_square(check_index))
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False

        if start_index >  end_index:
            for check_index in range(start_index-1 , end_index, 1):
                # print("index loop1", check_index, reverse_index_to_square(check_index))
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False

    print('Root move ok ', start_square, start_index, end_square, end_index)
    return can_move

def can_queen_moves(positions, start_index, end_index):
    """Validate if queen can move"""
    move_like_rook = can_root_moves(positions, start_index, end_index)
    if move_like_rook:
        return True

    move_as_bishop = can_bishop_moves(positions, start_index, end_index)
    if move_as_bishop:
        return True

    return False

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
