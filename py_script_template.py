#!/usr/bin/env python3

# author: Mourad Askar <mourad.askar@outlook.com>
# date: 2020-05-01
# version: 1.0
# description: This script is a template script for python scripts

# Import modules
import os, sys
import argparse
import logging
import logging.handlers
from yachalk import chalk
import tqdm

import shutil
import tempfile

# Declare global variables
log: logging.Logger
script_path, script_file, script_name, script_ext = None, None, None, None

# Main function
def main(args=None):
    log.info('Starting script')
    log.debug('Debug output')
    log.info('Info output')
    log.warning('Warning output')
    log.error('Error output')
    log.critical('Critical output')
    log.info('Script finished')

    load_config()
    print(script_path)



def load_config():
    '''Load configuration'''
    log.info(f'Loading configuration {sys._getframe().f_code.co_name}()')

def parse_args(description=None):
    '''Parse arguments'''
    parser = argparse.ArgumentParser(description)
    parser.add_argument('-d', '--debug', action='store_true', help='Enable debug output')
    parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose output')
    parser.add_argument('-q', '--quiet', action='store_true', help='Disable output')
    parser.add_argument('-l', '--log-to-file', action='store_true', help='Log to file')

    # Create a new group to store required arguments
    requiredName = parser.add_argument_group('required named arguments')

    # Add required arguments to the parser
    requiredName.add_argument("--path", action="extend", nargs="+", type=str)

    # Return the parsed arguments
    args = parser.parse_args()
    return args

def init_logging(logger_name, debug=False, verbose=False, quiet=False, log_to_file=False):
    '''Initialize logging'''
    # Initialize logging
    log_file_ext = 'log'
    log_file = f'{logger_name}.{log_file_ext}'

    # Setup logging
    logger = logging.getLogger(logger_name)

    # Set loglevel
    if debug:
        logger.setLevel(logging.DEBUG)
    elif verbose:
        logger.setLevel(logging.INFO)

    # Create formatter
    # Reference: https://docs.python.org/3/library/logging.html#logrecord-attributes
    formatter_file = logging.Formatter('{asctime} | {name} | {process} | {levelname:<8} | {message}', style='{')
    formatter_console = logging.Formatter('{asctime} | {name} | {levelname:<8} | {message}', style='{')

    # Create file handler
    if log_to_file:
        fh = logging.handlers.RotatingFileHandler(log_file, maxBytes=1_000_000, backupCount=3)
        fh.setFormatter(formatter_file)
        logger.addHandler(fh)

    # Create console handler
    if not quiet:
        ch = logging.StreamHandler()
        ch.setFormatter(formatter_console)
        logger.addHandler(ch)




    return logger


if __name__ == '__main__':
    # Parse scriptname
    script_path, script_file = os.path.split(__file__)
    script_name, script_ext = os.path.splitext(script_file)

    # Parse arguments (optional: add description)
    args = parse_args(description=None)
    # print(args)

    # Setup logging (default: log file is scriptfile.log)
    # global log
    log = init_logging(script_file, args.debug, args.verbose, args.quiet, args.log_to_file)

    # Run main
    sys.exit(main(args))
