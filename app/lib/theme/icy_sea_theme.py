"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class IcySeaTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'cardinal'):
        """constructor"""
        super().__init__(piece_set, 'app/boards/icy_sea.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#7B9FB3'
        self.frame_text_color = '#E4E9EB'
        self.border_outline_color = '#E4E9EB'
        self.active_square_color = '#e0dfd3'
