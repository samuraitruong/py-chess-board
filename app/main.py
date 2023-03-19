"""API"""
# from waitress import serve
from flask import Flask, request
from app.lib.board import Board
from app.lib.utils import serve_pil_image

api = Flask(__name__)

@api.route("/")
def generate_chess_from_fen():
    """The api entrypoint to generate board image from fen"""
    fen = request.args.get('fen')
    theme = request.args.get('theme')
    size = int(request.args.get('size', "850"))
    board = Board(fen  = fen, theme = theme )
    if request.args.get('piece'):
        board.theme.set_piece_set(request.args.get('piece'))
    return serve_pil_image(board.generate(), size)


#if __name__ == '__main__':# and os.environ.get('PYTHON_ENV') == 'production':
#    serve(api, host="0.0.0.0", port=8080)
