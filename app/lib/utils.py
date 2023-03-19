"""Share util functions"""
from io import BytesIO
from flask import send_file
from app.lib.theme.green_theme import GreenTheme
from app.lib.theme.default_theme import DefaultTheme
from app.lib.theme.bw_theme import BlackWhiteTheme
from app.lib.theme.orange_theme import OrangeTheme

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


def get_theme(name):
    """Get themes from a given name"""
    if name == 'green':
        return GreenTheme()

    if name == 'bw':
        return BlackWhiteTheme()

    if name == 'orange':
        return OrangeTheme()
    return DefaultTheme()
