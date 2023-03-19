"""Share util functions"""
from io import BytesIO
from flask import send_file

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
