"""
    This class add custom numbers formatting methods
"""


class NumbersFormatter:

    """
    If you need round number e.g.: 12.50 to 12.5 and remove zeroes after decimal separator from 9.00 e.g.:
        NumbersFormatter.round_num(12.50, 1)
        NumbersFormatter.round_num(9.00, 1, '.0', '')
    """
    @staticmethod
    def round_num(number, precision: int, replace_what: str = None, replace_to: str = None) -> str:
        if number:
            return str(round(number, precision)).replace(replace_what, replace_to)
