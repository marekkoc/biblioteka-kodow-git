#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Basic PIL functions

C: 2024.10.20
M: 2024.10.20
"""

from PIL import Image, ImageFilter, ImageEnhance
from pathlib import Path

fn = Path("~/Desktop/zdjecie.JPEG").expanduser()
with Image.open(fn) as pic:
    if 1: pic.show(title="oryginal")

    saturate = ImageEnhance.Color(pic)
    saturate = saturate.enhance(1.2)
    if 0: saturate.show("enhanced by 1.2")
    saturate.save(Path("~/Desktop/zdjecie-sat.JPEG").expanduser())

    black_white = pic.convert("L")
    if 0: black_white.show("blac& white")
    black_white.save(Path("~/Desktop/zdjecie-bw.JPEG").expanduser())

    mirror = pic.transpose(Image.FLIP_LEFT_RIGHT)
    if 0: mirror.show("mirrored")
    mirror.save(Path("~/Desktop/zdjecie-mirr.JPEG").expanduser())

    blur = pic.filter(ImageFilter.BLUR)
    if 0: blur.show()
    blur.save(Path("~/Desktop/zdjecie-blur.JPEG").expanduser())

    contrast = ImageEnhance.Contrast(pic)
    contrast = contrast.enhance(1.2)
    if 0: contrast.show()
    contrast.save(Path("~/Desktop/zdjecie-cont.JPEG").expanduser())

    color = ImageEnhance.Color(pic).enhance(2.0)
    if 0: color.show()
    color.save(Path("~/Desktop/zdjecie-color.JPEG").expanduser())


