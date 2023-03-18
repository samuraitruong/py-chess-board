from PIL import Image, ImageDraw, ImageFont
from app.lib.theme import DefaultTheme

class Board:
    def __init__(self, fen='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'):
        self.data = []
        self.size = (850, 850)
        self.board = None
        self.theme = DefaultTheme()
        self.margin_left = 25
        self.margin_bottom = 25
        self.fen = fen or 'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR'

        self.font = ImageFont.truetype("Arial", 24)
        self.medium_font = ImageFont.truetype("Arial", 18)

    def generate(self):
        self.board = Image.new('RGB', size=self.size, color= self.theme.base_color)
        for i in range(0,64):
            self.draw_square(i)
        
        self.draw_frame()

        return self.board
    
    def find_piece(self, row, col):
        fen =  self.fen
        list = fen.split('/')
        list = []
        for i in fen.split('/')[row-1]:
            if i.isnumeric():
                for j in range(0, int(i)):
                    list.append(' ')
            else:
                list.append(i)
        # print(fen.split('/')[row-1], row, col, list[col-1], list)
        return list[col]
    
    def draw_square(self,  index):
        square = ImageDraw.Draw(self.board )  
        square_size = 100

        col = index % 8
        row=  8 - int(index/8)

        # print(index, row, col)
        y= (row-1) * square_size  + self.margin_bottom
        x = col * square_size + self.margin_left

        shape = [(x, y), (x+square_size, y+square_size)]
        cell_index = index + 1
        # if cell_index in [2,4,6,8,64, 62, 60, 58]:
        if (row %2 ==0 and col %2 == 1) or (row %2 ==1 and col %2 == 0):
            square.rectangle(shape, fill =self.theme.white_color)
        else:
            square.rectangle(shape, fill = self.theme.black_color)

        d = ImageDraw.Draw(self.board )
        piece = self.find_piece(row, col)
        piece_image = self.theme.get_symbol_image(piece)
        if piece_image:
            self.board.paste(piece_image, (x+20, y+20), mask=piece_image)
        else:
            d.text((x+50, y+ 50), self.find_piece(row, col), fill='red', font= self.font)
               
    def draw_frame(self):
        d = ImageDraw.Draw(self.board )
        for i in range(1,9):
            d.text(( i * 100-23,  827), chr(i + 96), fill= self.theme.frame_text_color, font= self.medium_font)
            d.text(( 10,  870 - i * 100), str(i), fill= self.theme.frame_text_color, font= self.medium_font)