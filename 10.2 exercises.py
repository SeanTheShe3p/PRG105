import random
#
# 10.2
#


class Dice:
    def __init__(self):
        self.side_up = '1'

    def roll(self):
        die = random.randint(1, 6)
        if die == 1:
            self.side_up = '1'
        elif die == 2:
            self.side_up = '2'
        elif die == 3:
            self.side_up = '3'
        elif die == 4:
            self.side_up = '4'
        elif die == 5:
            self.side_up = '5'
        elif die == 6:
            self.side_up = '6'

    def get_side_up(self):
        return self.side_up


def main():
    my_dice = Dice()
    my_dice_two = Dice()
    print('the roll of the first die was ', my_dice.get_side_up())
    print('the roll of the second die was ', my_dice_two.get_side_up())
    print('\n\nI am tossing the coins..\n\n')
    my_dice.roll()
    my_dice_two.roll()
    print('the roll for die one is now ', my_dice.get_side_up())
    print('the roll for die two is now ', my_dice_two.get_side_up())


main()
