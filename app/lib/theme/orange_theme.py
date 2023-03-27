"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class OrangeTheme(Theme):  # pylint: disable=too-few-public-methods
    """Provides default look and feels"""

    def __init__(self, piece_set='chessnut'):
        """constructor"""
        super().__init__(piece_set)
        self.white_color = '#FF7900'
        self.black_color = '#151414'
        self.base_color = '#302E2B'
        self.frame_text_color = '#D3D4D5'
        self.border_outline_color = '#402E2B'
        self.square_border_width = 3
        self.square_border_color = '#D3D4D5'
        self.from_square_color = '#30D2F2CC'
