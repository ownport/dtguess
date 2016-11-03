# dtguess

[![Build Status](https://travis-ci.org/ownport/data-type-guess.svg?branch=master)](https://travis-ci.org/ownport/data-type-guess)

Data type guessing library

## How to install

to be described later

## How to use


```python
from dtguess import StringType, IntegerType, DecimalType, BooleanType, \
                DateType,  DateUtilType

from dtguess import CellGuess

assert CellGuess().guess(None) == [BooleanType()]

assert CellGuess().guess(5) == [IntegerType()]
assert CellGuess().guess('5') == [IntegerType()]
assert CellGuess().guess('5.0') == [IntegerType()]

assert CellGuess().guess(5.1) == [DecimalType()]
assert CellGuess().guess('5.1') == [DecimalType()]

assert CellGuess().guess('2016-01-01') == [StringType()]
assert CellGuess().guess('2016-01-01 01:02:63') == [StringType()]
assert CellGuess().guess('2016-01-01 01:02:03') == [DateType('%Y-%m-%d %H:%M:%S')]

```
Default types for guessing are:
- StringType()
- IntegerType()
- DecimalType()
- BooleanType()
- DateType('%Y-%m-%d %H:%M:%S')
