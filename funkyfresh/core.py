from pathlib import Path

import matplotlib.pyplot as plt


personal_color_dict = {
    'red': '#D62728',
    'orange': '#FF7F0E',
    'yellow': '#FDB813',
    'green': '#2CA02C',
    'blue': '#0079C1',
    'violet': '#9467BD',
    'cyan': '#17BECF',
    'magenta': '#D64ECF',
    'brown': '#8C564B',
    'darkgrey': '#3F3F3F',
    'grey': '#7F7F7F',
    'lightgrey': '#BFBFBF',
    'black': '#000000',
    'white': '#FFFFFF',
}

# Caltech color dictionaries from https://identity.caltech.edu/colors
caltech_orange = '#FF6C0C'  # Pantone PMS 1585c Orange
caltech_neutral_colors = {
    'PMS Cool Gray 9': '#76777B',
    'PMS Cool Gray 3c': '#C8C8C8',
    'PMS 414': '#AAA99F',
    'PMS 5497c': '#849895',
    'PMS 7494c': '#9DAE88',
    'PMS 451c': '#C7B784',
    'PMS 7403c': '#F1D384',
}
caltech_deep_colors = {
    'PMS 548c': '#003B4C',
    'PMS 3292c': '#005851',
    'PMS 668c': '#644B78',
    'PMS 195c': '#7A303F',
    'PMS 186c': '#CF0A2C',
}
caltech_bright_colors = {
    'PMS 299c': '#00A1DF',
    'PMS 7473c': '#1E988A',
    'PMS 7489c': '#73A950',
    'PMS 7408c': '#F9BE00',
    'PMS 605c': '#E2CC00',
    'PMS 1915c': '#F54D80',
}


def _set_style(name: str):
    try:
        plt.style.use(
            Path(Path(__file__).resolve().parent,
                 f'style_sheets/{name}.mplstyle'))
    except OSError:
        raise Exception("Sorry, either you mispelled the journal name or "
                        "the style doesn's exist yet!")


class AAS:

    def __init__(self):

        _set_style('AAS')

    @property
    def column_width(self) -> float:
        return 3.5

    @property
    def page_width(self) -> float:
        return 7.3


class AGU:

    def __init__(self):
        _set_style('AAS')

    @property
    def column_width(self) -> float:
        return 3.5

    @property
    def text_width(self) -> float:
        return 5.6

    @property
    def page_width(self) -> float:
        return 7.5

    @property
    def blue(self) -> str:
        return '#004174'


class PersonalWhitepaper:

    def __init__(self):
        _set_style('personal_whitepaper')

    @property
    def page_width(self) -> float:
        return 4.7917

    @property
    def colors(self) -> dict:
        return personal_color_dict


class CaltechThesis:

    def __init__(self):
        _set_style('caltech_thesis')

    @property
    def caltech_orange(self) -> str:
        return caltech_orange

    @property
    def caltech_neutral_colors(self) -> dict:
        return caltech_neutral_colors

    @property
    def caltech_deep_colors(self) -> dict:
        return caltech_deep_colors

    @property
    def caltech_bright_colors(self) -> dict:
        return caltech_bright_colors

    @property
    def text_width(self) -> float:
        return 5.5206


def set_aas_style():
    """
    Sets graphics style to match American Astronomical Society journals.
    Provides two different graphics width options: column (3.5 inches) and
    full-page (7.3 inches).

    Properties
    ----------
    column_width : float
        Width for a column-width figure in inches.
    page_width : float
        Width for a page-width figure in inches.

    Examples
    --------
    Get the column-width in inches:
    >>> style = set_aas_style()
    >>> style.column_width
    3.5

    Get the page-width in inches:
    >>> style = set_aas_style()
    >>> style.page_width
    7.3
    """
    return AAS()


def set_agu_style():
    """
    Sets graphics style to match American Geophysical Union (JGR) journals.
    Provides three different graphics width options: column (3.5 inches),
    full-text (5.4 inches) and full-page (7.3 inches). Also provides the blue
    color used in lines and section labels. Default figure size width is
    4.7917 pt.

    Properties
    ----------
    column_width : float
        Width for a column-width figure in inches.
    text_width : float
        Width for a text-block-width figure in inches.
    page_width : float
        Width for a page-width figure in inches.
    blue : str
        Hexadecimal string for AGU blue color #004174.

    Examples
    --------
    Get the column-width in inches:
    >>> style = set_agu_style()
    >>> style.column_width
    3.5

    Get the text-width in inches:
    >>> style = set_agu_style()
    >>> style.text_width
    5.6

    Get the page-width in inches:
    >>> style = set_agu_style()
    >>> style.page_width
    7.5

    Get the AGU blue color as a hexadecimal string
    >>> style = set_agu_style()
    >>> style.blue
    '#004174'
    """
    return AGU()


def set_personal_whitepaper_style():
    """
    Sets graphics style to match the default 10-point LaTeX article class I use
    for school papers, reports, etc. Also has a custom color dictionary.

    Properties
    ----------
    page_width : float
        LaTeX 10-pt article class default text width.
    colors : dict
        My custom color dictionary.

    Examples
    --------
    Get the column-width in inches:
    >>> style = set_personal_whitepaper_style()
    >>> style.page_width
    4.7917

    Get the blue color from the custom color dictionary:
    >>> style = set_personal_whitepaper_style()
    >>> style.colors['blue']
    '#0079C1'

    Get the available colors from the custom color dictionary:
    >>> style = set_personal_whitepaper_style()
    >>> style.colors.keys()
    dict_keys(['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'cyan', 'magenta', 'brown', 'darkgrey', 'grey', 'lightgrey', 'black', 'white'])
    """

    return PersonalWhitepaper()


def set_caltech_thesis_style():
    """
    Sets graphics style to match the Caltech LaTeX thesis class along with
    color dictionaries taken from the Caltech Identity Toolkit
    (https://identity.caltech.edu).

    Note: I have changed the font from Times New Roman to STIX2. It's just
    better. You can do this, too, by importing the stix2 package in your LaTeX
    preamble.

    Properties
    ----------
    caltech_orange : str
        Pantone MS 1585c Orange.
    caltech_neutral_colors : dict
        Caltech's neutral color palette complements the Caltech orange and
        should be used for projects with a more traditional, serious tone.
    caltech_deep_colors : dict
        Caltech's deep color palette adds contrast to the Caltech orange as
        well as the neutral palette, and may be used to provide more depth and
        texture to communications materials.
    caltech_bright_colors : dict
        Caltech's bright color palette provides an opportunity to adjust the
        temper of a piece from subtle to bold. These colors should be used as
        accents to the primary, neutral, and deep colors, and carefully
        selected based on what is appropriate to the tone of the piece.
    text_width : float
        Width for a text-block-width figure in inches.

    Examples
    --------
    Get the ubiquitous Caltech orange color:
    >>> style = set_caltech_thesis_style()
    >>> style.caltech_orange
    '#FF6C0C'

    Get the dark grey color from the Caltech netural colors dictionary:
    >>> style = set_caltech_thesis_style()
    >>> style.caltech_neutral_colors['PMS Cool Gray 9']
    '#76777B'

    Get the available colors from the Caltech neutral colors dictionary:
    >>> style = set_caltech_thesis_style()
    >>> style.caltech_neutral_colors.keys()
    dict_keys(['PMS Cool Gray 9', 'PMS Cool Grey 3c', 'PMS 414', 'PMS 5497c', 'PMS 7494c', 'PMS 451c', 'PMS 7403c'])

    Get the available colors from the Caltech deep colors dictionary:
    >>> style = set_caltech_thesis_style()
    >>> style.caltech_deep_colors.keys()
    dict_keys(['PMS 548c', 'PMS 3292c', 'PMS 668c', 'PMS 195c', 'PMS 186c'])

    Get the available colors from the Caltech bright colors dictionary:
    >>> style = set_caltech_thesis_style()
    >>> style.caltech_bright_colors.keys()
    dict_keys(['PMS 299c', 'PMS 7473c', 'PMS 7489c', 'PMS 7408c', 'PMS 605c', 'PMS 1915c'])
    """

    return CaltechThesis()


if __name__ == "__main__":
    style = set_caltech_thesis_style()
    print(style.caltech_orange)
