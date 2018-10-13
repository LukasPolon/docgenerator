""" Application main commands module.

    Commands:
        - pydocgen
"""
import click


@click.command('pydocgen', help='PyDocGenerator - Python documentation creator')
def pydocgen():
    """ Main application command. """
    click.echo('PYDOCGEN command.')
