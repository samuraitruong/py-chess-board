"""Default theme"""
from app.lib.base_theme import Theme


class DefaultTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'chessmonk'):
        """constructor"""
        super().__init__(piece_set)
        self.white_color = '#eeeee4'
        self.black_color = '#e9873a'
        self.base_color = '#4e2b14'
        self.frame_text_color = '#fff'
        self.border_outline_color = '#5e483e'
