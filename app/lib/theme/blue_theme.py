"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class BlueTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'california'):
        """constructor"""
        super().__init__(piece_set)
        self.white_color = '#3370BD'
        self.black_color = '#242526'
        self.base_color = '#4E4F50'
        self.frame_text_color = '#BEBEBE'
        self.border_outline_color = '#3A3B3C'
        self.active_square_color = '#2F88FF'
