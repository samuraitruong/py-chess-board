"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class BlueTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'california' ):
        """constructor"""
        super().__init__(piece_set, board_image='app/boards/blue.png')
        self.white_color = '#3370BD'
        self.black_color = '#242526'
        self.base_color = '#4C7399'
        self.frame_text_color = '#EAE9D2'
        self.border_outline_color = '#EAE9D2'
        self.active_square_color = '#2F88FFCC'
