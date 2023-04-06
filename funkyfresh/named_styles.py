from funkyfresh.colors import *

# ==================================== #
# American Astsronomical Society Style #
# ==================================== #

_aas = {

    'fontfamily': 'serif',
    'font': 'Times',
    'mathtext.fontset': 'stix',
    'fontsize': 8,
    'linewidths': 0.397,
    'figsize': (7.3, 4.51165),
    'latex_font_package': 'stix',
    'latex_preamble': r'\usepackage{siunitx, amsmath, amssymb, '
                      r'isomath, physics}\usepackage[version = 4]{mhchem}',
    'figurewidths': {'column': 3.5, 'page': 7.3},
}

# ================================ #
# American Geophysical Union Style #
# ================================ #

_agu = {
    'fontfamily': 'serif',
    'font': 'Times New Roman',
    'mathtext.fontset': 'stix',
    'fontsize': 8,
    'linewidths': 0.5,
    'figsize': (7.5, 4.63525),
    'latex_font_package': 'stix',
    'latex_preamble': r'\usepackage{siunitx, amsmath, amssymb, '
                      r'isomath, physics}\usepackage[version = 4]{mhchem}',
    'figurewidths': {'column': 3.5, 'text': 5.6,
                     'page': 7.5},
    'colors': [{'agu_blue': '#004174'}],
}


# ======================== #
# Caltech PhD Thesis Style #
# ======================== #

_caltech_thesis = {

    'fontfamily': 'serif',
    'font': 'Times',
    'mathtext.fontset': 'stix',
    'fontsize': 12,
    'linewidths': 0.4,
    'figsize': (5.5206, 3.4119),
    'latex_font_package': 'stix',
    'latex_preamble': r'\usepackage{siunitx, amsmath, amssymb, '
                      r'isomath, physics}\usepackage[version = 4]{mhchem}',
    'figurewidths': {'text': 5.5206},
    'colors': [caltech_orange, caltech_neutral_colors,
               caltech_bright_colors, caltech_deep_colors]
}


_named_styles = {
    'AAS': _aas,
    'AGU': _agu,
    'Caltech Thesis': _caltech_thesis,
}
