"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class SandTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'fresca'):
        """constructor"""
        super().__init__(piece_set, board_image='app/boards/sand.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#BFAA95'
        self.frame_text_color = '#eeeeee'
        self.border_outline_color = '#DDCEC0'
        self.active_square_color = '#1a9c71'
