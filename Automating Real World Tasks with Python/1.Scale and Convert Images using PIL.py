#!/usr/bin/env python3
import os, sys
from PIL import Image

size = (128, 128)

for infile in os.listdir():
    outfile = os.path.splitext(infile)[0]
    try:
        with Image.open(infile).convert('RGB') as im:
            im.thumbnail(size)
            im.rotate(270).save("/opt/icons/" + outfile, "JPEG")
    except OSError:
        pass
