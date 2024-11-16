from src import src
from src.config import _Config


def run():
    config = _Config()
    src.run(host=config.host(), port=config.port())


if __name__ == "__main__":
    run()
