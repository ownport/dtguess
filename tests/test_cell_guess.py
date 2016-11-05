
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


def test_cell_guess_column_guess_one_type():

    column = [1,2,3,4,5]
    cg = ColumnGuess()
    assert cg.guess(column) == [IntegerType()]
    assert cg.stats() == {'cells_count': 5, 'guesses': {IntegerType(): 5}}


def test_cell_guess_column_guess_mixed_types():

    column = ['a',2,'b',4,'c']
    cg = ColumnGuess()
    assert cg.guess(column) == [StringType()]
    assert cg.stats() == {'cells_count': 5, 'guesses': {IntegerType(): 2, StringType(): 3}}

    column = ['',2,'b',4,'c']
    cg = ColumnGuess()
    assert cg.guess(column) == [StringType()]
    assert cg.stats() == {'cells_count': 5, 'guesses': {IntegerType(): 2, StringType(): 2}}

    column = [.1, 2, 2.1, 4, .9]
    cg = ColumnGuess()
    assert cg.guess(column) == [DecimalType()]
    assert cg.stats() == {'cells_count': 5, 'guesses': {IntegerType(): 2, DecimalType(): 3}}
