import os
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import matplotlib

from funkyfresh.miscellaneous import _package_directory


# store default backend name
default_backend = matplotlib.get_backend()


class _Style:

    def __init__(self,
                 key: str,
                 name: str,
                 font: str,
                 fontpackage: str,
                 fontsize: int or float,
                 linewidth: int or float,
                 figure_widths: dict[str: float or int],
                 default_figure_size: tuple[float or int, float or int],
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
        fontpackage : str
            The LaTeX package string for the desired font.
        fontsize : float
            The style's font size.
        linewidth : float
            The style's line width.
        figure_widths : dict[str: float or int]
            The style's figure widths.
        default_figure_size : tuple[float or int, float or int]
            The default figure size. Probably the smallest of the figure sizes
            with a horizontal/vertical ratio of 1.618 (the golden ratio).
        custom_colors : list[str]
            Any custom colors appropriate to the style. For instance, AGU has
            a particular blue they use all over their journal articles, Caltech
            has its unique orange color, etc.
        """
        self._key = key
        self._name = name
        self._font = font
        self._fontpackage = fontpackage
        self._fontsize = fontsize
        self._linewidth = linewidth
        self._figure_widths = figure_widths
        self._default_figure_size = default_figure_size
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

    def _get_preamble(self,
                      fontpackage: str,
                      presentation: bool) -> str:
        path = Path(_package_directory, 'anc', 'latex_preambles')
        common_preamble = Path(path, 'common_preamble.tex')
        preamble = open(common_preamble, 'r').read()
        if presentation:
            font_preamble = Path(path, 'helvetica_preamble.tex')
        else:
            filename = f'{self._font.replace(" ", "").lower()}_preamble.tex'
            font_preamble = Path(path, filename)
        preamble += fontpackage
        preamble += open(font_preamble, 'r').read()
        return preamble.replace('\n', '')

    def _make_replacements_dictionary(self,
                                      fontpackage: str,
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
        replacements = {}

        figsize = ', '.join(np.array(self._default_figure_size).astype(str))
        replacements['[linewidth]'] = f'{self._linewidth}'
        replacements['[2*linewidth]'] = f'{2*self._linewidth}'
        replacements['[fontsize]'] = f'{self._fontsize}'
        replacements['[figsize]'] = figsize
        replacements['[preamble]'] = self._get_preamble(fontpackage,
                                                        presentation)
        if presentation:
            replacements['[fontfamily]'] = 'sans-serif'
        else:
            replacements['[fontfamily]'] = 'serif'
        return replacements

    def _make_stylesheet(self,
                         fontpackage: str,
                         presentation: bool) -> Path:
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
        replacements = self._make_replacements_dictionary(fontpackage,
                                                          presentation)
        for key, val in replacements.items():
            default_style = default_style.replace(key, val)
        outfile = Path(_package_directory, 'anc', 'temporary.mplstyle')
        if outfile.exists():
            os.remove(outfile)
        with open(outfile, 'w') as file:
            file.write(default_style)
        return outfile

    def set_style(self,
                  fontsize: int | float = None,
                  fontpackage: str = None,
                  presentation: bool = False,
                  silent: bool = False) -> None:
        r"""
        This method sets the Matplotlib rcParams.

        Parameters
        ----------
        fontsize : int or float, optional
            Set the fontsize if you want to override the default.
        fontpackage : str, optional
            Set the LaTeX font package if you want to override the default. For
            example, to specify the STIX fonts, you would pass `
            r'\usepackage{stix}'`.
        silent : bool
            Whether or not to print out information about the style and its
            parameters.
        presentation : bool
            If `True`, fonts are set to the sans-serif font 'Fira Sans'.

        Returns
        -------
        None
            None.
        """
        if fontsize is not None:
            self._fontsize = fontsize
        stylesheet = self._make_stylesheet(fontpackage=fontpackage,
                                           presentation=presentation)
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
        fontpackage=r'\usepackage{txfonts}',
        fontsize=9,
        linewidth=0.5,
        figure_widths={'column': 3.543, 'page': 7.283},
        default_figure_size=(3.543, 2.190),
        custom_colors=['aa_blue']),
    'AAS': _Style(
        key='AAS',
        name='American Astronomical Society',
        font='Times New Roman',
        fontpackage=r'\usepackage{txfonts}',
        fontsize=8,
        linewidth=0.397,
        figure_widths={'column': 3.5, 'page': 7.3},
        default_figure_size=(3.5, 2.163)),
    'AGU': _Style(
        key='AGU',
        name='American Geophysical Union',
        font='Times New Roman',
        fontpackage=r'\usepackage{txfonts}',
        fontsize=8,
        linewidth=0.5,
        figure_widths={'column': 3.5, 'text': 5.6, 'page': 7.5},
        default_figure_size=(5.6, 3.461),
        custom_colors=['agu_blue']),
    'Caltech Thesis': _Style(
        key='Caltech Thesis',
        name='Caltech Thesis',
        font='Times New Roman',
        fontpackage=r'\usepackage{txfonts}',
        fontsize=12,
        linewidth=0.4,
        figure_widths={'text': 6},
        default_figure_size=(6, 3.71),
        custom_colors=['caltech_orange']),
    'LaTeX Default': _Style(
        key='LaTeX Default',
        name='LaTeX Default',
        font='Computer Modern',
        fontpackage=r'\usepackage{lmodern}',
        fontsize=10,
        linewidth=0.4,
        figure_widths={'text': 4.79},
        default_figure_size=(4.79, 4.79/1.618)),
    'Elsevier': _Style(
        key='Elsevier',
        name='Elsevier (Icarus)',
        font='Charter',
        fontpackage=r'\usepackage[bitstream-charter]{mathdesign}',
        fontsize=8,
        linewidth=0.249,
        figure_widths={'column': 3.484, 'page': 7.2295},
        default_figure_size=(3.484, 2.153)),
    'MNRAS': _Style(
        key='MNRAS',
        name='Monthly Notices of the Royal Astronomical Society',
        font='Times New Roman',
        fontpackage=r'\usepackage{txfonts}',
        fontsize=8,
        linewidth=0.5,
        figure_widths={'column': 3.4, 'page': 7.05},
        default_figure_size=(3.4, 2.101),
        custom_colors=['mnras_lavender']),
    'Whitepaper': _Style(
        key='Whitepaper',
        name='Personal LaTeX Whitepaper',
        font='STIX Two',
        fontpackage=r'\usepackage{stix2}',
        fontsize=10,
        linewidth=0.4,
        figure_widths={'twocolumn_single': 3.1875,
                       'twocolumn_double': 6.514,
                       'onecolumn': 4.792},
        default_figure_size=(4.792, 2.962))
}
