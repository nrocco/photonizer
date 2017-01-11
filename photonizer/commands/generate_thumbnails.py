import os
from logging import getLogger
from pycli_tools.commands import Command, arg
from photonizer.utils import parse_file, DIR_NAME
from photonizer.thumbnails import generate_thumbnail

log = getLogger('photonizer')

class GenerateThumbnails(Command):
    '''generate missing thumbnails for photos in the collection'''
    name = 'thumbnails'
    args = [
        arg('directory', nargs='?', help='only scan this subdirectory in the collection'),
    ]

    def run(self, args, parser):
        if args.directory:
            directory = os.path.join(args.collection, args.directory)
        else:
            directory = args.collection

        log.info("Generating missing thumbnails for all photos in {}".format(directory))

        for root, subdirs, files in os.walk(directory):
            for file in files:
                photo = os.path.join(root, file)
                thumb = photo.replace(args.collection, args.thumbnails)

                if not os.path.isfile(thumb):
                    try:
                        generate_thumbnail(photo, thumb)
                    except OSError as e:
                        log.warn(e)

        log.info("Done generating thumbnails")
