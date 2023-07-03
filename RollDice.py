import random


class Dice:
    def Roll(self):
        l = random.choices([1, 2, 3, 4, 5, 6], k=2)
        return tuple(l)


dice = Dice()
print(dice.Roll())