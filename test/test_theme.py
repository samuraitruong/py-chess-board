"""Test theme"""
from app.lib.theme.base_theme import Theme


def test_bw_get_theme():
    """Test get_index_of_square"""
    bw_theme = Theme.get_theme("bw")

    assert (type(bw_theme).__name__) == 'BlackWhiteTheme'
    assert (bw_theme.white_color) == '#BEBEBE'

    assert (type(Theme.get_theme('tournament')).__name__) == 'TournamentTheme'
