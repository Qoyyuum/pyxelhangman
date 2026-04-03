import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pyxelhangman.game import Game


def main():
    Game()


if __name__ == "__main__":
    main()
