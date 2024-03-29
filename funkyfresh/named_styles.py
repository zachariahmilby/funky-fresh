from funkyfresh.colors import *


_default_latex_preamble = r'\usepackage{siunitx, amsmath, amssymb, isomath, ' \
                          r'physics}\usepackage[version=4,arrows=pgf]{mhchem}'
siunitx_params = ','.join(['print-unity-mantissa=false',
                           'separate-uncertainty=true',
                           'range-units=single',
                           'list-units=single',
                           'multi-part-units=single',
                           'range-exponents=combine',
                           'group-separator={,}',
                           'group-digits=integer'])
_default_latex_preamble += fr'\sisetup{{{siunitx_params}}}'

# ==================================== #
# American Astsronomical Society Style #
# ==================================== #

_aas = {
    'name': 'American Astronomical Society',
    'fontfamily': 'serif',
    'font': 'Times New Roman',
    'fontsize': 9,
    'linewidths': 0.397,
    'figsize': (3.5, 2.163),
    'latex_font_package': 'stix',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'column': 3.5, 'page': 7.3},
}

# ================================ #
# American Geophysical Union Style #
# ================================ #

_agu = {
    'name': 'American Geophysical Union',
    'fontfamily': 'serif',
    'font': 'Times New Roman',
    'fontsize': 8,
    'linewidths': 0.5,
    'figsize': (5.6, 3.461),
    'latex_font_package': 'stix',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'column': 3.5, 'text': 5.6,
                     'page': 7.5},
    'colors': [{'agu_blue': '#004174'}],
}


# ======================= #
# Elsevier (Icarus) Style #
# ======================= #

_elsevier = {
    'name': 'Elsevier',
    'fontfamily': 'serif',
    'font': 'Charis SIL',
    'fontsize': 8,
    'linewidths': 0.249,
    'figsize': (3.484, 2.153),
    'latex_font_package': 'fontspec',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'column': 3.484, 'page': 7.2295},
}

# ============================== #
# Astronomy & Astrophysics Style #
# ============================== #

_aa = {
    'name': 'Astronomy & Astrophysics',
    'fontfamily': 'serif',
    'font': 'Times New Roman',
    'fontsize': 9,
    'linewidths': 0.5,
    'figsize': (3.543, 2.190),
    'latex_font_package': 'stix',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'column': 3.543, 'page': 7.283},
    'colors': [{'aa_blue': '#0000FF'}],
}


# ================================================= #
# Monthly Notices of the Royal Astronomical Society #
# ================================================= #

_mnras = {
    'name': 'Monthly Notices of the Royal Astronomical Society',
    'fontfamily': 'serif',
    'font': 'Times New Roman',
    'fontsize': 8,
    'linewidths': 0.5,
    'figsize': (3.4, 2.101),
    'latex_font_package': 'stix',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'column': 3.4, 'page': 7.05},
    'colors': [{'mnras_lavender': '#AEA6CE'}],
}


# ======================== #
# Caltech PhD Thesis Style #
# ======================== #

_caltech_thesis = {
    'name': 'Caltech Thesis',
    'fontfamily': 'serif',
    'font': 'STIX 2',
    'fontsize': 12,
    'linewidths': 0.4,
    'figsize': (5.5, 3.399),
    'latex_font_package': 'stix2',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'text': 5.5},
    'colors': [caltech_orange, caltech_neutral_colors,
               caltech_bright_colors, caltech_deep_colors]
}


# ============================ #
# My Personal Whitepaper Style #
# ============================ #

_whitepaper = {
    'name': 'Personal Whitepaper',
    'fontfamily': 'serif',
    'font': 'STIX 2',
    'fontsize': 10,
    'linewidths': 0.4,
    'figsize': (4.792, 2.962),
    'latex_font_package': 'stix2',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'twocolumn_single': 3.1875, 'twocolumn_double': 6.514,
                     'onecolumn': 4.792},
}


_named_styles = {
    'AAS': _aas,
    'AGU': _agu,
    'Elsevier': _elsevier,
    'A&A': _aa,
    'MNRAS': _mnras,
    'Caltech Thesis': _caltech_thesis,
    'Whitepaper': _whitepaper,
}
