import os
from exiftool import ExifTool
from logging import getLogger
from pycli_tools.commands import Command, arg
from PIL import Image
from photonizer.dhash import dhash
from photonizer.utils import FILE_NAME, TAGS, parse_date

log = getLogger('photonizer')

class RenamePhotos(Command):
    '''rename photos according to their datetime'''
    name = 'rename'
    args = [
        arg('--dry-run', action="store_true", help='do not rename files'),
        arg('files', nargs='+', help='files to rename'),
    ]

    def run(self, args, parser):
        with ExifTool() as et:
            metadata = et.get_tags_batch(TAGS, args.files)

        for meta in metadata:
            log.debug('[{}] Extrating date information from file'.format(meta["File:FileName"]))

            if 'Composite:SubSecDateTimeOriginal' in meta:
                log.debug('[{}] Using Composite:SubSecDateTimeOriginal: {}'.format(
                    meta["File:FileName"],
                    meta["Composite:SubSecDateTimeOriginal"]
                ))
                date = parse_date(meta["Composite:SubSecDateTimeOriginal"])

            elif 'EXIF:DateTimeOriginal' in meta:
                log.debug('[{}] Using EXIF:DateTimeOriginal: {}'.format(
                    meta["File:FileName"],
                    meta["EXIF:DateTimeOriginal"]
                ))
                date = parse_date(meta["EXIF:DateTimeOriginal"])

            else:
                log.debug('[{}] Using File:FileModifyDate: {}'.format(
                    meta["File:FileName"],
                    meta["File:FileModifyDate"]
                ))
                date = parse_date(meta["File:FileModifyDate"])

            if not date:
                log.warn("[{}] Could not get date information".format(meta["File:FileName"]))
                continue

            filename = FILE_NAME.format(**date, ext=meta['File:FileTypeExtension'])
            destination = os.path.join(meta['File:Directory'], filename)

            if filename == meta['File:FileName']:
                log.info("[{}] Already named correctly.".format(filename))
                continue

            log.debug("[{}] Should be renamed to {}".format(meta['File:FileName'], filename))

            if os.path.exists(destination):
                log.warn("[{}] A file with the same name already exists at destination {}".format(meta['File:FileName'], destination))

                source = os.path.join(meta['File:Directory'], meta['File:FileName'])

                source_img = Image.open(source)
                destination_img = Image.open(destination)
                source_hash = str(dhash(source_img))
                destination_hash = str(dhash(destination_img))

                if source_hash == destination_hash:
                    log.info("[{}] Source and destination files are the same image ({} == {})".format(meta['File:FileName'], source_hash, destination_hash))
                    # TODO: find image of best quality and remove the other
                else:
                    log.warn("[{}] These are different images, please resolve manually ({} != {}): open '{}' '{}'".format(meta['File:FileName'], source_hash, destination_hash, source, destination))

                continue

            if not args.dry_run:
                os.rename(meta['SourceFile'], destination)

            log.info("[{}] Renamed to {}".format(meta['File:FileName'], destination))
