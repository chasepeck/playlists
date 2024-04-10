from sys import argv
from pathlib import Path
import subprocess
import json

MUSIC = Path.home() / "iCloud" / "Workspace" / "Music" / "Library"
PLAYER = "cog"

with open(argv[1], "r") as file:
	playlist = json.load(file)

for i in playlist:
	subprocess.run(["open", str(MUSIC.joinpath(i)), "-a", PLAYER])
