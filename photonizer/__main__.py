from sys import exit
from logging import getLogger
from photonizer import __version__
from photonizer import __config_files__
from photonizer.commands import commands
from pycli_tools.parsers import get_argparser

def main():
    parser = get_argparser(prog='photonizer', default_config=__config_files__, version=__version__)
    parser.add_commands(commands)

    args = parser.parse_args()

    return args.func(args, parser=parser)

if '__main__' == __name__:
    exit(main())
