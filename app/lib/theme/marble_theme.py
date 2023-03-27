"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class MarbleTheme(Theme):  # pylint: disable=too-few-public-methods
    """Provides default look and feels"""

    def __init__(self, piece_set='chessicons', ):
        """constructor"""
        super().__init__(piece_set, 'app/boards/marble.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#706B66'
        self.frame_text_color = '#DDDBD1'
        self.border_outline_color = '#DDDBD1'
        self.from_square_color = '#e0dfd3cc'
