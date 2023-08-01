"""Cache images"""
import os

from app.lib.board import Board


def cache_all():
    """Cache all image by call all piece set to generate svg"""
    piece_set_folder = os.getcwd() + '/app/pieces'

    subfolders = [f.name for f in os.scandir(piece_set_folder) if f.is_dir()]
    for piece_set in subfolders:
        try:
            print('generate board with ' + piece_set)
            board = Board()
            board.theme.set_piece_set(piece_set)
            board.generate()
        # pylint: disable=W0718
        except Exception:  # [broad-exception-caught]
            print('Error generating board images: ' + piece_set)


if __name__ == '__main__':
    cache_all()
