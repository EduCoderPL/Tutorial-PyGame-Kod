from constants import COLOR_WHITE


class Text:

    def __init__(self, string, position, font, color=COLOR_WHITE):

        self.string = string
        self.position = position
        self.font = font
        self.color = color


    def draw(self, screen, string=None):

        if string is not None:
            self.string = string

        textGraphics = self.font.render(self.string, True, self.color)
        textRect = textGraphics.get_rect()
        textRect.center = self.position
        screen.blit(textGraphics, textRect)