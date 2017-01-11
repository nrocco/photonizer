import os
from logging import getLogger
from pycli_tools.commands import Command, arg
from photonizer.utils import parse_file, DIR_NAME
from photonizer.thumbnails import generate_thumbnail

log = getLogger('photonizer')

class ImportPhotos(Command):
    '''import photos into your collection'''
    name = 'import'
    args = [
        arg('--dry-run', action="store_true", help='do not rename files'),
        arg('files', nargs='+', help='files to rename'),
    ]

    def run(self, args, parser):
        for file in args.files:
            if not os.path.exists(file):
                continue

            date_parts = parse_file(file)

            if not date_parts:
                log.warn('[{}] Could not parse filename. Ignoring'.format(file))
                continue

            source = os.path.abspath(file)
            destination = DIR_NAME.format(basedir=args.collection,
                                          file=os.path.basename(file),
                                          **date_parts)

            destination_dir = os.path.dirname(destination)

            if not os.path.exists(destination_dir):
                log.info('Directory {} does not exist. Creating it now'.format(destination_dir))
                os.makedirs(destination_dir)

            if os.path.exists(destination):
                log.warn("[{}] A file with the same name already exists at destination {}".format(file, destination))
                continue

            if not args.dry_run:
                os.rename(source, destination)

                thumbnail = DIR_NAME.format(basedir=args.thumbnails,
                                            file=os.path.basename(file),
                                            **date_parts)
                generate_thumbnail(destination, thumbnail)

            log.info("[{}] Imported to {}".format(file, destination))
