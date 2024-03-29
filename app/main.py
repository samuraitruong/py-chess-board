"""API"""
# from waitress import serve
import os
from os.path import isfile, join
from flask import Flask, request, render_template
from app.lib.board import Board
from app.lib.utils import serve_as_gif, serve_pil_image
from app.lib.theme.base_theme import Theme

api = Flask(__name__,
            static_url_path='/static',
            static_folder=os.getcwd() + '/app/pgn',)


@api.after_request
def add_header(response):
    """
    Add no-cache header to response headers
    """
    response.headers["Cache-Control"] = 'no-cache, no-store, must-revalidate'
    response.headers["Pragma"] = 'no-cache'
    response.headers["Expires"] = '0'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@api.route("/playground")
def playground():
    """Render simple html to test the api"""
    # return os. getcwd()
    # read all the file inside pgn and add to the list
    folder = os.getcwd() + '/app/pgn'
    piece_set_folder = os.getcwd() + '/app/pieces'

    onlyfiles = [f for f in os.listdir(folder) if isfile(
        join(folder, f)) and '.pgn' in f]
    onlyfiles.sort()
    fens = []

    with open(os.getcwd() + '/app/pgn/puzzle.txt', 'r', encoding="utf-8") as puzzle_file:
        fens = puzzle_file.readlines()

    data_sources = []
    for file_name in onlyfiles:
        with open(join(folder, file_name), encoding="utf-8") as pgn_file:
            pgn = pgn_file.read()
            index = pgn.index('1. ')
            pgn_only = pgn[index-2:].replace('\n', ' ')
            data_sources.append((file_name, pgn_only))
    # piece_sets = []

    subfolders = [f.name for f in os.scandir(piece_set_folder) if f.is_dir()]
    subfolders.sort()
    return render_template('playground.html',
                           data_sources=data_sources,
                           themes=Theme.get_theme_list(),
                           piece_sets=subfolders,
                           fen_sources=fens
                           )


@api.route("/")
def generate_chess_from_fen():
    """The api entrypoint to generate board image from fen"""
    fen = request.args.get('fen')
    theme = request.args.get('theme')
    size = int(request.args.get('size', "850"))
    view_as = request.args.get('viewer', "w")
    frameless = request.args.get('frame') == "false"

    board = Board(fen=fen, theme=theme)
    if request.args.get('piece'):
        board.theme.set_piece_set(request.args.get('piece'))
    return serve_pil_image(board.generate(view_as=view_as, frameless=frameless), size)


@api.route("/gif")
def generate_gift_from_pgn():
    """Generate gift from pgn """
    max_frames = int(os.environ.get('MAX_FRAMES', "10000"))
    pgn = request.args.get('pgn')
    view_as = request.args.get('viewer', "w")

    theme = request.args.get('theme')
    move_arrow = request.args.get('arrow', False, bool)
    duration = int(request.args.get('duration', "1000"))
    # size = int(request.args.get('size', "400"))
    board = Board(theme=theme, debug=os.environ.get('DEBUG', '0') == '1')
    frameless = request.args.get('frame') == "false"

    if request.args.get('piece'):
        board.theme.set_piece_set(request.args.get('piece'))

    images = board.generate_gif_from_pgn(pgn,
                                         move_arrow in ['true', '1', True],
                                         viewer=view_as,
                                         frameless=frameless,
                                         frames_count=max_frames)
    return serve_as_gif(images, duration)
