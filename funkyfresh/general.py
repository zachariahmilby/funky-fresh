import matplotlib.pyplot as plt
from matplotlib_inline.backend_inline import set_matplotlib_formats

from funkyfresh.styles import styles


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
              fontsize: int | float = None,
              fontpackage: str = None,
              presentation: bool = False,
              silent: bool = False) -> None:
    r"""
    Change Matplotlib runtime configuration parameters (rcParams) to match a
    journal style.

    Parameters
    ----------
    name : str
        The (abbreviated) name of the style. You can get the available styles
        using `get_available_styles()`.
    fontsize : int or float, optional
        Set the fontsize if you want to override the default.
    fontpackage : str, optional
        Set the LaTeX font package if you want to override the default. For
        example, to specify the STIX fonts, you would pass `
        r'\usepackage{stix}'`.
    presentation : bool
        If `True`, fonts are set to the sans-serif font 'Fira Sans'.
    silent : bool
        Whether or not to print out information about the style and its
        parameters.

    Returns
    -------
    None
        None.
    """
    set_matplotlib_formats('retina')
    plt.style.use('default')  # reset rcParams before applying new settings
    style = styles[name]
    style.set_style(fontsize=fontsize,
                    fontpackage=fontpackage,
                    presentation=presentation,
                    silent=silent)
