import pandas as pd

class Format:
    INT = "{:,d}".format
    FLOAT = "{:,.2f}".format

    @staticmethod
    def int(width: int, thousands: str = ',', zero: str = '', sign: str = '') -> callable:
        return f"{{:{sign}{zero}{width}{thousands}d}}".format

class PandasHelper:
    def __init__(self):
        # Show all columns (instead of cascading columns in the middle)
        self.orig_display_max_columns = pd.get_option('display.max_columns')
        self.orig_display_max_colwidth = pd.get_option('display.max.colwidth')

        self.unlimit_columns()
        # Don't show numbers as scientific notation
        pd.set_option("display.float_format", Format.FLOAT)

    def unlimit_columns(self):
        pd.set_option("display.max_columns", None)

    def set_max_columns(self, size: int = None):
        pd.set_option("display.max_columns", size)

    def reset_columns(self):
        pd.set_option("display.max_columns", self.orig_display_max_columns)

    def unlimit_colwidth(self):
        pd.set_option('display.max.colwidth', None)

    def reset_colwidth(self):
        pd.set_option("display.max_colwidth", self.orig_display_max_colwidth)

    def set_max_colwidth(self, size: int = None):
        pd.set_option("display.max_colwidth", size)

