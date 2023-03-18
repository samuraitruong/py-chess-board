"""API"""
from flask import Flask, request
from app.lib.board import Board

from app.lib.utils import serve_pil_image

app = Flask(__name__)

@app.route("/")
def generate_chess_from_fen():
    """The api entrypoing to generate board image from fen"""
    fen = request.args.get('fen')
    size = int(request.args.get('size', "850"))
    board = Board(fen  = fen)
    return serve_pil_image(board.generate(), size)
