class missile(object):
    missilelist = []

    def __init__(self, posx, posy):
        self.position_x = posx
        self.position_y = posy


class missile1(missile):
    def __init__(self, start, status, posx, posy):
        self.missile_start_time = start
        self.status = 0
        self.typeo = 1
        super(missile1, self).__init__(posx, posy)

    def update(self, time):
        self.missile_start_time = time


class missile2(missile):
    def __init__(self, start, status, posx, posy):
        self.missile_start_time = start
        self.status = 0
        self.typeo = 2
        super(missile2, self).__init__(posx, posy)

    def update(self, time):
        self.missile_start_time = time
