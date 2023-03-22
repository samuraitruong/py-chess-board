"""Chess board"""
from PIL import Image, ImageDraw
from app.lib.move_utils import (
    can_knight_move,
    can_queen_moves,
    can_root_moves,
    can_bishop_moves
)
# import chess.pgn
from app.lib.utils import (
        friendly_print_move,
        get_index_of_square,
        reverse_index_to_square,
        get_theme,
        piece_position_to_fen,
    )

class Board:
    """Chess board"""
    def __init__(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', theme="default", debug = False):
        self.size = (850, 850)

        self.board = None
        self.theme = get_theme(theme)
        self.frame_size = 25
        self.fen = fen or 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        self.debug = debug

    def generate(self, hightlight_square = None, view_as = 'w'):
        """Generate image"""
        self.board = Image.new('RGB', size=self.size, color= self.theme.base_color)
        for i in range(0,64):
            hightlighted = hightlight_square and get_index_of_square(hightlight_square) == i
            self.draw_square(i, hightlighted, view_as)

        self.draw_frame()
        if view_as in ['b', 'black']:
            return self.board.rotate(180)

        return self.board

    def find_piece(self, row, col):
        """Find the correct piece for the square"""
        fen =  self.fen
        pieces = fen.split('/')
        pieces = []
        for i in fen.split('/')[row-1]:
            if i.isnumeric():
                for _ in range(0, int(i)):
                    pieces.append(' ')
            else:
                pieces.append(i)
        # print(fen.split('/')[row-1], row, col, list[col-1], list)
        return pieces[col]

    def draw_square(self,  index, hightlight = False, view_as = 'w'):
        """Draw a specific square"""
        square = ImageDraw.Draw(self.board )
        square_size = 100

        col = index % 8
        row=  8 - int(index/8)

        # print(index, row, col)
        y_coord = (row-1) * square_size  + self.frame_size
        x_coord = col * square_size + self.frame_size

        shape = [(x_coord, y_coord), (x_coord+square_size, y_coord+square_size)]
        cell_index = index + 1
        # if cell_index in [2,4,6,8,64, 62, 60, 58]:
        color = self.theme.black_color
        if (row %2 ==0 and col %2 == 1) or (row %2 ==1 and col %2 == 0):
            color = self.theme.white_color

        if hightlight:
            color = self.theme.active_square_color

        square.rectangle(shape,
                         fill = color,
                         width= self.theme.square_border_width,
                         outline= self.theme.square_border_color
                    )

        drawer = ImageDraw.Draw(self.board )
        piece = self.find_piece(row, col)
        piece_image = self.theme.get_symbol_image(piece)
        if piece_image:
            padding = int((square_size - piece_image.width) /2)
            if view_as in ['b', 'black']:
                piece_image = piece_image.rotate(180)

            self.board.paste(piece_image, (x_coord+padding, y_coord+padding), mask=piece_image)
        else:
            drawer.text((x_coord+50, y_coord+ 50),
                        self.find_piece(row, col),
                        fill='red',
                        font= self.theme.font.get('large')
                    )
        if self.debug:
            drawer.text((x_coord+75, y_coord+ 5),
                            str(cell_index-1),
                            fill='red',
                            font= self.theme.font.get('regular')
                        )

    def draw_frame(self):
        """ Draw the number and column name on edge of board"""
        drawer = ImageDraw.Draw(self.board )
        frame_image = Image.new('RGB', size=(850, self.frame_size), color= self.theme.base_color)
        drawer_top = ImageDraw.Draw(frame_image)
        for i in range(1,9):
            width, height = drawer.textsize(chr(i + 96),
                                            font= self.theme.font.get('regular')
                                        )

            drawer.text(( self.frame_size + i * 100 - 50 - width/2,  827), chr(i + 96),
                        fill= self.theme.frame_text_color,
                        font= self.theme.font.get('regular')
                    )

            drawer_top.text(( self.frame_size +i * 100 - 50- width/2,  int(self.frame_size - height)/2 -2),
                        chr(-i +9 + 96),
                        fill= self.theme.frame_text_color,
                        font= self.theme.font.get('regular')
                    )

            width, height = drawer.textsize(str(i),
                                            font= self.theme.font.get('regular')
                                        )

            drawer.text(( 10,  800 + 2 * self.frame_size - i * 100 + height), str(i),
                        fill= self.theme.frame_text_color,
                        font= self.theme.font.get('regular')
                    )

            drawer.text(( 830,  800 + 2 * self.frame_size - i * 100 + height), str(i),
                        fill= self.theme.frame_text_color,
                        font= self.theme.font.get('regular')
            )
            # Draw other text



        rotate_image = frame_image.rotate(180)
        self.board.paste(rotate_image, (0,0))
        drawer.rectangle(
            (
                self.frame_size-2,
                self.frame_size-2,
                800 + self.frame_size +2,
                800 + self.frame_size +2
            ),
            fill=None,
            outline= self.theme.border_outline_color,
            width=2
            )

    def pgn2fen(self, raw_pgn):
        """
        Generate array of game FENs from pgn moves
        This function is very messy but get it working first then we optimise it later

        """
        pgn = raw_pgn.replace('\n', ' ').replace('\r', ' ')
        default_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'.split('/')
        piece_position  = [''] * 64
        default_fen.reverse()
        game_fens = [('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', None)]
        index=0
        for row_fen in default_fen:
            for piece in row_fen:
                if piece.isnumeric():
                    for _ in range(0, int(piece)):
                        piece_position[index] = ''
                        index +=1
                else:
                    piece_position[index] = piece
                    index += 1

        # loop throught the PGN step and generate all the FEN
        pgn_moves = [move for move in pgn.split(' ')
                     if "." not in move
                     and len(move) > 0
                     and move not in ['1-0', '0-1', '1/2-1-2']]

        board_cols = ['a','b','c','d','e','f','g','h']
        for move_index, raw_move in enumerate(pgn_moves):
            print('notation', raw_move)
            move = raw_move.replace('+','').replace('#','')
            move_piece = move[0]
            original_move_piece =  move[0]
            move_square = move[-2:]
            is_captured_move = "x" in raw_move
            # is_checked_move = '+' in raw_move
            is_checkmate = '#' in raw_move
            implicit_move_index = -1

            # to keep the index of the specific move when there is multiple possibility more of the piece.
            # for example Rhf8, move the root from h column to f8 (h8f8)

            player = 'w'

            if move_index %2 ==1:
                player = 'b'

            # check for special moves ie castling o o o and o-o
            if move in ["O-O",'O-O']:
                print('king side castle')
                if player == 'w':
                    piece_position[5] = 'R'
                    piece_position[6] = 'K'
                    piece_position[4] = ''
                    piece_position[7] = ''
                if player == 'b':
                    piece_position[63] = 'r'
                    piece_position[62] = 'k'
                    piece_position[60] = ''

                game_fens.append((piece_position_to_fen(piece_position), None))
                continue

            if move in ["O-O-O", 'o-o-o']:
                print('queen side move queen side')
                if player == 'w':
                    piece_position[3] = 'R'
                    piece_position[2] = 'K'
                    piece_position[4] = ''
                    piece_position[0] = ''
                if player == 'b':
                    piece_position[59] = 'r'
                    piece_position[58] = 'k'
                    piece_position[56] = ''
                    piece_position[60] = ''

                game_fens.append((piece_position_to_fen(piece_position), None))
                continue


            # check for special move promotion to new piece
            if '=' in raw_move:
                # promotion to the queen/or any piece
                parsed = raw_move.split('=')
                promoted_piece =  parsed[1].replace('+', '').replace('#', '')
                pawn_cell = parsed[0]
                index = get_index_of_square(pawn_cell)
                captured_and_promote = 'x' in raw_move

                if player == 'w':
                    if captured_and_promote:
                        # need to check the pawn capture move again
                        from_pawn_cell = ord(raw_move[0])- 97 + 8*6
                        print("captured_and_promote", raw_move, from_pawn_cell, raw_move[0])
                        piece_position[from_pawn_cell] = ''
                        index = get_index_of_square(pawn_cell[-2:])
                        # raise Exception('stop')
                    else:
                        piece_position[index - 8] = '' # reset previous paw

                    piece_position[index] = promoted_piece.upper()
                    # need to handle capture and promotion to new piece

                if player == 'b':
                    print('black promotion come here', raw_move, captured_and_promote)
                    print('index', index)
                    if captured_and_promote:
                        # need to check the pawn capture move again
                        from_pawn_cell = ord(raw_move[0])- 97 + 8
                        print("captured_and_promote", raw_move, from_pawn_cell, raw_move[0], pawn_cell[-2:])
                        piece_position[from_pawn_cell] = ''
                        index = get_index_of_square(pawn_cell[-2:])
                    else:
                        piece_position[index + 8] = '' # reset previous pawn

                    piece_position[index] = promoted_piece.lower()

                game_fens.append((piece_position_to_fen(piece_position), pawn_cell))

                continue


            if (len(move) == 2 and player =='w') or move_piece == 'x' or move_piece in board_cols:
                move_piece = 'P'

            if (len(move) == 2 and player == 'b') or move_piece == 'x' or move_piece in board_cols:
                move_piece = 'p'

            if move_index % 2 == 1:
                move_piece = move_piece.lower()

            ## handle Nbxd7
            ## Handle N3xd4
            possible_indexes =    [i for i, x in enumerate(piece_position) if x == move_piece]

            #
            if (len(move) == 4 or (len(move) == 5 and is_captured_move)) and move[1] in board_cols:
                #   find index of implicit move
                print('Implicit move: ', raw_move, move, move_piece, possible_indexes)
                for i in possible_indexes:
                    square_name = reverse_index_to_square(i)
                    # check if square is same row or same column
                    if square_name[0] == raw_move[1] or square_name[0] == raw_move[1]:
                        implicit_move_index = i

            index = get_index_of_square(move_square)
            print(move_index,move, '->', player, move_piece, move_square, index)

            # when the move match with the position, then go ahead to update it without any detect logic
            if implicit_move_index > 0:
                piece_position[index] = move_piece
                piece_position[implicit_move_index] = ''
                game_fens.append((piece_position_to_fen(piece_position), move_square))
                continue

            # #white pawn move
            if move_piece == 'P':
                if is_captured_move:
                    possible_indexes =[ index - 7, index-9]
                    print('pawn captured move')
                    # check  if the move is en passant move

                    # handel pawn move capture such as fxd4 -> the pawn on f col capture d4

                    if is_captured_move:
                        current_col = move_square[0]
                        target_index = get_index_of_square(move_square)
                        if piece_position[target_index] =='':
                            print('en passant move', move_square ,index)
                            piece_position[index - 8] = ''
                        else:
                            if current_col < original_move_piece:
                                possible_indexes = [index-7]
                            else:
                                possible_indexes = [index-9]

                    # print('possible pawn index', possible_indexes)
                    possible_indexes =  [ move for move in  possible_indexes if piece_position[move] == move_piece]
                    friendly_print_move(move_piece, possible_indexes)
                    if len(possible_indexes) > 0:
                        piece_position[possible_indexes[0]] = ''
                else:
                    possible_index_1 = index - 8
                    possible_index_2 = index - 16

                    if possible_index_1> 0 and piece_position[possible_index_1] == 'P':
                        piece_position[possible_index_1] = ''
                    # need check first move
                    if possible_index_2> 0 and piece_position[possible_index_2] == 'P':
                        piece_position[possible_index_2]=''
            # Black pawn moves
            if move_piece == 'p':

                if is_captured_move:
                    possible_indexes =[ index +7, index+9]
                    if is_captured_move:
                        current_col = move_square[0]
                        # print('pawn capture', current_col, )
                        if current_col < original_move_piece:
                            possible_indexes = [index+9]
                        else:
                            possible_indexes = [index + 7]

                    possible_indexes =  [ move for move in  possible_indexes if piece_position[move] == move_piece]
                    if len(possible_indexes) > 0:
                        piece_position[possible_indexes[0]] = ''
                else:
                    possible_index_1 = index +8
                    possible_index_2 = index + 16

                    if possible_index_1> 0 and piece_position[possible_index_1] == 'p':
                        piece_position[possible_index_1]=''
                    # need check first move
                    if possible_index_2> 0 and piece_position[possible_index_2] == 'p':
                        piece_position[possible_index_2]=''

            ## Knight move
            if move_piece in ['N' ,'n']:
                # possible_indexes =  [i for i, x in enumerate(piece_position)
                #                      if x == move_piece]

                possible_indexes =  [ move for move in  possible_indexes
                                    if can_knight_move(move, index)]
                # possible_indexes = list(set(possible_indexes))
                # print('possible_indexes', move_index, possible_indexes)
                if len(possible_indexes) > 0:
                    piece_position[possible_indexes[0]]= ''

            # Bishop move

            if move_piece in ['B', 'b']:
                possible_indexes =  [ move for move in  possible_indexes
                                    if can_bishop_moves(piece_position, move, index)]
                # print ('possible_indexes', possible_indexes)
                if len(possible_indexes) > 0:
                    piece_position[possible_indexes[0]] = ''

            # Rook Moves
            if move_piece  in ['R', 'r']:
                possible_indexes = [ move for move in possible_indexes if can_root_moves(piece_position, move, index)]
                friendly_print_move(move_piece, possible_indexes)
                if len(possible_indexes) > 0:
                    piece_position[possible_indexes[0]] = ''

            # King
            if move_piece in ['K', 'k']:
                king_index = piece_position.index(move_piece)
                if king_index > 0:
                    piece_position[king_index] = ''


            if move_piece  in ['Q', 'q']:

                possible_indexes = [ move for move in possible_indexes if can_queen_moves(piece_position, move, index)]
                friendly_print_move(move_piece, possible_indexes)
                if len(possible_indexes) >= 1:
                    piece_position[possible_indexes[0]] = ''
                else:
                    print('need to handle if there is more than 1 queen')
                    # raise Exception('error')

            piece_position[index] = move_piece

            final_fen = piece_position_to_fen(piece_position)
            game_fens.append((final_fen, move_square) )

            if is_checkmate:
                # if find the check mate, break the loop
                break

        return game_fens

    # def get_fens_from_pgn(self, raw_pgn):
    #     pgn = io.StringIO(raw_pgn)
    #     game = chess.pgn.read_game(pgn)
    #     board = game.board()
    #     fens = []
    #     for move in game.mainline_moves():
    #         board.push(move)
    #         fens.append((board, move))
    #
    #    return fens

    def generate_gif_from_pgn(self, pgn):
        """Generate the gif image for pgn moves"""
        fens = self.pgn2fen(pgn)
        # fens = self.fens(pgn)
        images = []
        for game_fen in fens:
            fen, last_move_square = game_fen
            self.fen = fen
            move_image = self.generate(last_move_square)
            images.append(move_image)

        return images
