
class Simulation(object):

    def __init__(self):
        self.run = True
        self.filter = 0
        self.filter_list = ["elevation map", "waves map color", "waves map wb", "perlin noise", "temperature air"]
        self.camera = None
        self.word = None

    def create_word_with_perlin_noise(self):
        pass

    def draw_menu(self):
        pass

    def input_mouse(self):

        for e in pygame.event.get():  # проверка нажатий
            if e.type == pygame.QUIT:
                self.run = False

            if e.type == pygame.MOUSEBUTTONUP:
                if e.button == 1:
                    panel.press_buttons(e.pos)
                    self.filter = panel.press_filter_buttons(e.pos, filter)

            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.button == 4:
                    if length_cam > 1 and height_cam > 1:

                if e.button == 5:


    def input_keyboard(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:

        if keys[pygame.K_a]:

        if keys[pygame.K_w]:

        if keys[pygame.K_s]:

        if keys[pygame.K_r]:

        if keys[pygame.K_f]:

        if keys[pygame.K_g]:


