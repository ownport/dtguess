

from utils import get_default_instances
from collections import Counter


class Guess(object):

    def __init__(self, type_instances=get_default_instances()):

        if not isinstance(type_instances, (list, tuple)):
            raise RuntimeError('Type instances shall be list or tuple of types, %s' % type(type_instances))
        self._type_instances = type_instances
        self._guesses = dict()

    def clear(self):
        ''' clear previuos guesses
        '''
        self._guesses = dict()

    def max_weight(self):
        ''' returns instance type(-s) with max weight
        '''
        if len(self._guesses) > 0:
            max_weight = max([g.guessing_weight for g in self._guesses])
            return [g for g in self._guesses if g.guessing_weight == max_weight]
        else:
            return []

    def min_weight(self):
        ''' returns instance type(-s) with min weight
        '''
        if len(self._guesses) > 0:
            min_weight = min([g.guessing_weight for g in self._guesses])
            return [g for g in self._guesses if g.guessing_weight == min_weight]
        else:
            return []


class CellGuess(Guess):

    def guess(self, value):

        self.clear()
        for t in self._type_instances:
            if t.test(value) and t not in self._guesses:
                self._guesses[t] = 1
        return self.max_weight()


class ColumnGuess(Guess):


    def __init__(self, type_instances=get_default_instances()):

        super(ColumnGuess, self).__init__(type_instances)
        self._cells_count = 0

    def guess(self, column):

        if not isinstance(column, (list, tuple)):
            raise RuntimeError('The column shall be a list or tuple of cells, %s' % type(column))

        self.clear()
        cell_guess = CellGuess(self._type_instances)
        for ci, cell in enumerate(column):
            for _cell_type in cell_guess.guess(cell):
                if _cell_type not in self._guesses:
                    self._guesses[_cell_type] = 1
                else:
                    self._guesses[_cell_type] += 1

        if len(self._guesses) > 0:
            self._cells_count = ci + 1
            return self.min_weight()
        else:
            return None


    def stats(self):
        ''' return guessing stats
        '''
        return {'cells_count': self._cells_count, 'guesses': self._guesses}
