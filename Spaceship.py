class ship(object):
    def Moveleft(self, pos):
        if(pos >= 100):
            pos -= 100
        return pos

    def Moveright(self, pos):
        if(pos <= 600):
            pos += 100
        return pos
