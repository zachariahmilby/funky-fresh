import matplotlib
from funkyfresh.named_styles import _named_styles
from funkyfresh.colors import standard_color_dict

# get named style options
_named_style_options = list(_named_styles.keys())

# these are universal properties I want to apply to every style
universal_properties = {
    'axes.prop_cycle': matplotlib.cycler('color', ['k']),
    'legend.fancybox': False,
    'legend.edgecolor': 'k',
    'legend.framealpha': 1,
    'savefig.dpi': 600,
    'figure.dpi': 150,
    'pdf.fonttype': 42,
    'ps.fonttype': 42,
}

# get the list of default rcParams for the particular version of Matplotlib
default_rcparams = list(matplotlib.rcParams.keys())


class NamedStyleException(Exception):
    """
    Raised if named style not found.
    """
    pass


class FunkyFresh:

    def __init__(self, highres_inline_plots: bool = False):
        """
        Make your Matplotlib plots both funky and fresh!

        Parameters
        ----------
        highres_inline_plots : bool
            If you are coding in a Jupyter notebook or similar, set this to
            `True` to enable high-resolution inline plots.
        """
        self._colors = standard_color_dict
        self._figure_widths = None
        if highres_inline_plots:
            self._set_highres_inline()

    @staticmethod
    def _set_highres_inline():
        from matplotlib_inline.backend_inline import set_matplotlib_formats
        set_matplotlib_formats('retina')

    def _get_named_style(self, named_style: str, use_latex: bool,
                         latex_font_package: str,
                         latex_font_options: str,
                         additional_latex_packages: str or [str],
                         additional_rcparams: dict):
        if named_style not in _named_style_options:
            raise NamedStyleException(
                f"Named style not found. Available options are: "
                f"{', '.join(_named_style_options)}.")
        else:
            named_style: dict = _named_styles[named_style]
            style = self._make_named_style_dictionary(
                named_style=named_style, use_latex=use_latex,
                latex_font_package=latex_font_package,
                latex_font_options=latex_font_options,
                additional_latex_packages=additional_latex_packages,
                additional_rcparams=additional_rcparams)
            return style, named_style

    @staticmethod
    def _make_font_dictionary(family: str = 'serif',
                              fontsize: int = 10):
        return {
            'font.family': family,
            'font.size': fontsize,
            'axes.titlesize': fontsize,
            'axes.labelsize': fontsize,
            'xtick.labelsize': fontsize,
            'ytick.labelsize': fontsize,
            'legend.fontsize': fontsize,
            'figure.titlesize': fontsize,
            'figure.labelsize': fontsize,
        }

    @staticmethod
    def _make_linewidth_dictionary(linewidth: float = 0.5,
                                   minor_ticks: bool = False):
        dictionary = {
            'lines.linewidth': 2 * linewidth,
            'lines.markeredgewidth': linewidth,
            'patch.linewidth': linewidth,
            'hatch.linewidth': linewidth,
            'boxplot.whiskers': 1.5 * linewidth,
            'boxplot.flierprops.linewidth': 1.5 * linewidth,
            'boxplot.boxprops.linewidth': 1.5 * linewidth,
            'boxplot.whiskerprops.linewidth': 1.5 * linewidth,
            'boxplot.capprops.linewidth': 1.5 * linewidth,
            'boxplot.medianprops.linewidth': 1.5 * linewidth,
            'boxplot.meanprops.linewidth': 1.5 * linewidth,
            'axes.linewidth': linewidth,
            'grid.linewidth': linewidth,
            'xtick.major.width': linewidth,
            'xtick.minor.width': linewidth,
            'ytick.major.width': linewidth,
            'ytick.minor.width': linewidth,
        }
        if minor_ticks:
            dictionary['xtick.minor.visible'] = True
            dictionary['ytick.minor.visible'] = True
        return dictionary

    @staticmethod
    def _make_latex_dictionary(
            preamble: str, font_package: str or None,
            font_options: str or None,
            additional_latex_packages: str or None):
        if font_package is not None:
            if font_options is not None:
                preamble = fr'\usepackage[{font_options}]{{{font_package}}}' \
                           fr'{preamble}'
            else:
                preamble = fr'\usepackage{{{font_package}}}{preamble}'
        if additional_latex_packages is not None:
            preamble += additional_latex_packages
        return {
            'text.usetex': True,
            'text.latex.preamble': preamble,
        }

    @staticmethod
    def _cleanup_dictionary(dictionary: dict):
        missing_keys = [key for key in dictionary.keys()
                        if key not in default_rcparams]
        for key in missing_keys:
            del dictionary[key]

    def _make_named_style_dictionary(self, named_style: dict,
                                     use_latex: bool,
                                     latex_font_package: str,
                                     latex_font_options: str,
                                     additional_latex_packages: str,
                                     additional_rcparams: dict):
        font_dictionary = self._make_font_dictionary(
            family=named_style['fontfamily'], fontsize=named_style['fontsize'])
        linewidth_dictionary = self._make_linewidth_dictionary(
            linewidth=named_style['linewidths'])
        dictionary = {**universal_properties, **font_dictionary,
                      **linewidth_dictionary}
        if use_latex:
            if latex_font_package is not None:
                font_package = latex_font_package
            else:
                font_package = named_style['latex_font_package']
            latex_dictionary = self._make_latex_dictionary(
                preamble=named_style['latex_preamble'],
                font_package=font_package,
                font_options=latex_font_options,
                additional_latex_packages=additional_latex_packages)
            dictionary = {**dictionary, **latex_dictionary}
        if additional_rcparams is not None:
            dictionary = {**dictionary, **additional_rcparams}
        self._cleanup_dictionary(dictionary)
        return dictionary

    def set_named_style(self, named_style: str, use_latex: bool = False,
                        latex_font_package: str = None,
                        latex_font_options: str = None,
                        additional_latex_packages: str = None,
                        additional_rcparams: dict = None):
        """
        Set the Matplotlib runtime configuration to match a named journal
        style.

        Parameters
        ----------
        named_style : str
            The pre-defined style you want to use. For a list of available
            styles, use the method `get_available_styles()`.
        use_latex : bool
            Set to True if you want to use LaTeX to render text in your plots.
            Requires a local LaTeX installation.
        latex_font_package : str
            If you want to set a LaTeX font package other than the default
            Computer Modern, give the package name here. For example, 'stix'
            will result in `\\usepackage{stix}` at the beginning of the LaTeX
            preamble.
        latex_font_options: str (optional)
            Any options you want to pass when loading the LaTeX font package.
        additional_latex_packages : str
            Any additional packages you want loaded. You must explicitly pass
            this as a string with escaped backslashes like
            "\\usepackage[option]{package1}\\usepackage{package2}".
        additional_rcparams : dict
            Any additional runtime configuration parameters you want to change
            in addition to the named style defaults (or overwriting the named
            style defaults). For example, {'font.size': 24} will override the
            font size defined in one of the FunkyFresh named styles and set it
            to 24 pt.

        Returns
        -------
        None.

        Examples
        --------
        Set AAS journals style and get the width of a column-width figure:
        >>> ffs = FunkyFresh()
        >>> ffs.set_named_style('AAS')
        >>> ffs.figure_widths['column']
        3.5

        Set AGU journals style and get the custom blue color:
        >>> ffs = FunkyFresh()
        >>> ffs.set_named_style('AGU')
        >>> ffs.colors['agu_blue']
        '#004174'

        Set A&A journal style and get the (garish) custom blue color:
        >>> ffs = FunkyFresh()
        >>> ffs.set_named_style('A&A')
        >>> ffs.colors['aa_blue']
        '#0000FF'

        Set Caltech Thesis style and get the Caltech orange color:
        >>> ffs = FunkyFresh()
        >>> ffs.set_named_style('Caltech Thesis')
        >>> ffs.colors['caltech_orange']
        '#FF6C0C'

        Set Monthly Notices of the Royal Astronomical Socity style and get the lavender color:
        >>> ffs = FunkyFresh()
        >>> ffs.set_named_style('MNRAS')
        >>> ffs.colors['mnras_lavender']
        '#AEA6CE'
        """
        style, style_params = self._get_named_style(
            named_style=named_style, use_latex=use_latex,
            latex_font_package=latex_font_package,
            latex_font_options=latex_font_options,
            additional_latex_packages=additional_latex_packages,
            additional_rcparams=additional_rcparams)
        self._set_rcparams(style)
        self._figure_widths = style_params['figurewidths']
        if 'colors' in style_params.keys():
            for color_set in style_params['colors']:
                self._colors = {**self._colors, **color_set}

    def named_style_context(self, named_style: str, use_latex: bool = False,
                            latex_font_package: str = None,
                            latex_font_options: str = None,
                            additional_latex_packages: str = None,
                            additional_rcparams: dict = None):
        """
        Temporarily set the Matplotlib runtime configuration to match a named
        journal style using the context manager.

        Parameters
        ----------
        named_style : str
            The pre-defined style you want to use. For a list of available
            styles, use the method `get_available_styles()`.
        use_latex : bool
            Set to True if you want to use LaTeX to render text in your plots.
            Requires a local LaTeX installation.
        latex_font_package : str
            If you want to set a LaTeX font package other than the default
            Computer Modern, give the package name here. For example, 'stix'
            will result in `\\usepackage{stix}` at the beginning of the LaTeX
            preamble.
        latex_font_options: str (optional)
            Any options you want to pass when loading the LaTeX font package.
        additional_latex_packages : str
            Any additional packages you want loaded. You must explicitly pass
            this as a string with escaped backslashes like
            "\\usepackage[option]{package1}\\usepackage{package2}".
        additional_rcparams : dict
            Any additional runtime configuration parameters you want to change
            in addition to the named style defaults (or overwriting the named
            style defaults). For example, {'font.size': 24} will override the
            font size defined in one of the FunkyFresh named styles and set it
            to 24 pt.

        Returns
        -------
        None.
        """
        style, style_params = self._get_named_style(
            named_style=named_style, use_latex=use_latex,
            latex_font_package=latex_font_package,
            latex_font_options=latex_font_options,
            additional_latex_packages=additional_latex_packages,
            additional_rcparams=additional_rcparams)
        return matplotlib.rc_context(rc=style)

    def set_custom_style(self, rcparams: dict = None, use_latex: bool = False,
                         latex_preamble: str = None):
        """
        A convenience function for arbitrarily modifying the runtime
        configuration.

        Parameters
        ----------
        rcparams : str
            Any runtime configuration parameters you want to change.
        use_latex : bool
            Set to True if you want to use LaTeX to render text in your plots.
            Requires a local LaTeX installation.
        latex_preamble : str
            Any LaTeX packages you want loaded. You must explicitly pass
            this as a string with escaped backslashes like
            "\\usepackage[option]{package1}\\usepackage{package2}".

        Returns
        -------
        None.

        Examples
        --------
        Change the default font size:
        >>> import matplotlib
        >>> ffs = FunkyFresh()
        >>> params = {'font.size': 24}
        >>> ffs.set_custom_style(rcparams=params)
        >>> matplotlib.rcParams['font.size']
        24.0

        Use LaTeX rendering and load the STIX2 font with upright integrals:
        >>> import matplotlib
        >>> ffs = FunkyFresh()
        >>> preamble = r'\\usepackage[upint]{stix2}'
        >>> ffs.set_custom_style(use_latex=True, latex_preamble=preamble)
        >>> matplotlib.rcParams['text.latex.preamble']
        '\\\\usepackage[upint]{stix2}'
        """
        if rcparams is None:
            rcparams = {}
        if use_latex:
            latex_dictionary = self._make_latex_dictionary(
                preamble=latex_preamble, font_package=None, font_options=None,
                additional_latex_packages=None)
            rcparams = {**rcparams, **latex_dictionary}
        self._cleanup_dictionary(rcparams)
        self._set_rcparams(rcparams)

    @staticmethod
    def get_available_styles() -> [str]:
        """
        Return a list of available named styles.

        Returns
        -------
        A list of available named styles.

        Examples
        --------
        Get the column-width in inches:
        >>> ffs = FunkyFresh()
        >>> ffs.get_available_styles()
        ['AAS', 'AGU', 'A&A', 'MNRAS', 'Caltech Thesis']
        """
        return _named_style_options

    @staticmethod
    def _set_rcparams(style: dict):
        for key in style.keys():
            matplotlib.rcParams[key] = style[key]

    @property
    def colors(self) -> dict:
        return self._colors

    @property
    def figure_widths(self) -> dict:
        return self._figure_widths
