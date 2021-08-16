
class Simulation(object):

    def __init__(self):
        self.run = True
        self.filter = 0
        self.filter_list = ["elevation map", "waves map color", "waves map wb", "perlin noise", "temperature air"]
        self.camera = None

    def draw_menu(self):
        pass

    def input(self):
        for e in pygame.event.get():  # проверка нажатий
            if e.type == pygame.QUIT:
                self.run = False
            if e.type == pygame.KEYUP:
                if e.key == pygame.K_g:
                    self.filter += 1
                    if self.filter == len(filter_list):
                        self.filter = 0

            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    panel.press_buttons(e.pos)
                    self.filter = panel.press_filter_buttons(e.pos, filter)

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:
                    if length_cam > 1 and height_cam > 1:
                        new_length_cam = length_cam / 1.2
                        new_height_cam = height_cam / 1.2
                        x_cam += (length_cam - new_length_cam) / 2
                        y_cam += (height_cam - new_height_cam) / 2
                        length_cam = new_length_cam
                        height_cam = new_height_cam
                if e.button == 5:
                    new_length_cam = length_cam * 1.2
                    new_height_cam = height_cam * 1.2
                    x_cam -= (new_length_cam - length_cam) / 2
                    y_cam -= (new_height_cam - height_cam) / 2
                    length_cam = new_length_cam
                    height_cam = new_height_cam
            keys = pygame.key.get_pressed()
            if keys[pygame.K_d]:
                x_cam += 10
            if keys[pygame.K_a]:
                x_cam -= 10
            if keys[pygame.K_w]:
                y_cam -= 10
            if keys[pygame.K_s]:
                y_cam += 10
            if keys[pygame.K_r]:
                new_length_cam = length_cam * 1.2
                new_height_cam = height_cam * 1.2
                x_cam -= (new_length_cam - length_cam) / 2
                y_cam -= (new_height_cam - height_cam) / 2
                length_cam = new_length_cam
                height_cam = new_height_cam
            if keys[pygame.K_f]:
                if length_cam > 1 and height_cam > 1:
                    new_length_cam = length_cam / 1.2
                    new_height_cam = height_cam / 1.2
                    x_cam += (length_cam - new_length_cam) / 2
                    y_cam += (height_cam - new_height_cam) / 2
                    length_cam = new_length_cam
                    height_cam = new_height_cam
