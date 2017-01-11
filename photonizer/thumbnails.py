import os
from logging import getLogger

from PIL import Image

log = getLogger('photonizer')

def generate_thumbnail(photo, thumbnail):
    os.makedirs(os.path.dirname(thumbnail), exist_ok=True)
    file = Image.open(photo)
    exif = file._getexif()

    if exif:
        exif = dict(exif.items())

        if not 274 in exif:
            pass
        elif exif[274] == 3:
            file = file.rotate(180, expand=True)
        elif exif[274] == 6:
            file = file.rotate(270, expand=True)
        elif exif[274] == 8:
            file = file.rotate(90, expand=True)

    file.thumbnail((300,300))
    file.save(thumbnail, 'JPEG')

    log.info("Generated thumbnail for {}".format(photo))
