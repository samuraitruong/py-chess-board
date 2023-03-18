"""Chess board"""
from PIL import Image, ImageDraw
from app.lib.theme import DefaultTheme

class Board:
    """Chess board"""
    def __init__(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'):
        self.size = (850, 850)
        self.board = None
        self.theme = DefaultTheme()
        self.frame_size = 25
        self.fen = fen or 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

    def generate(self):
        """Generate image"""
        self.board = Image.new('RGB', size=self.size, color= self.theme.base_color)
        for i in range(0,64):
            self.draw_square(i)

        self.draw_frame()

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

    def draw_square(self,  index):
        """Draw a specific square"""
        square = ImageDraw.Draw(self.board )
        square_size = 100

        col = index % 8
        row=  8 - int(index/8)

        # print(index, row, col)
        y_coord = (row-1) * square_size  + self.frame_size
        x_coord = col * square_size + self.frame_size

        shape = [(x_coord, y_coord), (x_coord+square_size, y_coord+square_size)]
        # cell_index = index + 1
        # if cell_index in [2,4,6,8,64, 62, 60, 58]:
        if (row %2 ==0 and col %2 == 1) or (row %2 ==1 and col %2 == 0):
            square.rectangle(shape, fill =self.theme.white_color)
        else:
            square.rectangle(shape, fill = self.theme.black_color)

        drawer = ImageDraw.Draw(self.board )
        piece = self.find_piece(row, col)
        piece_image = self.theme.get_symbol_image(piece)
        if piece_image:
            padding = int((square_size - piece_image.width) /2)
            self.board.paste(piece_image, (x_coord+padding, y_coord+padding), mask=piece_image)
        else:
            drawer.text((x_coord+50, y_coord+ 50),
                        self.find_piece(row, col),
                        fill='red',
                        font= self.theme.font.get('large')
                    )

    def draw_frame(self):
        """ Draw the number and column name on edge of board"""
        drawer = ImageDraw.Draw(self.board )
        for i in range(1,9):
            drawer.text(( i * 100-23,  827), chr(i + 96),
                        fill= self.theme.frame_text_color,
                        font= self.theme.font.get('regular')
                    )
            drawer.text(( 10,  870 - i * 100), str(i),
                        fill= self.theme.frame_text_color,
                        font= self.theme.font.get('regular')
                    )

        drawer.rectangle(
            (
                self.frame_size,
                self.frame_size,
                800 + self.frame_size,
                800 + self.frame_size
            ),
            fill=None,
            outline= self.theme.border_outline_color,
            width=2
            )
