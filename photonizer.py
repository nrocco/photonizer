#!/usr/bin/env python
import sys
import os
import logging
import exiftool
import re

RE_DATE = re.compile(r'^(?P<year>\d{4}):(?P<month>\d{2}):(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.(?P<subsec>\d+))?.*$')

FILE_NAME = '{year}.{month:0>2d}.{day:0>2d}-{hour:0>2d}.{minute:0>2d}.{second:0>2d}.{subsec:0<3d}.{ext}'
DIR_NAME = '{year}/{year}-{month:0>2d}'

logger = logging.getLogger(__name__)

def parse_date(datetime_string):
    results = RE_DATE.match(datetime_string)
    if results:
        subsec = '{0:0<3}'.format(results.group('subsec') or 0)
        return {
            'year': int(results.group('year')),
            'month': int(results.group('month')),
            'day': int(results.group('day')),
            'hour': int(results.group('hour')),
            'minute': int(results.group('minute')),
            'second': int(results.group('second')),
            'subsec': int(subsec[:3])
        }

def main():
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(message)s')

    files = sys.argv[1:]

    if len(files) == 0:
        print("No files found...")
        return 1

    with exiftool.ExifTool() as et:
        metadata = et.get_metadata_batch(files)

    for meta in metadata:
        if 'Composite:SubSecDateTimeOriginal' in meta:
            date = parse_date(meta["Composite:SubSecDateTimeOriginal"])
        elif 'EXIF:DateTimeOriginal' in meta:
            date = parse_date(meta["EXIF:DateTimeOriginal"])
        else:
            date = parse_date(meta["File:FileModifyDate"])

        if not date:
            logger.error("Could get date from EXIF for {}".format(meta["File:FileName"]))
            return

        filename = FILE_NAME.format(**date, ext=meta['File:FileTypeExtension'])
        destination = os.path.join(meta['File:Directory'], filename)

        if filename == meta['File:FileName']:
            logger.info("File {} is already named correctly".format(filename))
            continue

        logger.info("The file {} should be renamed to {}".format(meta['File:FileName'], filename))

        if os.path.exists(destination):
            log.warn("A file with the same name already exists at {}".format(destination))
            continue

        os.rename(meta['SourceFile'], destination)
        logger.info("Renamed {} to {}".format(meta['File:FileName'], destination))

if '__main__' == __name__:
    main()
