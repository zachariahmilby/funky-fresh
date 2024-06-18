from pathlib import Path

"""Absolute directory of package installation."""
_package_directory = Path(__file__).resolve().parent

"""Absolute directory of included fonts."""
_font_directory = Path(_package_directory, 'anc', 'fonts')
