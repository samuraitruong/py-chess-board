"""Chess board"""
import math
from PIL import Image, ImageDraw

from app.lib.theme.base_theme import Theme
from app.lib.move_utils import (
    break_down_knight_move,
    can_knight_move,
    can_queen_moves,
    can_root_moves,
    can_bishop_moves
)
# import chess.pgn
from app.lib.utils import (
    friendly_print_move,
    get_index_of_square,
    get_square_coordinates,
    reverse_index_to_square,
    piece_position_to_fen,
)


class Board:
    """Chess board"""

    def __init__(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', theme="default", debug=False):
        self.size = (850, 850)
        self.square_size = 100

        self.board = None
        self.theme = Theme.get_theme(theme)
        self.frame_size = 25
        self.fen = fen or 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'
        self.debug = debug

    def generate(self, moved_from_square=None, moved_to_square=None, view_as='w', arrow_squares=None, frameless=False):
        """Generate image"""
        self.board = Image.new('RGBA', size=self.size,
                               color=self.theme.base_color)
        if self.theme.board_image:
            self.board.paste(self.theme.board_image.resize((self.square_size * 8, self.square_size * 8)),
                             (self.frame_size, self.frame_size))

        for i in range(0, 64):
            hightlighted_color = None
            if moved_from_square and get_index_of_square(moved_from_square) == i:
                hightlighted_color = self.theme.from_square_color
            if moved_to_square and get_index_of_square(moved_to_square) == i:
                hightlighted_color = self.theme.current_square_color

            self.draw_square(i, hightlighted_color, view_as)
        self.draw_frame(view_as, frameless)

        if arrow_squares:
            self.draw_move_arrow(
                arrow_squares[0], arrow_squares[1], True, frameless=frameless)
        # sample knight move
        # self.draw_move_arrow('c3', 'e4')

        if view_as in ['b', 'black']:
            return self.board.rotate(180)
        return self.board

    def find_piece(self, row, col):
        """Find the correct piece for the square"""
        fen = self.fen
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

    def draw_square(self,  index, hightlighted_color=None, view_as='w'):
        """Draw a specific square"""
        square = ImageDraw.Draw(self.board)
        square_size = self.square_size

        col = index % 8
        row = 8 - int(index/8)

        # print(index, row, col)
        y_coord = (row-1) * square_size + self.frame_size
        x_coord = col * square_size + self.frame_size

        shape = [(x_coord, y_coord), (x_coord+square_size, y_coord+square_size)]
        cell_index = index + 1
        # if cell_index in [2,4,6,8,64, 62, 60, 58]:
        color = self.theme.black_color
        if (row % 2 == 0 and col % 2 == 1) or (row % 2 == 1 and col % 2 == 0):
            color = self.theme.white_color

        if self.theme.board_image is None:
            square.rectangle(shape,
                             fill=color,
                             width=self.theme.square_border_width,
                             outline=self.theme.square_border_color
                             )

        if hightlighted_color:
            moved_from_square_img = Image.new('RGBA', size=(
                square_size+1, square_size+1), color=hightlighted_color)
            drawer = ImageDraw.Draw(moved_from_square_img)
            # square.rectangle(shape,
            #                 fill = color,
            #                 width= self.theme.square_border_width,
            #                 outline= self.theme.square_border_color

            drawer.rectangle((0, 0, square_size+1, square_size+1),
                             width=self.theme.square_border_width,
                             outline=self.theme.square_border_color)
            self.board.paste(moved_from_square_img,
                             (x_coord, y_coord), mask=moved_from_square_img)

        drawer = ImageDraw.Draw(self.board)
        piece = self.find_piece(row, col)
        piece_image = self.theme.get_symbol_image(piece)
        if piece_image:
            padding = int((square_size - piece_image.width) / 2)
            if view_as in ['b', 'black']:
                piece_image = piece_image.rotate(180)

            self.board.paste(piece_image, (x_coord+padding,
                             y_coord+padding), mask=piece_image)
        else:
            drawer.text((x_coord+self.square_size/2, y_coord + self.square_size/2),
                        self.find_piece(row, col),
                        fill='red',
                        font=self.theme.font.get('large')
                        )
        if self.debug:
            drawer.text((x_coord+75, y_coord + 5),
                        str(cell_index-1),
                        fill='red',
                        font=self.theme.font.get('regular')
                        )

    def draw_frame(self, view_as, frameless=False):
        """ Draw the number and column name on edge of board"""
        is_black_view = view_as in ['black', 'b']
        drawer = ImageDraw.Draw(self.board, 'RGBA')
        frame_image = Image.new('RGBA', size=(
            850, self.frame_size), color='#00000000')

        vertical_image = Image.new('RGBA', size=(
            self.frame_size, 850), color='#00000000')

        drawer_top = ImageDraw.Draw(frame_image, 'RGBA')
        drawer_number = ImageDraw.Draw(vertical_image, 'RGBA')

        for i in range(1, 9):
            display_num = str(i)
            display_col = chr(i + 96)

            if is_black_view:
                display_num = str(9-i)
                display_col = chr(-i + 9 + 96)

            width, height = drawer.textsize(display_col,
                                            font=self.theme.font.get('regular')
                                            )

            drawer_top.text((self.frame_size + i * self.square_size - self.square_size/2 - width/2,  2), display_col,
                            fill=self.theme.frame_text_color,
                            font=self.theme.font.get('regular')
                            )

            width, height = drawer_top.textsize(display_num,
                                                font=self.theme.font.get(
                                                    'regular')
                                                )

            drawer_number.text((10,  8*self.square_size + 2 * self.frame_size - i * self.square_size + height), display_num,
                               fill=self.theme.frame_text_color,
                               font=self.theme.font.get('regular')
                               )
        if is_black_view:
            vertical_image = vertical_image.rotate(180)

        self.board.paste(
            frame_image, (0, 8 * self.square_size + self.frame_size), mask=frame_image)
        self.board.paste(frame_image.rotate(180), (0, 0),
                         mask=frame_image.rotate(180))
        self.board.paste(vertical_image, (0, 0), mask=vertical_image)
        self.board.paste(vertical_image, (8 * self.square_size +
                         self.frame_size, 0), mask=vertical_image)

        drawer.rectangle(
            (
                self.frame_size - self.theme.outline_border_width,
                self.frame_size - self.theme.outline_border_width,
                8*self.square_size + self.frame_size,
                8*self.square_size + self.frame_size
            ),
            fill=None,
            outline=self.theme.border_outline_color,
            width=self.theme.outline_border_width
        )
        if frameless:
            box_size = self.frame_size + 8 * self.square_size + self.theme.outline_border_width

            self.board = self.board.crop((
                self.frame_size - self.theme.outline_border_width, self.frame_size-self.theme.outline_border_width, box_size, box_size))

            self.board.paste(vertical_image, (-5, 10), mask=vertical_image)
            self.board.paste(
                vertical_image, (8 * self.square_size - 23, 10), mask=vertical_image)

            self.board.paste(
                frame_image, (20, 8 * self.square_size - self.frame_size), mask=frame_image)
            self.board.paste(
                frame_image, (20, 0), mask=frame_image)

    def draw_move_arrow(self, from_square, to_square, arrow_head=True, draw_circle=False, frameless=False):
        """Draw a move arrow between square and square"""
        # https://stackoverflow.com/questions/43527894/drawing-arrowheads-which-follow-the-direction-of-the-line-in-pygame
        start_x, start_y = get_square_coordinates(
            from_square, self.square_size)
        end_x, end_y = get_square_coordinates(to_square, self.square_size)
        diff_x = abs(int((start_x - end_x) / self.square_size))
        diff_y = abs(int((start_y - end_y)/self.square_size))

        if (diff_x == 2 and diff_y == 1) or (diff_x == 1 and diff_y == 2):
            line1, line2 = break_down_knight_move((from_square, to_square))
            self.draw_move_arrow(line1[0], line1[1],
                                 False, True, frameless=frameless)
            self.draw_move_arrow(line2[0], line2[1], True, frameless=frameless)

        else:
            arrow_image = Image.new(
                'RGBA', size=self.size, color=(255, 255, 255, 0))

            # reset x
            drawer = ImageDraw.Draw(arrow_image)
            center_adjustment = self.square_size/2 + self.frame_size
            if frameless:
                center_adjustment = center_adjustment - self.frame_size

            start_point = (start_x + center_adjustment,
                           start_y + center_adjustment)
            end_point = (end_x + center_adjustment, end_y + center_adjustment)
            x_0, y_0 = start_point
            x_1, y_1 = end_point

            # if(x_1 == x_0):
            if y_0 != y_1 and arrow_head:
                shorter_arrow = 35 * (y_0 - y_1)/(abs(y_0-y_1))
                y_1 = y_1 + shorter_arrow

            # if(y_1 == y_0):
            if x_0 != x_1 and arrow_head:
                shorter_arrow = 35 * (x_0 - x_1)/(abs(x_0-x_1))
                x_1 = x_1 + shorter_arrow

            drawer.line(((x_0, y_0), (x_1, y_1)),
                        fill=self.theme.move_arrow_color, width=30)
            if arrow_head:
                trirad = 30
                rotation = math.degrees(math.atan2(x_1-x_0, y_1 - y_0)) + 120
                points = [
                    (int(x_1+trirad*math.sin(math.radians(rotation))),
                     int(y_1+trirad*math.cos(math.radians(rotation)))),
                    (x_1+trirad*math.sin(math.radians(rotation-120)),
                     y_1+trirad*math.cos(math.radians(rotation-120))),
                    (x_1+trirad*math.sin(math.radians(rotation+120)),
                     y_1+trirad*math.cos(math.radians(rotation+120)))
                ]

                drawer.polygon(points, fill=self.theme.move_arrow_color)

            if draw_circle:
                border = 14
                drawer.ellipse((x_1-border, y_1-border, x_1+border,
                               y_1+border), fill=self.theme.move_arrow_color)
            self.board.paste(arrow_image, mask=arrow_image)

    def pgn2fen(self, raw_pgn):
        """
        Generate array of game FENs from pgn moves
        This function is very messy but get it working first then we optimise it later

        """
        pgn = raw_pgn.replace('\n', ' ').replace('\r', ' ')
        default_fen = 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'.split('/')
        piece_position = [''] * 64
        default_fen.reverse()
        game_fens = [
            ('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', None, None, None)]
        index = 0
        for row_fen in default_fen:
            for piece in row_fen:
                if piece.isnumeric():
                    for _ in range(0, int(piece)):
                        piece_position[index] = ''
                        index += 1
                else:
                    piece_position[index] = piece
                    index += 1

        # loop throught the PGN step and generate all the FEN
        pgn_moves = [move.strip() for move in pgn.split(' ')
                     if "." not in move
                     and len(move) > 0
                     and move.strip() not in ['1-0', '0-1', '1/2-1/2', "*"]]

        board_cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for move_index, raw_move in enumerate(pgn_moves):
            print('notation', raw_move)
            move = raw_move.replace('+', '').replace('#', '')
            move_piece = move[0]
            original_move_piece = move[0]
            move_square = move[-2:]
            is_captured_move = 'x' in raw_move
            # is_checked_move = '+' in raw_move
            is_checkmate = '#' in raw_move
            implicit_move_index = -1

            # to keep the index of the specific move when there is multiple possibility more of the piece.
            # for example Rhf8, move the root from h column to f8 (h8f8)

            player = 'w'
            from_square = None
            if move_index % 2 == 1:
                player = 'b'

            # check for special moves ie castling o o o and o-o
            if move in ["O-O", 'O-O']:
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

                game_fens.append(
                    (piece_position_to_fen(piece_position), None, None, raw_move))
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

                game_fens.append(
                    (piece_position_to_fen(piece_position), None, None, raw_move))
                continue

            # check for special move promotion to new piece
            if '=' in raw_move:
                # promotion to the queen/or any piece
                parsed = raw_move.split('=')
                promoted_piece = parsed[1].replace('+', '').replace('#', '')
                pawn_cell = parsed[0]
                index = get_index_of_square(pawn_cell)
                captured_and_promote = 'x' in raw_move

                if player == 'w':
                    if captured_and_promote:
                        # need to check the pawn capture move again
                        from_pawn_cell = ord(raw_move[0]) - 97 + 8*6
                        print("captured_and_promote", raw_move,
                              from_pawn_cell, raw_move[0])
                        piece_position[from_pawn_cell] = ''
                        index = get_index_of_square(pawn_cell[-2:])
                        from_square = reverse_index_to_square(from_pawn_cell)
                        # raise Exception('stop')
                    else:
                        from_square = reverse_index_to_square(index-8)
                        piece_position[index - 8] = ''  # reset previous paw

                    piece_position[index] = promoted_piece.upper()
                    # need to handle capture and promotion to new piece

                if player == 'b':
                    print('black promotion come here',
                          raw_move, captured_and_promote)
                    if captured_and_promote:
                        # need to check the pawn capture move again
                        from_pawn_cell = ord(raw_move[0]) - 97 + 8
                        print("captured_and_promote", raw_move,
                              from_pawn_cell, raw_move[0], pawn_cell[-2:])
                        piece_position[from_pawn_cell] = ''
                        from_square = reverse_index_to_square(from_pawn_cell)
                        index = get_index_of_square(pawn_cell[-2:])
                    else:
                        from_square = reverse_index_to_square(index + 8)
                        piece_position[index + 8] = ''  # reset previous pawn

                    piece_position[index] = promoted_piece.lower()

                game_fens.append((piece_position_to_fen(
                    piece_position), pawn_cell, from_square, raw_move))

                continue

            if (len(move) == 2 and player == 'w') or move_piece == 'x' or move_piece in board_cols:
                move_piece = 'P'

            if (len(move) == 2 and player == 'b') or move_piece == 'x' or move_piece in board_cols:
                move_piece = 'p'

            if move_index % 2 == 1:
                move_piece = move_piece.lower()

            # handle Nbxd7
            # Handle N3xd4
            possible_indexes = [i for i, x in enumerate(
                piece_position) if x == move_piece]

            #
            if (len(move) == 4 or (len(move) == 5 and is_captured_move)) and move[1] in board_cols:
                #   find index of implicit move
                print('Implicit move: ', raw_move, move,
                      move_piece, possible_indexes)
                for i in possible_indexes:
                    square_name = reverse_index_to_square(i)
                    # check if square is same row or same column
                    if square_name[0] == raw_move[1] or square_name[0] == raw_move[1]:
                        implicit_move_index = i
            # R8f5 -> move the root from row 8 to F5. ie Rf8 -> f5
            if len(move) == 4 and move[1].isdigit():
                print('specifial move with row index', move, possible_indexes)
                for i in possible_indexes:
                    square_name = reverse_index_to_square(i)
                    # check if square is same row or same column
                    if square_name[1] == move[1] or square_name[0] == move[1]:
                        implicit_move_index = i

            index = get_index_of_square(move_square)
            print(move_index, move, '->', player,
                  move_piece, move_square, index)

            # when the move match with the position, then go ahead to update it without any detect logic
            if implicit_move_index > 0:
                piece_position[index] = move_piece
                piece_position[implicit_move_index] = ''
                game_fens.append((piece_position_to_fen(piece_position), move_square,
                                  reverse_index_to_square(implicit_move_index), raw_move))
                continue

            # #white pawn move
            if move_piece == 'P':
                if is_captured_move:
                    possible_indexes = [index - 7, index-9]
                    print('pawn captured move')
                    # check  if the move is en passant move

                    # handel pawn move capture such as fxd4 -> the pawn on f col capture d4

                    if is_captured_move:
                        current_col = move_square[0]
                        target_index = get_index_of_square(move_square)
                        if piece_position[target_index] == '':
                            print('en passant move', move_square, index)
                            piece_position[index - 8] = ''
                            from_square = reverse_index_to_square(index - 8)
                        else:
                            if current_col < original_move_piece:
                                possible_indexes = [index-7]
                            else:
                                possible_indexes = [index-9]

                    # print('possible pawn index', possible_indexes)
                    possible_indexes = [
                        move for move in possible_indexes if piece_position[move] == move_piece]
                    friendly_print_move(move_piece, possible_indexes)
                    if len(possible_indexes) > 0:
                        piece_position[possible_indexes[0]] = ''
                        from_square = reverse_index_to_square(
                            possible_indexes[0])
                else:
                    possible_index_1 = index - 8
                    possible_index_2 = index - 16

                    if possible_index_1 > 0 and piece_position[possible_index_1] == 'P':
                        piece_position[possible_index_1] = ''
                        from_square = reverse_index_to_square(possible_index_1)
                    # need check first move
                    if possible_index_2 > 0 and piece_position[possible_index_2] == 'P':
                        piece_position[possible_index_2] = ''
                        from_square = reverse_index_to_square(possible_index_2)
            # Black pawn moves
            if move_piece == 'p':

                if is_captured_move:
                    possible_indexes = [index + 7, index+9]
                    if is_captured_move:
                        current_col = move_square[0]
                        # print('pawn capture', current_col, )
                        if current_col < original_move_piece:
                            possible_indexes = [index+9]
                        else:
                            possible_indexes = [index + 7]

                    possible_indexes = [
                        move for move in possible_indexes if piece_position[move] == move_piece]
                    if len(possible_indexes) > 0:
                        piece_position[possible_indexes[0]] = ''
                        from_square = reverse_index_to_square(
                            possible_indexes[0])
                else:
                    possible_index_1 = index + 8
                    possible_index_2 = index + 16

                    if possible_index_1 > 0 and piece_position[possible_index_1] == 'p':
                        piece_position[possible_index_1] = ''
                        from_square = reverse_index_to_square(possible_index_1)
                    # need check first move
                    if possible_index_2 > 0 and piece_position[possible_index_2] == 'p':
                        piece_position[possible_index_2] = ''
                        from_square = reverse_index_to_square(possible_index_1)

            # Knight move
            if move_piece in ['N', 'n']:
                # possible_indexes =  [i for i, x in enumerate(piece_position)
                #                      if x == move_piece]

                possible_indexes = [move for move in possible_indexes
                                    if can_knight_move(move, index)]
                # possible_indexes = list(set(possible_indexes))
                # print('possible_indexes', move_index, possible_indexes)
                if len(possible_indexes) > 0:
                    piece_position[possible_indexes[0]] = ''
                    from_square = reverse_index_to_square(possible_indexes[0])

            # Bishop move

            if move_piece in ['B', 'b']:
                possible_indexes = [move for move in possible_indexes
                                    if can_bishop_moves(piece_position, move, index)]
                # print ('possible_indexes', possible_indexes)
                if len(possible_indexes) > 0:
                    piece_position[possible_indexes[0]] = ''
                    from_square = reverse_index_to_square(possible_indexes[0])

            # Rook Moves
            if move_piece in ['R', 'r']:
                possible_indexes = [move for move in possible_indexes if can_root_moves(
                    piece_position, move, index)]
                friendly_print_move(move_piece, possible_indexes)
                if len(possible_indexes) > 0:
                    piece_position[possible_indexes[0]] = ''
                    from_square = reverse_index_to_square(possible_indexes[0])

            # King
            if move_piece in ['K', 'k']:
                king_index = piece_position.index(move_piece)
                if king_index > 0:
                    piece_position[king_index] = ''
                    from_square = reverse_index_to_square(king_index)

            if move_piece in ['Q', 'q']:

                possible_indexes = [move for move in possible_indexes if can_queen_moves(
                    piece_position, move, index)]
                friendly_print_move(move_piece, possible_indexes)
                if len(possible_indexes) >= 1:
                    piece_position[possible_indexes[0]] = ''
                    from_square = reverse_index_to_square(possible_indexes[0])
                else:
                    print('need to handle if there is more than 1 queen')
                    # raise Exception('error')

            piece_position[index] = move_piece

            final_fen = piece_position_to_fen(piece_position)
            game_fens.append((final_fen, move_square, from_square, raw_move))

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

    def generate_gif_from_pgn(self, pgn, move_arrow=False, viewer='w', frameless=False, frames_count=1000):
        """Generate the gif image for pgn moves"""
        fens = self.pgn2fen(pgn)
        # fens = self.fens(pgn)
        images = []
        for game_fen in fens[:frames_count]:
            fen, last_move_square, move_from_square, raw_move = game_fen
            self.fen = fen
            # print('last_move_square , move_from_square', last_move_square , move_from_square)
            arrow_squares = None
            if last_move_square and move_from_square and move_arrow:
                arrow_squares = (move_from_square, last_move_square)
            move_image = self.generate(
                move_from_square, last_move_square, arrow_squares=arrow_squares, view_as=viewer, frameless=frameless)
            if raw_move and self.debug:
                drawer = ImageDraw.Draw(move_image)
                drawer.text((10, 10), raw_move, fill=(255, 255, 255),
                            font=self.theme.font.get('x-large'))

            images.append(move_image)

        return images
