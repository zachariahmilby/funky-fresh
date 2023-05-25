from funkyfresh.colors import *


_default_latex_preamble = r'\usepackage{siunitx, amsmath, amssymb, isomath, ' \
                          r'physics}\usepackage[version=4]{mhchem}'

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


# ============================== #
# Astronomy & Astrophysics Style #
# ============================== #

_aa = {
    'name': 'Astronomy & Astrophysics',
    'fontfamily': 'serif',
    'font': 'Times New Roman',
    'fontsize': 9,
    'linewidths': 0.5,
    'figsize': (3.543, 2.19),
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
    'figsize': (3.4, 2.10),
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
    'font': 'Times New Roman',
    'fontsize': 10,
    'linewidths': 0.4,
    'figsize': (5.5206, 3.4119),
    'latex_font_package': 'stix',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'text': 5.5206},
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
    'fontsize': 8,
    'linewidths': 0.4,
    'figsize': (3.1875, 1.97),
    'latex_font_package': 'stix2',
    'latex_preamble': _default_latex_preamble,
    'figurewidths': {'column': 3.1875, 'page': 6.514},
}


_named_styles = {
    'AAS': _aas,
    'AGU': _agu,
    'A&A': _aa,
    'MNRAS': _mnras,
    'Caltech Thesis': _caltech_thesis,
    'Whitepaper': _whitepaper,
}
