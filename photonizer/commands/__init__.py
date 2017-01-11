from photonizer.commands.rename_photos import RenamePhotos
from photonizer.commands.import_photos import ImportPhotos
from photonizer.commands.generate_thumbnails import GenerateThumbnails
from photonizer.commands.webserver import Webserver

commands = [
    RenamePhotos(),
    ImportPhotos(),
    GenerateThumbnails(),
    Webserver()
]
