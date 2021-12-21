import pygame


class Panel(object):
    def __init__(self, x, y, length, height):
        self.length = length
        self.height = height
        self.x = x
        self.y = y
        self.xp = self.x + 50
        self.yp = self.y + 50
        self.size_p = 30
        self.size_f = 30
        self.color = (170, 102, 81)
        self.pause = False
        self.button_filter_list = [[20, 120], [70, 120], [120, 120], [20, 170], [70, 170]]
        self.filter_color_list = [(0, 100, 0), (255, 69, 0), (105, 105, 105), (75, 0, 130), (47, 79, 79)]

    def draw_panel(self, window):
        pygame.draw.rect(window, self.color, [self.x, self.y, self.length, self.height])
        self.draw_pause_button(window)
        self.draw_filter_button(window)

    def draw_filter_button(self, window):
        number_filter = 0
        for pos in self.button_filter_list:
            pygame.draw.rect(window, self.filter_color_list[number_filter],
                             [pos[0] + self.x, pos[1] + self.y, self.size_f, self.size_f])
            number_filter += 1

    def draw_pause_button(self, window):
        pygame.draw.rect(window, (255, 255, 255), [self.xp, self.yp, self.size_p, self.size_p])
        if self.pause:
            pygame.draw.line(window, (0, 0, 0), [self.xp + 5, self.yp + 2], [self.xp + 5, self.yp + (self.size_p - 2)], 5)
            pygame.draw.line(window, (0, 0, 0), [self.xp + 5, self.yp + 2], [self.xp + (self.size_p - 2), self.yp + (self.size_p / 2)], 5)
            pygame.draw.line(window, (0, 0, 0), [self.xp + 5, self.yp + (self.size_p - 2)], [self.xp + (self.size_p - 2), self.yp + (self.size_p / 2)], 5)
        else:
            pygame.draw.rect(window, (0, 0, 0), [self.xp + 3, self.yp + 2, (self.size_p / 2) - 5, self.size_p - 5])
            pygame.draw.rect(window, (0, 0, 0), [self.xp + (self.size_p / 2) + 3, self.yp + 2, (self.size_p / 2) - 5, self.size_p - 5])

    def press_buttons(self, pos):
        # проверка нажатие паузи
        if self.xp < pos[0] < self.xp + self.size_p and self.yp < pos[1] < self.yp + self.size_p:
            if self.pause:
                self.pause = False
            else:
                self.pause = True

    def press_filter_buttons(self, pos, filter):
        # проверка фильтров
        number_filter = 0
        for pos_f in self.button_filter_list:
            if self.x + pos_f[0] < pos[0] < self.x + pos_f[0] + self.size_f and \
                    self.y + pos_f[1] < pos[1] < self.y + pos_f[1] + self.size_f:
                return number_filter
            number_filter += 1

        return filter
