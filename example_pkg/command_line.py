from . import *
import argparse
import yaml
import sys
import os
from .pipeline import ProcessingSession

def show_banner():
    print("""
    Example_pkg version {version}
    An example python package by Yongkuk Choi <ykchoi624@gmail.com>
    """.format(version=__version__))

def load_config(args):
    presets_dir = os.path.join(os.path.dirname(__file__),'presets')
    if not args.config:
        config_path = os.path.join(presets_dir, 'default.cfg')
    elif os.path.isfile(args.config):
        config_path = args.config
    elif os.path.isfile(os.patj.join(presets_dir, args.config + '.cfg')):
        config_path = os.path.join(presets_dir, args.config + '.cfg')
    else:
        errx('ERROR: Cannot find a configuration in {}.'.format(args.config))

    config = yaml.load(open(config_path))

    return config

def main(args):
    if not args.quiet:
        show_banner()

    config = load_config(args)
    config['mode'] = args.mode
    config['quiet'] = args.quiet
    config['parallel'] = args.parallel

    print("Parallel mode : {}".format(config['mode']))

    session = ProcessingSession(config)
    session.run_task_is_prime()



def __main__():
    parser = argparse.ArgumentParser(
            prog='example_pkg', add_help=False,
            description='An example python package.')

    group = parser.add_argument_group('Basics')
    group.add_argument('-m', '--mode', required=True, type=str,
                        help='Choose the type of executor; process or thread')
    group.add_argument('-p', '--parallel', default=1, type=int, metavar='COUNT',
                        help='number of wrokers (default=1)')
    group.add_argument('-h', '--help', action='help',
                        help='show this help message and exit')
    group.add_argument('-q', '--quiet', default=False, action='store_true',
                        help='suppress all messages')
    group.add_argument('-c', '--config', default='', metavar='NAME',
                        help='path to configuration file')

    args = parser.parse_args(sys.argv[1:])
    main(args)
