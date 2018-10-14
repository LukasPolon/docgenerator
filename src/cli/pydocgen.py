""" Application main commands module.

    Commands:
        - pydocgen
"""
import click


@click.command('pydocgen', help='PyDocGenerator - Python documentation creator TEST HOUND CI')
def pydocgen():
    """ Main application command. """
    click.echo('PYDOCGEN command.')
