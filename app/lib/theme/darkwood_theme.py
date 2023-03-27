"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class DarkWoodTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'cburnett', board_image = 'app/boards/dark_wood.png'):
        """constructor"""
        super().__init__(piece_set, board_image=board_image)
        self.white_color = '#EDEED2'
        self.black_color = '#759655'
        self.base_color = '#75522E'
        self.frame_text_color = '#EDEED2'
        self.border_outline_color = '#C09B5E'
        self.active_square_color = '#f7e225cc'
