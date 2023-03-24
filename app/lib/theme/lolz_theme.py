"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class LolzTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'merida'):
        """constructor"""
        super().__init__(piece_set, board_image='app/boards/lolz.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#777D7C'
        self.frame_text_color = '#222'
        self.border_outline_color = '#D5E0E1'
        self.active_square_color = '#1a9c71'
