"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class BlackWhiteTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'chessicons'):
        """constructor"""
        super().__init__(piece_set)
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#302E2B'
        self.frame_text_color = '#BEBEBE'
        self.border_outline_color = '#402E2B'
