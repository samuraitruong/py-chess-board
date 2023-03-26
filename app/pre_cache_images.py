
import os

from app.lib.board import Board

def cach_all() :

    piece_set_folder = os.getcwd() + '/app/pieces'

    subfolders= [f.name for f in os.scandir(piece_set_folder) if f.is_dir()]
    for piece_set in subfolders:
        board = Board()
        board.theme.set_piece_set(piece_set)
        board.generate()


if __name__ == '__main__':
    print ('hello')
