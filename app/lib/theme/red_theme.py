"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class RedTheme(Theme):  # pylint: disable=too-few-public-methods
    """Provides default look and feels"""

    def __init__(self, piece_set='companion'):
        """constructor"""
        super().__init__(piece_set)
        self.white_color = '#FF0100'
        self.black_color = '#000000'
        self.base_color = '#EF0100'
        self.frame_text_color = '#EAE9D2'
        self.border_outline_color = '#EAE9D2'
        self.from_square_color = '#2F88FFCC'
