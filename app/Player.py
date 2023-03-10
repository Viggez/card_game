

class Player:

    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self):
        return self.hand.pop()

    def play_card(self):
        if len(self.hand) == 0:
            return None
        return self.hand.pop(0)

    def gh(self):
        return self.hand

    def clear_hand(self):
        self.hand = []

    def __str__(self):
        return f'{self.name} has {len(self.hand)} cards'
