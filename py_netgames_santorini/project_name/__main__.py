import logging
from project_name.game_logic.teste2 import App

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("__main__.py").info("Project has run")
    #Add your logic here
App()

