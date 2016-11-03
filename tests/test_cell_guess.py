
from dtguess import StringType, IntegerType, DecimalType, BooleanType, \
                DateType,  DateUtilType

from dtguess import CellGuess

def test_cell_guess_basic_types():

    assert CellGuess().guess(None) == [BooleanType()]

    assert CellGuess().guess(5) == [IntegerType()]
    assert CellGuess().guess('5') == [IntegerType()]
    assert CellGuess().guess('5.0') == [IntegerType()]

    assert CellGuess().guess(5.1) == [DecimalType()]
    assert CellGuess().guess('5.1') == [DecimalType()]

    assert CellGuess().guess('2016-01-01') == [StringType()]
    assert CellGuess().guess('2016-01-01 01:02:63') == [StringType()]
    assert CellGuess().guess('2016-01-01 01:02:03') == [DateType('%Y-%m-%d %H:%M:%S')]
