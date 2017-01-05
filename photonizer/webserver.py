import os
from logging import getLogger

from PIL import Image

from bottle import Bottle, run
from bottle import static_file, template, abort

log = getLogger('photonizer')

app = Bottle()

@app.route('/thumbs/<path:path>')
def static_thumbs(path):
    thumb = os.path.join(app.config['thumbs_dir'], path)

    if not os.path.isfile(thumb):
        photo = os.path.join(app.config['photos_dir'], path)
        if not os.path.isfile(photo):
            abort(404)

        os.makedirs(os.path.dirname(thumb), exist_ok=True)
        file = Image.open(photo)
        exif = file._getexif()
        if exif:
            exif = dict(exif.items())
            if exif[274] == 3:
                file = file.rotate(180, expand=True)
            elif exif[274] == 6:
                file = file.rotate(270, expand=True)
            elif exif[274] == 8:
                file = file.rotate(90, expand=True)
        file.thumbnail((300,300))
        file.save(thumb, 'JPEG')
        log.info("Generated thumbnail on the fly for {}".format(photo))

    return static_file(path, root=app.config['thumbs_dir'])


@app.route('/')
@app.route('/<path:path>')
def index(path=""):
    files = []
    directories = []
    directory = os.path.join(app.config['photos_dir'], path) if path else app.config['photos_dir']

    if os.path.isfile(directory):
        return static_file(path, root=app.config['photos_dir'])

    for file in os.listdir(directory):
        if os.path.isdir(os.path.join(directory, file)):
            directories.append(os.path.join(path, file))
        else:
            files.append(file)
    return template('hello_template',
                    path=path,
                    paths=path.split('/'),
                    directories=directories,
                    files=files)


def main(photos_dir, thumbs_dir, host='0.0.0.0', port=8080):
    app.config['photos_dir'] = photos_dir
    app.config['thumbs_dir'] = thumbs_dir

    log.info("Serving photos from {}".format(photos_dir))
    log.info("Serving thumbs from {}".format(thumbs_dir))

    run(app, host=host, port=port, reloader=True)


if __name__ == '__main__':
    photos_dir = os.getcwd() + '/run/collection'
    thumbs_dir = os.getcwd() + '/run/thumbnails'
    main(photos_dir, thumbs_dir)
