
from collections import defaultdict

import types


def get_default_instances():

    return [
        types.StringType(), types.DecimalType(), types.IntegerType(),
        types.DateType('%Y-%m-%d %H:%M:%S'), types.BooleanType()
    ]


def type_guess(rows, types=types.DEFAULT_TYPES, strict=False):
    """ The type guesser aggregates the number of successful
    conversions of each column to each type, weights them by a
    fixed type priority and select the most probable type for
    each column based on that figure. It returns a list of
    ``CellType``. Empty cells are ignored.

    Strict means that a type will not be guessed
    if parsing fails for a single cell in the column."""
    guesses = []
    type_instances = [i for t in types for i in t.instances()]
    if strict:
        at_least_one_value = []
        for ri, row in enumerate(rows):
            diff = len(row) - len(guesses)
            for _ in range(diff):
                typesdict = {}
                for type in type_instances:
                    typesdict[type] = 0
                guesses.append(typesdict)
                at_least_one_value.append(False)
            for ci, cell in enumerate(row):
                if not cell.value:
                    continue
                at_least_one_value[ci] = True
                for type in list(guesses[ci].keys()):
                    if not type.test(cell.value):
                        guesses[ci].pop(type)
        # no need to set guessing weights before this
        # because we only accept a type if it never fails
        for i, guess in enumerate(guesses):
            for type in guess:
                guesses[i][type] = type.guessing_weight
        # in case there were no values at all in the column,
        # we just set the guessed type to string
        for i, v in enumerate(at_least_one_value):
            if not v:
                guesses[i] = {types.StringType(): 0}
    else:
        for i, row in enumerate(rows):
            diff = len(row) - len(guesses)
            for _ in range(diff):
                guesses.append(defaultdict(int))
            for i, cell in enumerate(row):
                # add string guess so that we have at least one guess
                guesses[i][types.StringType()] = guesses[i].get(types.StringType(), 0)
                if not cell.value:
                    continue
                for type in type_instances:
                    if type.test(cell.value):
                        guesses[i][type] += type.guessing_weight
        _columns = []
    _columns = []
    for guess in guesses:
        # this first creates an array of tuples because we want the types to be
        # sorted. Even though it is not specified, python chooses the first
        # element in case of a tie
        # See: http://stackoverflow.com/a/6783101/214950
        guesses_tuples = [(t, guess[t]) for t in type_instances if t in guess]
        _columns.append(max(guesses_tuples, key=lambda t_n: t_n[1])[0])
    return _columns


def types_processor(types, strict=False):
    """ Apply the column types set on the instance to the
    current row, attempting to cast each cell to the specified
    type.

    Strict means that casting errors are not ignored"""
    def apply_types(row_set, row):
        if types is None:
            return row
        for cell, type in izip_longest(row, types):
            try:
                cell.value = type.cast(cell.value)
                cell.type = type
            except:
                if strict and type:
                    raise
        return row
    return apply_types
