"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class BurledWoodTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'merida'):
        """constructor"""
        super().__init__(piece_set, board_image='app/boards/burled_wood.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#62361D'
        self.frame_text_color = '#F0CA9E'
        self.border_outline_color = '#8A5333'
        self.active_square_color = '#1a9c71'
