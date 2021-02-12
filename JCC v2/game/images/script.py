from os import rename, listdir
from PIL import Image

fnames = listdir('.')

for fname in fnames:
    if "bff" in fname or "gavin" in fname or "mbff" in fname:
        im = Image.open(
            "C:/Users/saul/Documents/gavin sim/jccDatingSim/JCC v2/game/images/" + fname)

        ratio = 2.2
        out = im.resize([int(ratio * s) for s in im.size])
        out = out.save(fname)
