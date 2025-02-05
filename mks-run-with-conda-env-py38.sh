#!/bin/bash

# C: 2024.10.15
# M: 2025.02.05
#
# Usage:
# skrypt przyjmuje jeden argument: nazwa skryptu pythona do wykonania wraz z rozszerzeniem .py
conda run -n py312 python $1 

