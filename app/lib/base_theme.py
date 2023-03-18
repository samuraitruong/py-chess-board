"""Base theme class"""
import os
from PIL import Image, ImageFont

class Theme: # pylint: disable=too-few-public-methods
    """Theme base"""
    def __init__(self):
        self.symbol_set = 'theme'
        self.font = {
            "large" : ImageFont.truetype("Arial", 24),
            "regular": ImageFont.truetype("Arial", 18)
        }

    def get_symbol_image(self, symbol, size=(75, 75)):
        """Get the image"""
        image_name = symbol
        if image_name.lower() == image_name:
            image_name = 'b'+image_name
        else:
            image_name = 'w'+image_name
        file_name = f'icons/{self.symbol_set}/{image_name.lower()}.png'

        if os.path.exists(file_name):
            piece_image= Image.open(file_name)
            return piece_image.resize(size)

        return None
