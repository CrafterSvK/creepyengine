from random import randint
import World


class Main:
    def game(self):
        world = World.World()

        number_tries = 1
        tries = 0
        while number_tries > tries:
            x = randint(1, 1000)
            y = randint(1, 1000)
            print(world.generate_tile(x, y))
            tries = tries + 1

main = Main()
main.game()
