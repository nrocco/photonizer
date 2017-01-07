from logging import getLogger
from pycli_tools.commands import Command, arg
from photonizer.webserver import main

log = getLogger('photonizer')

class Webserver(Command):
    '''expose your collection over http'''
    name = 'webserver'
    args = [
        arg('--host', default='0.0.0.0'),
        arg('--port', default='8080'),
    ]

    def run(self, args, parser):
        main(args.collection, args.thumbnails, args.host, args.port)
