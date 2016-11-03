
__title__ = 'dtguess'
__version__ = "0.0.1"

import os
import sys

path = os.path.realpath(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(path)))
sys.path.insert(0, os.path.join(os.path.dirname(path), 'vendor/'))


from types import StringType, IntegerType, DecimalType, BooleanType, \
                DateType,  DateUtilType

from guesses import CellGuess

# from utils import guess, type_guess
