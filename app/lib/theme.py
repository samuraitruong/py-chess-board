"""Default theme"""
from app.lib.base_theme import Theme


class DefaultTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self):
        """constructor"""
        super().__init__()
        self.white_color = '#eeeee4'
        self.black_color = '#e9873a'
        self.base_color = '#4e2b14'
        self.symbol_set = 'default'
        self.frame_text_color = '#fff'
