import yaml
from sys import exit
from pathlib import Path

MAIN_DIR = Path(__file__).parent.parent

try:
    config = yaml.load(
        open(f'{MAIN_DIR}/config.yaml', 'r', encoding='utf-8'),
        Loader=yaml.Loader
    )
except FileNotFoundError:
    print("config.yaml: file does not exit")
    exit()
else:
    BOT_TOKEN = config["BOT_TOKEN"]
    DB_HOST = config["DB_HOST"]
    DB_USER = config["DB_USER"]
    DB_PASS = config["DB_PASS"]
    DB_PORT = config["DB_PORT"]
