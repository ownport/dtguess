
from dtguess import StringType, IntegerType, DecimalType, BooleanType, \
                DateType,  DateUtilType

from dtguess import CellGuess
from dtguess import ColumnGuess


def test_cell_guess_basic_types():

    assert CellGuess().guess(None) == []

    assert CellGuess().guess(5) == [IntegerType()]
    assert CellGuess().guess('5') == [IntegerType()]
    assert CellGuess().guess('5.0') == [IntegerType()]

    assert CellGuess().guess(5.1) == [DecimalType()]
    assert CellGuess().guess('5.1') == [DecimalType()]

    assert CellGuess().guess('2016-01-01') == [StringType()]
    assert CellGuess().guess('2016-01-01 01:02:63') == [StringType()]
    assert CellGuess().guess('2016-01-01 01:02:03') == [DateType('%Y-%m-%d %H:%M:%S')]


def test_cell_guess_column_guess():

    column = [1,2,3,4,5]
    cg = ColumnGuess()

    assert cg.guess(column) == (5, {IntegerType(): 5})
    assert cg.stats() == (5, {IntegerType(): 5})
