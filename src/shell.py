""" Module responsible for running the application.

    Functions:
        - run
"""

import sys

from click import echo

from src.cli.pydocgen import pydocgen


def run():
    """ Start the application and handle exceptions. """
    try:
        pydocgen()
    except Exception:
        exc_type, exc_value, _ = sys.exc_info()
        echo('>> ERR >> {}: {}'.format(exc_type.__name__, exc_value))
