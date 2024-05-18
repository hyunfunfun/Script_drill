class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0
    def inHand(self):
        return self.N
    def addCard(self,c):
        self.cards.append(c)
        self.N += 1
    def reset(self):
        self.N = 0
        self.cards.clear()
    def value(self):
        result = 0
        ain = False
        for c in self.cards:
            v = c.getValue()
            if v == 1:
                v = 11
                ain = True
            result += v

        if result > 21 and ain:
            result -= 10

        return result