from pathlib import Path

from matplotlib_inline.backend_inline import set_matplotlib_formats

from funkyfresh.miscellaneous import _package_directory
from funkyfresh.styles import styles


def get_font_location() -> str:
    """
    Return the absolute path to the location of fonts included with your
    installation of FunkyFresh.

    Parameters
    ----------
    None.

    Returns
    -------
    location : str
        The absolute path to the location of fonts included with your
        installation of FunkyFresh.
    """
    location = str(Path(_package_directory, 'anc', 'fonts'))
    return location


def get_available_styles() -> list[str]:
    """
    Return a list of the available style names.

    Parameters
    ----------
    None.

    Returns
    -------
    style_names : list[str]
        A list of the available style names.
    """
    style_names = list(styles.keys())
    return style_names


def set_style(name: str,
              silent: bool = False,
              presentation: bool = False) -> None:
    """
    Change Matplotlib runtime configuration parameters (rcParams) to match a
    journal style.

    Parameters
    ----------
    name : str
        The (abbreviated) name of the style. You can get the available styles
        using `get_available_styles()`.
    silent : bool
        Whether or not to print out information about the style and its
        parameters.
    presentation : bool
        If `True`, fonts are set to the sans-serif font 'Fira Sans'.

    Returns
    -------
    None.
    """
    set_matplotlib_formats('retina')
    style = styles[name]
    style.set_style(silent=silent, presentation=presentation)
