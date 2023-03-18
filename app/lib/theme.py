from app.lib.base_theme import Theme


class DefaultTheme(Theme):
    def __init__(self):
        self.white_color = '#eeeee4'
        self.black_color = '#e9873a'
        self.base_color = '#4e2b14'
        self.symbol_set = 'default'
        self.frame_text_color = '#fff'