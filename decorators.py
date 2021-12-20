"""Decorators"""

from progress.bar import Bar


class ProgressBar:
    bar_list = []

    def __init__(self, text, aim, recursion=False):
        if not recursion:
            self.bar_list.append(ProgressBar(text, aim, recursion=True))
        else:
            self.progress = Bar(text, max=aim)

    def __call__(self, func):
        def add_progress(*args):
            bar = self.bar_list[0]

            result = func(*args)
            bar.progress.next()

            if bar.progress.index == bar.progress.max:
                bar.progress.finish()
                self.bar_list.pop(0)

            return result

        return add_progress


def show_palette():
    import pygame
    from class_block import CBlock

    screen_size = (600, 500)

    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('PALETTE TESTER')
    font = pygame.font.SysFont('Comic Sans MS', 30)

    colorbox = CBlock.colorbox
    colorbox_keys_class = colorbox.keys()
    colorbox_keys = []

    for color in colorbox_keys_class:
        colorbox_keys.append(color)

    done = False
    key = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            elif event.type == pygame.MOUSEBUTTONUP:
                key -= 1
                if key < 0:
                    key = len(colorbox_keys) - 1

        screen.fill(colorbox[colorbox_keys[key]])
        text_surface = font.render(f"{colorbox_keys[key]}", True, (255, 255, 255))
        text_width = text_surface.get_height()
        text_height = text_surface.get_width()

        pygame.draw.rect(screen, (0, 0, 0), (0, screen_size[1] - text_width - 40, screen_size[0], 100))
        screen.blit(text_surface, (screen_size[0]/2 - text_height/2, screen_size[1] - text_width - 20))

        pygame.display.flip()


if __name__ == '__main__':
    show_palette()
