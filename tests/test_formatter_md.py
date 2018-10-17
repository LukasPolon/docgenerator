""" Unit tests for formatter_md module. """
import unittest

from src.formatter_md import FormatterMd


class TestFormatterMd(unittest.TestCase):
    """ Test suite for FormatterMd class."""

    def setUp(self):
        self.formattermd = FormatterMd()

    def test_header_one(self):
        """ Test header method from FormatterMd class.

            Case: level one
        """
        text = 'Example text'
        level = 1

        result = self.formattermd.header(text, level)
        exp_result = '# Example text'
        self.assertEqual(result, exp_result)

    def test_header_six(self):
        """ Test header method from FormatterMd class.

            Case: level six
        """
        text = 'Example text'
        level = 6

        result = self.formattermd.header(text, level)
        exp_result = '###### Example text'
        self.assertEqual(result, exp_result)

    def test_link(self):
        """ Test link method from FormatterMd class."""
        title = 'Example link title'
        link = 'http://test/link'

        result = self.formattermd.link(title, link)
        exp_result = '[Example link title](http://test/link)'
        self.assertEqual(result, exp_result)

    def test_italics(self):
        """ Test italics method from FormatterMd class."""
        text = 'Example text'

        result = self.formattermd.italics(text)
        exp_result = '_Example text_'
        self.assertEqual(result, exp_result)

    def test_bold(self):
        """ Test bold method from FormatterMd class."""
        text = 'Example text'

        result = self.formattermd.bold(text)
        exp_result = '**Example text**'
        self.assertEqual(result, exp_result)

    def test_code(self):
        """ Test code method from FormatterMd class."""
        code_lines = [
            'example code line #1',
            'example code line #2'
        ]

        result = self.formattermd.code(code_lines)
        exp_result = [
            '```',
            'example code line #1',
            'example code line #2',
            '```'
        ]
        self.assertEqual(result, exp_result)

    def test_bullet_list(self):
        """ Test bullet_list method from FormatterMd class."""
        list_elements = [
            'example element #1',
            'example element #2'
        ]

        result = self.formattermd.bullet_list(list_elements)
        exp_result = [
            '* example element #1',
            '* example element #2'
        ]
        self.assertEqual(result, exp_result)

    def test_numbered_list(self):
        """ Test numbered_list method from FormatterMd class."""
        list_elements = [
            'example element #1',
            'example element #2'
        ]

        result = self.formattermd.numbered_list(list_elements)
        exp_result = [
            '1. example element #1',
            '2. example element #2'
        ]
        self.assertEqual(result, exp_result)

    def test_add_horizontal(self):
        """ Test add_horizontal method from FormatterMd class."""
        exp_result = '---'
        result = self.formattermd.add_horizontal()
        self.assertEqual(result, exp_result)

    def test_create_table(self):
        """ Test table creation feature. """
        headers = ['Header1', 'Header2', 'Header3']
        first_row = ['example', 'element', 'in first row']
        second_row = ['good', 'bad', 'medium']
        third_row = ['Python', 'Java', 'Brainfuck']
        rows = [first_row, second_row, third_row]
        exp_result = [
            'Header1 | Header2 | Header3',
            '--- | --- | --- | ',
            'example | element | in first row',
            'good | bad | medium',
            'Python | Java | Brainfuck'
        ]
        result = self.formattermd.create_table(rows, headers)
        self.assertEqual(result, exp_result)
