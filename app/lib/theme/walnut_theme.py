"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class WalnutTheme(Theme):  # pylint: disable=too-few-public-methods
    """Provides default look and feels"""

    def __init__(self, piece_set='chessicons'):
        """constructor"""
        super().__init__(piece_set, 'app/boards/walnut.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#73523A'
        self.frame_text_color = '#BFA482'
        self.border_outline_color = '#BFA482'
        self.from_square_color = '#e0dfd3cc'
