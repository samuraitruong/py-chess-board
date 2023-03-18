from PIL import Image
import os

class Theme:
    def __init__(self):
        self.symbol_set = 'theme'
    def get_symbol_image(self, symbol, size=(70,70)):
        image_name = symbol
        if image_name.lower() == image_name:
            image_name = 'b'+image_name
        else:
            image_name = 'w'+image_name
        file_name = f'icons/{self.symbol_set}/{image_name.lower()}.png'

        if os.path.exists(file_name):
            pn= Image.open(file_name)
            return pn.resize(size)
        
        return None