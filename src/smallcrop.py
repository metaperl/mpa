from PIL import Image


def horizontal_sections(input, sections):
    im = Image.open(input)
    imgwidth, imgheight = im.size
    width = imgwidth / sections
    height = imgheight
    i = 0
    filenames = list()
    offsets = list()
    for j in range(0, imgwidth, imgwidth/4):
        box = (j, i, j + width, i + height)
        a = im.crop(box)
        fn = "IMG-{0}.png".format(i)
        a.save(fn)
        filenames.append(fn)
        offsets.append(j)
        if i == 3:
            break
        i += 1
    sectioned_image = dict(filenames=filenames,offsets=offsets)

    return sectioned_image


if __name__ == '__main__':
    horizontal_sections('candidate_images.gif', 4)
