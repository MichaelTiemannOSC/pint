"""
    pint.delegates.formatter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Formats quantities and units.
    :copyright: 2022 by Pint Authors, see AUTHORS for more details.
    :license: BSD, see LICENSE for more details.
"""


from .base_formatter import BaseFormatter
from .iso80000_formatter import ISO80000Formatter


class Formatter(ISO80000Formatter, BaseFormatter):
    # TODO: this should derive from all relevant formaters to
    # reproduce the current behavior of Pint.
    pass


__all__ = [
    "Formatter",
]
