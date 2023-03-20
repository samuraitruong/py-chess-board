"""API"""
# from waitress import serve
from flask import Flask, request
from app.lib.board import Board
from app.lib.utils import serve_as_gif, serve_pil_image

api = Flask(__name__)

@api.after_request
def add_header(response):
    """
    Add no-cache header to response headers
    """
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

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

@api.route("/gif")
def generate_gift_from_pgn():
    """Generate gift from pgn """
    pgn = request.args.get('pgn')
    theme = request.args.get('theme')
    duration = int(request.args.get('duration', "1000"))
    # size = int(request.args.get('size', "400"))
    board = Board( theme = theme )

    images =  board.generate_gif_from_pgn(pgn)
    return serve_as_gif(images, duration)


#if __name__ == '__main__':# and os.environ.get('PYTHON_ENV') == 'production':
#    serve(api, host="0.0.0.0", port=8080)
