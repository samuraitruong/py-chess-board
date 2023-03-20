from app.lib.utils import reverse_index_to_square


def can_root_moves(positions, start_index, end_index):
    """Check if the rook can move between 2 squares"""
    start_square = reverse_index_to_square(start_index)
    end_square = reverse_index_to_square(end_index)
    can_move = True
    print('checking rook move ', start_square, start_index, end_square, end_index)

    ## Not on the same row or column , root will not able to move
    if start_square[0] != end_square[0] and start_square[1] != end_square[1]:
        return False
    # same column a7 to c7 for example
    if start_square[0] == end_square[0]:
        print('check the same column')

        # 1 steps move
        if abs(start_index - end_index) <= 8:
            return True

        if(start_index <  end_index):
            for check_index in range(start_index+8 , end_index-8, 8):
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False

        if(start_index >  end_index):
            for check_index in range(start_index-8 , end_index+ 8, 8):
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False



    if start_square[1] == end_square[1]:
        print('check the same row', start_index - end_index)
        if abs(start_index - end_index) <= 1:
            return True

        if(start_index <  end_index):
            for check_index in range(start_index+1 , end_index, 1):
                print("index loop", check_index, reverse_index_to_square(check_index))
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False

        if(start_index >  end_index):
            for check_index in range(start_index-1 , end_index, 1):
                print("index loop1", check_index, reverse_index_to_square(check_index))
                # If any piece between start and end , the move is blocked
                if positions[check_index] != '':
                    return False

    print('Root move ok ', start_square, start_index, end_square, end_index)
    return can_move

def can_queen_moves(positions, start_index, end_index):
    move_like_rook = can_root_moves(positions, start_index, end_index)
    if move_like_rook:
        return True

    # TODO check move like Bishop
    return True
