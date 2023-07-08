#!/usr/bin/env python3

from PIL import Image
import glob
import os


def AdjustImage():

    size = (128, 128)
    graus = 270

    try:
        for root, directory, infile in os.walk("."):

            for infile in glob.glob("*.tiff"):
                file, ext = os.path.splitext(infile)
                outfile = "/opt/icons/" + file
                im = Image.open(infile)
                im.thumbnail(size)
                im.rotate(graus)
                im.save(outfile + ".thumbnail", "JPEG")
                print('Success record!')

    except OSError as e:
        print(e)

    return 'Process finishing!'


if __name__ == '__main__':
    AdjustImage()
