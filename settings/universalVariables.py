import arcade
import json

with open("settings/settings.json") as f:
    settings_data = json.load(f)

WINDOW_WIDTH = settings_data["window"]["width"]
WINDOW_HEIGHT = settings_data["window"]["height"]
WINDOW_TITLE = "Tutorial"

key_bindings = settings_data["keybindings"]