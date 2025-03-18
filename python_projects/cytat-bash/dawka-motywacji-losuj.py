#!/usr/bin/env python
"""
Author: @marekkoc

Created: 2020.12.15 
Updated: 2025.03.18
"""

import os
import sys
import random
from pathlib import Path

#from mkenvs import EnvVars
from mkquotes import (
                    Quote,
                    QuoteSelector,
                    FilePaths
                    )



# 2021.10.19
#hashseed = os.getenv('PYTHONHASHSEED')
#if not hashseed:
#    os.environ['PYTHONHASHSEED'] = '0'
#    os.execv(sys.executable, [sys.executable] + sys.argv)

# 2025.03.18    
#hashseed = os.getenv('PYTHONHASHSEED')
#if hashseed == '0':
#    # Usuń deterministyczne ustawienie
#    os.environ.pop('PYTHONHASHSEED', None)
#    os.execv(sys.executable, [sys.executable] + sys.argv)    
    

quote_selector = QuoteSelector(FilePaths("dawka-motywacji"))
quote = quote_selector.random_quote()
print(f"{quote.tekst}\n  ** {quote.autor} **")
