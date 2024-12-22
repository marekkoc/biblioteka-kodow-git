#!/bin/bash

# C: 2024.10.15
# M: 2024.10.15
#
# Usage:
# skrypt przyjmuje jeden argument: nazwa skryptu pythona do wykonania wraz z rozszerzeniem .py
conda run -n py38 python $1 

