import os
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from funkyfresh.miscellaneous import _package_directory


class _Style:

    def __init__(self,
                 key: str,
                 name: str,
                 font: str,
                 fontsize: int or float,
                 linewidth: int or float,
                 figure_widths: dict[str: float or int],
                 default_figure_size: tuple[float or int, float or int],
                 font_package: str,
                 font_package_options: str = '',
                 custom_colors: list[str] = None):
        """
        Class to hold style parameters and provide methods to create and use
        stylesheets based on those parameters.

        Parameters
        ----------
        key : str
            The shortened name of the style, e.g., 'AGU'.
        name : str
            The full name of the style, e.g., 'American Geophysical Union.'
        font : str
            The style's font name, e.g., 'Times New Roman'.
        fontsize : float
            The style's font size.
        linewidth : float
            The style's line width.
        figure_widths : dict[str: float or int]
            The style's figure widths.
        default_figure_size : tuple[float or int, float or int]
            The default figure size. Probably the smallest of the figure sizes
            with a horizontal/vertical ratio of 1.618 (the golden ratio).
        font_package : str
            The name of the font package to use with LaTeX.
        font_package_options : str
            Any options to pass to LaTeX when using the font package.
        custom_colors : list[str]
            Any custom colors appropriate to the style. For instance, AGU has
            a particular blue they use all over their journal articles, Caltech
            has its unique orange color, etc.
        """
        self._key = key
        self._name = name
        self._font = font
        self._fontsize = fontsize
        self._linewidth = linewidth
        self._figure_widths = figure_widths
        self._default_figure_size = default_figure_size
        self._font_package = font_package
        self._font_package_options = font_package_options
        self._custom_colors = custom_colors

    def __str__(self):
        print_str = f'   Name: {self._name}' + '\n'
        print_str += f'   Font: {self._font}' + '\n'
        print_str += f'   Font size: {self._fontsize}' + '\n'
        print_str += f'   Line width: {self._linewidth}' + '\n'
        print_str += f'   Figure widths:' + '\n'
        for key, val in self._figure_widths.items():
            print_str += f'      {key}: {val} in' + '\n'
        print_str += f'   Default figure size: {self._default_figure_size}'
        if self._custom_colors is not None:
            print_str += '\n'
            print_str += f'   Custom color: {", ".join(self._custom_colors)}'
        return print_str

    def _make_replacements_dictionary(self,
                                      presentation: bool) -> dict[str, str]:
        """
        This method produces a dictionary of strings to be replaced in the
        rcParams template.

        Parameters
        ----------
        presentation : bool
            If `True`, fonts are set to the sans-serif font 'Fira Sans'.

        Returns
        -------
        replacements : dict[str, str]
            The dictionary containing keys (to be replaced) and values (their
            replacements).
        """
        if presentation:
            fontpackage = (r'\usepackage{fontspec}'
                           r'\setmainfont{Fira Sans}[Scale=0.93]'
                           r'\setsansfont{Fira Sans}[Scale=0.93]'
                           r'\usepackage{unicode-math}'
                           r'\setmathfont{Fira Math}[Scale=0.93]')
            plt.switch_backend('pgf')
        else:
            fontpackage = (
                rf'\usepackage[{{{self._font_package_options}}}]'
                rf'{{{self._font_package}}}')
        figsize = ', '.join(np.array(self._default_figure_size).astype(str))
        replacements = {
            '[linewidth]': f'{self._linewidth}',
            '[2*linewidth]': f'{2*self._linewidth}',
            '[fontsize]': f'{self._fontsize}',
            '[figsize]': figsize,
            '[fontpackage]': fontpackage,
        }
        return replacements

    def _make_stylesheet(self, presentation: bool) -> Path:
        """
        This method generates a style-specific style sheet.

        Parameters
        ----------
        presentation : bool
            If `True`, fonts are set to the sans-serif font 'Fira Sans'.

        Returns
        -------
        outfile : Path
            The path to the temporary style sheet.
        """
        default_style = open(Path(_package_directory, 'anc',
                                  'template.mplstyle'), 'r').read()
        replacements = self._make_replacements_dictionary(presentation)
        for key, val in replacements.items():
            default_style = default_style.replace(key, val)
        outfile = Path(_package_directory, 'anc', 'temporary.mplstyle')
        if outfile.exists():
            os.remove(outfile)
        with open(outfile, 'w') as file:
            file.write(default_style)
        return outfile

    def set_style(self,
                  silent: bool = False,
                  presentation: bool = False) -> None:
        """
        This method sets the Matplotlib rcParams.

        Parameters
        ----------
        silent : bool
            Whether or not to print out information about the style and its
            parameters.
        presentation : bool
            If `True`, fonts are set to the sans-serif font 'Fira Sans'.

        Returns
        -------
        None
        """
        stylesheet = self._make_stylesheet(presentation=presentation)
        if not silent:
            print('Loading FunkyFresh style...')
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=UserWarning)
            plt.style.use(stylesheet)
        if not silent:
            print(self.__str__())
        os.remove(stylesheet)


"""Define all the styles here."""
styles: dict[str, _Style] = {
    'A&A': _Style(
        key='A&A',
        name='Astronomy & Astrophysics',
        font='Times New Roman',
        fontsize=9,
        linewidth=0.5,
        figure_widths={'column': 3.543, 'page': 7.283},
        default_figure_size=(3.543, 2.190),
        font_package='stix',
        custom_colors=['aa_blue']),
    'AAS': _Style(
        key='AAS',
        name='American Astronomical Society',
        font='Times New Roman',
        fontsize=8,
        linewidth=0.397,
        figure_widths={'column': 3.5, 'page': 7.3},
        font_package='stix',
        default_figure_size=(3.5, 2.163)),
    'AGU': _Style(
        key='AGU',
        name='American Geophysical Union',
        font='Times New Roman',
        fontsize=8,
        linewidth=0.5,
        figure_widths={'column': 3.5, 'text': 5.6, 'page': 7.5},
        default_figure_size=(5.6, 3.461),
        font_package='stix',
        custom_colors=['agu_blue']),
    'Elsevier': _Style(
        key='Elsevier',
        name='Elsevier (Icarus)',
        font='Charis SIL',
        fontsize=8,
        linewidth=0.249,
        figure_widths={'column': 3.484, 'page': 7.2295},
        font_package='mathdesign',
        font_package_options='bitstream-charter',
        default_figure_size=(3.484, 2.153)),
    'MNRAS': _Style(
        key='MNRAS',
        name='Monthly Notices of the Royal Astronomical Society',
        font='Times New Roman',
        fontsize=8,
        linewidth=0.5,
        figure_widths={'column': 3.4, 'page': 7.05},
        default_figure_size=(3.4, 2.101),
        font_package='stix',
        custom_colors=['mnras_lavender']),
    'Caltech Thesis': _Style(
        key='Caltech Thesis',
        name='Caltech Thesis',
        font='Times New Roman',
        fontsize=12,
        linewidth=0.4,
        figure_widths={'text': 5.5},
        default_figure_size=(5.5, 3.399),
        font_package='stix',
        custom_colors=['caltech_orange']),
    'Caltech Thesis v2': _Style(
        key='Caltech Thesis v2',
        name='Caltech Thesis v2',
        font='STIX Two',
        fontsize=12,
        linewidth=0.4,
        figure_widths={'text': 5.5},
        default_figure_size=(5.5, 3.399),
        font_package='stix2',
        custom_colors=['caltech_orange']),
    'Whitepaper': _Style(
        key='Whitepaper',
        name='Personal LaTeX Whitepaper',
        font='STIX Two',
        fontsize=10,
        linewidth=0.4,
        figure_widths={'twocolumn_single': 3.1875,
                       'twocolumn_double': 6.514,
                       'onecolumn': 4.792},
        font_package='stix2',
        default_figure_size=(4.792, 2.962))
}
