import logging
from game_logic.AtorJogador import Atorjogador

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("__main__.py").info("Project has run")
    Atorjogador()


