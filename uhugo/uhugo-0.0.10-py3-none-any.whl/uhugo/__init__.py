__version__ = "0.0.10"

from pathlib import Path

# Creates a .uhugo folder in user folder
if not Path.home().joinpath(".uhugo").is_dir():
    Path.home().joinpath(".uhugo").mkdir(exist_ok=True)
