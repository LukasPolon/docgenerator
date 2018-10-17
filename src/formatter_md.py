""" Module which is resposnible for MD text formatting.

    Classes:
        - FormatterMd
"""
from copy import deepcopy


class FormatterMd:
    """ Format given text to a certain Markdown element."""

    def header(self, text, level):
        """ Add a header mark.
            Header levels: 1-6

            Args:
                text(str): text to format
                level(int): header level

            Returns:
                formatted(str): formatted text
        """
        header_marks = '#' * level

        formatted = '{marks} {text}'.format(
            marks=header_marks, text=text
        )
        return formatted

    def link(self, title, link):
        """ Create a link format.

            Args:
                title(str): link title which will be shown
                link(str): url representation

            Returns:
                formatted(str): formatted text
        """
        formatted = '[{title}]({link})'.format(
            title=title, link=link
        )
        return formatted

    def italics(self, text):
        """ Change text format to italics.

            Args:
                text(str): text to format

            Returns:
                formatted(str): formatted text
        """
        formatted = '_{text}_'.format(text=text)
        return formatted

    def bold(self, text):
        """ Change text format to bold.

            Args:
                text(str): text to format

            Returns:
                formatted(str): formatted text
        """
        formatted = '**{text}**'.format(text=text)
        return formatted

    def code(self, code_lines):
        """ Create code block on a given code lines.

            Args:
                code_lines(list): sequence of code lines

            Returns:
                code_block(list): formatted code block
        """
        code_sign = '```'
        code_block = deepcopy(code_lines)
        code_block.insert(0, code_sign)
        code_block.append(code_sign)
        return code_block

    def bullet_list(self, list_elements):
        """ Create a bullet list.

            Args:
                list_elements(list): elements of a bullet list

            Returns:
                bullet_list(list): formatted bullet list
        """
        bullet_list = ['* {el}'.format(el=el) for el in list_elements]
        return bullet_list

    def numbered_list(self, list_elements):
        """ Create a numbered list.

            Args:
                list_elements(list): elements of a numbered list

            Returns:
                numbered_list(list): formatted numbered list
        """
        numbered_list = ['{num}. {el}'.format(num=num, el=el) for num, el
                         in enumerate(list_elements, 1)]
        return numbered_list

    def add_horizontal(self):
        """ Return a horizontal rule string.

            Returns:
                horizontal(str): horizontal rule string
        """
        return '---'

    def _prepare_headers_cells(self, headers):
        """Prepare headers cells for table creation.

        Args:
            headers (list): table column names

        Returns:
            headers_cells(list): headers cells ready for further table-related
            operations
        """
        headers_row = ['{header} | '.format(header=h) for h in headers]
        headers_row = ''.join(headers_row)
        headers_separation = '--- | ' * len(headers)
        headers_cells = [headers_row, headers_separation]
        return headers_cells

    def create_table(self, rows, headers):
        """ Creates table with the given size.

        Args:
           rows(list): list of lists; each nested list is a table row
           headers(list): column names

        Returns:
            table(list): list of formatted strings; every string represents
            single row, starting from headers
        """
        headers_cells = self._prepare_headers_cells(headers)
        table = headers_cells
        for row in rows:
            row_str = str()
            for row_elem in row:
                row_str += ''.join(row_elem + ' | ')
            table.append(row_str)
        return table
