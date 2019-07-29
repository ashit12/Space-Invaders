class alien:
    alienlist = []

    def __init__(self, posx, posy, time, freeze, freeze_time):
        self.alien_time = time
        self.alien_posx = posx
        self.alien_posy = posy
        self.freeze = freeze
        self.freeze_time = freeze_time
