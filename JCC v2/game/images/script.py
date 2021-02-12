from os import rename, listdir
from PIL import Image

fnames = listdir('.')

for fname in fnames:
    if "male bff" in fname:
        im = Image.open(
            "C:/Users/saul/Documents/gavin sim/jccDatingSim/JCC v2/game/images/" + fname)

        ratio = 0.62
        out = im.resize([int(ratio * s) for s in im.size])
        out = out.save(fname)
