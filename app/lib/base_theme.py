"""Base theme class"""
import os
from cairosvg import svg2png
from PIL import Image, ImageFont

class Theme: # pylint: disable=too-few-public-methods
    """Theme base"""
    def __init__(self, piece_set):
        self.piece_set = piece_set

        self.font = {
            "large" : ImageFont.truetype("Arial", 24),
            "regular": ImageFont.truetype("Arial", 18)
        }

    def get_symbol_image(self, symbol, size=(85, 85)):
        """Get the image"""
        image_name = symbol
        if image_name.lower() == image_name:
            image_name = 'b'+image_name
        else:
            image_name = 'w'+image_name
        file_name = f'icons/{self.piece_set}/{image_name.lower()}.png'

        svg_file = f'pieces/{self.piece_set}/{image_name.lower()}.svg'

        svg_png_file = f'pieces/{self.piece_set}/{image_name.lower()}.svg.png'
        # skip convert if the file already converted
        if os.path.exists(svg_png_file):
            piece_image= Image.open(svg_png_file)
            return piece_image.resize(size)

        if os.path.exists(svg_file):

            svg2png(url = svg_file, write_to=svg_file + ".png")
            file_name = svg_file + ".png"

        if os.path.exists(file_name):
            piece_image= Image.open(file_name)
            return piece_image.resize(size)

        return None

    def set_piece_set(self, piece_set):
        self.piece_set = piece_set
