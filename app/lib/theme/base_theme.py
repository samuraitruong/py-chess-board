"""Base theme class"""
import os
from cairosvg import svg2png
from PIL import Image, ImageFont

cache = {} # maybe use lru_cache but now keep it simple

class Theme: # pylint: disable=too-few-public-methods
    """Theme base"""
    def __init__(self, piece_set):
        self.piece_set = piece_set
        self.square_border_width = 0
        self.square_border_color = None
        self.last_move_square_color = 'red'
        self.font = {
            "large" : ImageFont.truetype("app/fonts/arial/arial.ttf", 24),
            "regular": ImageFont.truetype("app/fonts/arial/arial.ttf", 18)
        }

    def get_symbol_image(self, piece_name, size=(85, 85)):
        """Get the image"""

        image_name = piece_name
        if image_name.lower() == image_name:
            image_name = 'b'+image_name
        else:
            image_name = 'w'+image_name
        file_name = f'app/pieces/{self.piece_set}/{image_name.lower()}.png'

        svg_file = f'app/pieces/{self.piece_set}/{image_name.lower()}.svg'

        svg_png_file = f'app/pieces/{self.piece_set}/{image_name.lower()}.svg.png'

        cache_key = svg_file + str(size)

        cache_image = cache.get(cache_key)

        if cache_image:
            return cache_image

                # skip convert if the file already converted
        if os.path.exists(svg_png_file):
            piece_image= Image.open(svg_png_file)
            cache_image =  piece_image.resize(size)
            cache[cache_key] = cache_image
            return cache_image

        if os.path.exists(svg_file):

            svg2png(url = svg_file,
                    write_to=svg_file + ".png",
                    output_width = 512,
                    output_height = 512
                )
            file_name = svg_file + ".png"

        if os.path.exists(file_name):
            piece_image= Image.open(file_name)
            cache_image =  piece_image.resize(size)
            cache[cache_key] = cache_image
            return cache_image

        return None

    def set_piece_set(self, piece_set):
        """set piece set"""
        self.piece_set = piece_set
