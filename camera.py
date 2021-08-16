
class Camera(object):

    def __init__(self, x, y, length, height):
        self.x = x  # координаты камеры
        self.y = y
        self.length = length  # длина и высота камеры
        self.height = height
        self.zoom = 1

    def move_right(self, intensity):
        self.x += intensity

    def move_left(self, intensity):
        self.x -= intensity

    def move_up(self, intensity):
        self.y -= intensity

    def move_down(self, intensity):
        self.y += intensity

    def zoom_in(self):
        if self.length > 1 and self.height > 1:
            new_length_cam = self.length / 1.2
            new_height_cam = self.height / 1.2
            self.x += (self.length - new_length_cam) / 2
            self.y += (self.height - new_height_cam) / 2
            self.length = new_length_cam
            self.height = new_height_cam

    def zoom_out(self):
        new_length_cam = self.length * 1.2
        new_height_cam = self.height * 1.2
        self.x -= (new_length_cam - self.length) / 2
        self.y -= (new_height_cam - self.height) / 2
        self.length = new_length_cam
        self.height = new_height_cam

    def in_vision(self, block_x, block_y, block_size):
        if block_x + block_size > self.x and block_x < self.x + self.length \
                and block_y + block_size > self.y and block_y < self.y + self.height:
            return True
        else:
            return False

    def get_block_in_window(self, block_x, block_y, block_size, window_x, window_y):
        # локальные координаты
        x_loc = block_x - self.x
        y_loc = block_y - self.y

        # координаты блока на window
        x = (x_loc / self.length) * window_x
        y = (y_loc / self.height) * window_y

        size = (block_size / self.length) * window_x

        return x, y, size
