import os, sys
from PIL import Image

size = (320, 240)

# https://pillow.readthedocs.io/en/stable/handbook/tutorial.html
# kör programmet med python3 thumb.py *.jpg

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + "_thumbnail.jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im.thumbnail(size)
                im.save(outfile, "JPEG")
        except OSError:
            print("cannot create thumbnail for", infile)