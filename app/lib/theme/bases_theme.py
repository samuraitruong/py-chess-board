"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class BaseTheme(Theme):  # pylint: disable=too-few-public-methods
    """Provides default look and feels"""

    def __init__(self, piece_set='chessicons', ):
        """constructor"""
        super().__init__(piece_set, 'app/boards/bases.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#BF6836'
        self.frame_text_color = '#EFC99D'
        self.border_outline_color = '#EFC99D'
        self.from_square_color = '#e0dfd3cc'
