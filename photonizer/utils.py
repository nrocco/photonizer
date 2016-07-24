from re import compile

RE_DATE = compile(r'^(?P<year>\d{4}):(?P<month>\d{2}):(?P<day>\d{2}) (?P<hour>\d{2}):(?P<minute>\d{2}):(?P<second>\d{2})(\.(?P<subsec>\d+))?.*$')
RE_FILE_NAME = compile(r'^.*(?P<year>\d{4})\.(?P<month>\d{2})\.(?P<day>\d{2})-(?P<hour>\d{2})\.(?P<minute>\d{2})\.(?P<second>\d{2})\.(?P<subsec>\d+).*$')
FILE_NAME = '{year}.{month:0>2d}.{day:0>2d}-{hour:0>2d}.{minute:0>2d}.{second:0>2d}.{subsec:0<3d}.{ext}'
DIR_NAME = '{basedir}/{year}/{year}-{month:0>2d}/{file}'

TAGS = [
    'Composite:SubSecDateTimeOriginal',
    'EXIF:DateTimeOriginal',
    'File:Directory',
    'File:FileModifyDate',
    'File:FileName',
    'File:FileTypeExtension',
    'SourceFile',
]

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

def parse_file(filename):
    results = RE_FILE_NAME.match(filename)
    if results:
        return {
            'year': int(results.group('year')),
            'month': int(results.group('month')),
            'day': int(results.group('day')),
            'hour': int(results.group('hour')),
            'minute': int(results.group('minute')),
            'second': int(results.group('second')),
            'subsec': int(results.group('subsec'))
        }
