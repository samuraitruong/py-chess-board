"""Green theme of chess.com default"""
from app.lib.theme.base_theme import Theme


class TournamentTheme(Theme): # pylint: disable=too-few-public-methods
    """Provides default look and feels"""
    def __init__(self, piece_set = 'merida'):
        """constructor"""
        super().__init__(piece_set, board_image='app/boards/tournament.png')
        self.white_color = '#BEBEBE'
        self.black_color = '#242424'
        self.base_color = '#32684A'
        self.frame_text_color = '#EAEBE9'
        self.border_outline_color = '#EAEBE9'
        self.active_square_color = '#1a9c71cc'
