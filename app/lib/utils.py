"""Share util functions"""
from io import BytesIO
import os, uuid, tempfile as tf
from flask import send_file
from app.lib.theme.green_theme import GreenTheme
from app.lib.theme.default_theme import DefaultTheme
from app.lib.theme.bw_theme import BlackWhiteTheme
from app.lib.theme.orange_theme import OrangeTheme

def make_temp_name(dir = tf.gettempdir()):
    """ Create tmp file name"""
    return os.path.join(dir, str(uuid.uuid1()))

def serve_as_gif(images, duration=1000):
    """Response to client as gif file from multiple images"""
    # img_io = BytesIO()
    tmp_file = make_temp_name() + '.gif'

    images[0].save(tmp_file,
               save_all=True, append_images=images[1:], optimize=False, duration = duration, loop=0, disposal=2000)
    with open(tmp_file, "rb") as fh:
        buf = BytesIO(fh.read())

    os.remove(tmp_file)

    return send_file(buf, mimetype='image/gif')

def serve_pil_image(pil_img, size=1000):
    """Response the image to request client"""
    img_io = BytesIO()
    final_img = pil_img
    width = pil_img.width
    if width != size:
        final_img = pil_img.resize((size, size))
    final_img.save(img_io, 'PNG', quality=100)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

def get_previous_move(fen):
    """
        Return previous move from fen string
    """
    meme = fen.split(' ')
    print(meme)

def get_index_of_square(square_name):
    """ Return the flat index number of given square name. for example a1 ->0 a8 return 56"""
    return ord(square_name[0])-97  + (ord(square_name[1]) - 49) *8

def reverse_index_to_square(index):
    """ Return the flat index number of given square name. for example a1 ->0 a8 return 56"""
    row = str(int(index/8))
    col = chr(index %8 + 97)
    return col + row


def get_theme(name):
    """Get themes from a given name"""
    if name == 'green':
        return GreenTheme()

    if name == 'bw':
        return BlackWhiteTheme()

    if name == 'orange':
        return OrangeTheme()
    return DefaultTheme()


def piece_position_to_fen(piece_position):
    """ Reverse piece position to FEN strings"""
    final_fen =''
    for idx in range(0, 8):
        pos = idx * 8
        row_fen = piece_position[pos : pos + 8]
        # print(row_fen)
        row_fen_string=''
        empty_count = 0
        for piece in row_fen:
            if piece =='':
                empty_count += 1
            else:
                if empty_count >0 :
                    row_fen_string += str(empty_count)
                    empty_count = 0
                row_fen_string += piece

        if empty_count >0:
            row_fen_string += str(empty_count)
        # print(row_fen_string)
        if final_fen == '':
            final_fen = row_fen_string
        else:
            final_fen = row_fen_string+ "/"+ final_fen

    return final_fen
