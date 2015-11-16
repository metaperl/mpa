__author__ = 'anicca'

# core
import math
import sys
from itertools import izip

# 3rd party
from PIL import Image, ImageChops
import argh


def dhash(image, hash_size=8):
    # Grayscale and shrink the image in one step.
    image = image.convert('L').resize(
        (hash_size + 1, hash_size),
        Image.ANTIALIAS,
    )

    pixels = list(image.getdata())

    # Compare adjacent pixels.
    difference = []
    for row in range(hash_size):
        for col in range(hash_size):
            pixel_left = image.getpixel((col, row))
            pixel_right = image.getpixel((col + 1, row))
            difference.append(pixel_left > pixel_right)

    # Convert the binary array to a hexadecimal string.
    decimal_value = 0
    hex_string = []
    for index, value in enumerate(difference):
        if value:
            decimal_value += 2 ** (index % 8)
        if (index % 8) == 7:
            hex_string.append(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return ''.join(hex_string)


def rosetta(image1, image2):
    i1 = Image.open(image1)
    i2 = Image.open(image2)
    assert i1.mode == i2.mode, "Different kinds of images."
    print i1.size, i2.size
    assert i1.size == i2.size, "Different sizes."

    pairs = izip(i1.getdata(), i2.getdata())
    if len(i1.getbands()) == 1:
        # for gray-scale jpegs
        dif = sum(abs(p1 - p2) for p1, p2 in pairs)
    else:
        dif = sum(abs(c1 - c2) for p1, p2 in pairs for c1, c2 in zip(p1, p2))

    ncomponents = i1.size[0] * i1.size[1] * 3
    retval = (dif / 255.0 * 100) / ncomponents
    return retval


def rmsdiff_2011(im1, im2):
    "Calculate the root-mean-square difference between two images"

    im1 = Image.open(im1)
    im2 = Image.open(im2)
    diff = ImageChops.difference(im1, im2)
    h = diff.histogram()
    sq = (value * (idx ** 2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rms = math.sqrt(sum_of_squares / float(im1.size[0] * im1.size[1]))
    return rms


def main(image_filename1, image_filename2, dhash=False, rosetta=False, rmsdiff=False):
    pass


if __name__ == '__main__':
    argh.dispatch_command(main)
