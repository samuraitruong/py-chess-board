"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class GreenTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'cburnett'):
        """constructor"""
        super().__init__(piece_set)
        self.white_color = '#EDEED2'
        self.black_color = '#759655'
        self.base_color = '#302E2B'
        self.frame_text_color = '#EDEED2'
        self.border_outline_color = '#402E2B'
        self.active_square_color = '#f7e225'
