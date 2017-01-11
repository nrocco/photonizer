import os
from logging import getLogger
from PIL import Image
from bottle import Bottle, run, TEMPLATE_PATH
from bottle import static_file, template, abort
from photonizer.thumbnails import generate_thumbnail

TEMPLATE_PATH.insert(0, os.path.join(os.path.dirname(__file__), 'views'))

log = getLogger('photonizer')

app = Bottle()

@app.route('/thumbs/<path:path>')
def static_thumbs(path):
    thumb = os.path.join(app.config['thumbs_dir'], path)

    if not os.path.isfile(thumb):
        photo = os.path.join(app.config['photos_dir'], path)
        if not os.path.isfile(photo):
            abort(404)
        generate_thumbnail(photo, thumb)

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
    return template('gallery',
                    path=path,
                    paths=path.split('/'),
                    directories=directories,
                    files=files)


def main(photos_dir, thumbs_dir, host='0.0.0.0', port=8080):
    app.config['photos_dir'] = photos_dir
    app.config['thumbs_dir'] = thumbs_dir

    log.info("Serving photos from {}".format(photos_dir))
    log.info("Serving thumbs from {}".format(thumbs_dir))

    run(app, host=host, port=port, reloader=False)


if __name__ == '__main__':
    photos_dir = os.getcwd() + '/run/collection'
    thumbs_dir = os.getcwd() + '/run/thumbnails'
    main(photos_dir, thumbs_dir)
