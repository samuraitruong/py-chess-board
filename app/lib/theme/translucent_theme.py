"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class TranslucentTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'merida'):
        """constructor"""
        super().__init__(piece_set, board_image='app/boards/translucent.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#A38548'
        self.frame_text_color = '#222'
        self.border_outline_color = '#E5E2CA'
        self.active_square_color = '#1a9c71cc'
