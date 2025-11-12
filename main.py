from game.core import BaseGame, logger
from game.states import Menu, Night1

def main():
    game = BaseGame()
    states = [
        Night1(game), Menu(game)
    ]
    for s in states:
        game.add_state(s)
    game.run()

if __name__ == "__main__":
    main()