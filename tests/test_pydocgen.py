import unittest

from click.testing import CliRunner

from src.cli.pydocgen import pydocgen


class TestPydocgen(unittest.TestCase):

    def setUp(self):
        """ SetUp method inherted from TestCase."""
        self.clirunner = CliRunner()

    def test_pydocgen(self):
        """ Test pydocgen command."""
        result = self.clirunner.invoke(pydocgen)
        self.assertEqual(result.exit_code, 0)
        self.assertEqual(result.output.strip(), 'PYDOCGEN command.')
