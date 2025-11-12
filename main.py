from game.core import BaseGame, logger
from game.states import (
    States,
    Menu,
    # SplashScreen,
    # PauseMenu,
    # Ending,
    # Credits,
    Night1,
    # Night2,
    # Night3,
    # Night4,
    # Night5,
    # Night6,
    # Night7,
    # Night8,
    # Night9,
)


def main():
    logger.info("=== Spin of Light - Starting ===")

    # create game
    game = BaseGame()
    
    # defines states
    states = [
        # SplashScreen(game),
        Menu(game),
        Night1(game),
        # Night2(game),
        # Night3(game),
        # Night4(game),
        # Night5(game),
        # Night6(game),
        # Night7(game),
        # Night8(game),
        # Night9(game),
        # PauseMenu(game),
        # Ending(game),
        # Credits(game),
    ]
    
    # add to game all states
    for state in states:
        game.add_state(state)
    
    # set starting state
    game.set_state_by_name(States.MENU)
    
    # run the game loop
    try:
        game.run()
    except Exception as e:
        logger.exception(f"Fatal error: {e}")
    finally:
        logger.info("=== Spin of Light - Ended ===")


if __name__ == "__main__":
    main()