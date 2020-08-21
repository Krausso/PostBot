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
    REDIS_HOST = config["REDIS_HOST"]
    REDIS_PASS = config["REDIS_PASS"]
    REDIS_PORT = config["REDIS_PORT"]
