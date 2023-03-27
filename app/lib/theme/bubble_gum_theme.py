"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class BubbleGumTheme(Theme):  # pylint: disable=too-few-public-methods
    """Provides default look and feels"""

    def __init__(self, piece_set='chessicons', ):
        """constructor"""
        super().__init__(piece_set)
        self.white_color = '#FFFFFF'
        self.black_color = '#FCD7DD'
        self.base_color = '#fdd'
        self.frame_text_color = '#898989'
        self.border_outline_color = '#eeeeee'
        self.from_square_color = '#e0dfd3cc'
