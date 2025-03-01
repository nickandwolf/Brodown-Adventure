import arcade
import json
import math

with open("settings/settings.json") as f:
    settings_data = json.load(f)

GAME_WIDTH = 800
GAME_HEIGHT = 600

WINDOW_WIDTH = settings_data["window"]["width"]
WINDOW_HEIGHT = settings_data["window"]["height"]
WINDOW_TITLE = "Tutorial"
WINDOW_FULLSCREEN = settings_data["window"]["fullscreen"]
WINDOW_FPS = 1/settings_data["window"]["fps"]

MUSIC_VOLUME = settings_data["sound"]["music_volume"]
SOUND_VOLUME = settings_data["sound"]["sound_volume"]

key_bindings = settings_data["keybindings"]