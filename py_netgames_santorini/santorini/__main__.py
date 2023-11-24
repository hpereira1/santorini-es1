import logging
from santorini.game_logic.AtorJogador import AtorJogador


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("__main__.py").info("Project has run")
    AtorJogador()


