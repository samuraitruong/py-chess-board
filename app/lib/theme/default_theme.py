"""Default theme"""
from app.lib.theme.base_theme import Theme


class DefaultTheme(Theme):  # pylint: disable=too-few-public-methods
    """Provides default look and feels"""

    def __init__(self, piece_set='chessmonk'):
        """set default look and feel"""
        super().__init__(piece_set)
        self.white_color = '#eeeee4'
        self.black_color = '#e9873a'
        self.base_color = '#DA883A'
        self.frame_text_color = '#fff'
        self.border_outline_color = '#FA883A'
        self.from_square_color = '#ed2d187D'
        self.current_square_color = '#ed2d18cc'
        self.move_arrow_color = '#00aa00aa'
