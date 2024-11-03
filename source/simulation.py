import os

from source.constants import *

import eevolve


class Simulation:
    def __init__(self) -> None:
        self._game = eevolve.Game(DISPLAY_SIZE, SCREEN_SIZE, WINDOW_NAME,
                                  os.path.join(ASSETS_PATH, "bg.png"), SECTORS_NUMBER)

    def run(self) -> None:
        self._game.run()
