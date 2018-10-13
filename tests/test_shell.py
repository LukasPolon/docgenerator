import unittest

from unittest import mock

from src.shell import run


class TestShell(unittest.TestCase):

    @mock.patch('src.shell.pydocgen')
    def test_run(self, mock_pydocgen):
        """ Test run function from shell module."""
        run()
        self.assertTrue(mock_pydocgen.called)

    @mock.patch('src.shell.echo')
    @mock.patch('src.shell.pydocgen')
    def test_run_negative(self, mock_pydocgen, mock_echo):
        """ Test run function from shell module.
            Case: Exception occurred.
        """
        mock_pydocgen.side_effect = ValueError
        run()
        self.assertTrue(mock_echo.called)
