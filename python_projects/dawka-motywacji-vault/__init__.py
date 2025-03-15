"""
Pakiet do zarządzania cytatami motywacyjnymi.

Zawiera narzędzia do konwersji plików z cytatami oraz losowego wybierania cytatów.
"""

from mkquotes import FilePaths, Odt2TxtConverter, Txt2JsonConverter, QuoteSelector
from .main_dawka import *

__all__ = ['FilePaths', 'Odt2TxtConverter', 'Txt2JsonConverter', 'QuoteSelector', 'main_dawka'] 