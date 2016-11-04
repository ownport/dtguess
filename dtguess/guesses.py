

from utils import get_default_instances


class Guess(object):

    def __init__(self, type_instances=get_default_instances()):

        if not isinstance(type_instances, (list, tuple)):
            raise RuntimeError('Type instances shall be list or tuple of types, %s' % type(type_instances))
        self._type_instances = type_instances


class CellGuess(Guess):

    def guess(self, value):

        guesses = []
        for t in self._type_instances:
            if t.test(value):
                guesses.append((t.guessing_weight, t))
        if len(guesses) > 0:
            max_weight = max([g[0] for g in guesses])
            return [g[1] for g in guesses if g[0] == max_weight]
        else:
            return []


class ColumnGuess(Guess):


    def __init__(self, type_instances=get_default_instances()):

        super(ColumnGuess, self).__init__(type_instances)
        self._cells = 0
        self._guesses = dict()


    def guess(self, column):

        if not isinstance(column, (list, tuple)):
            raise RuntimeError('The column shall be a list or tuple of cells, %s' % type(column))

        cell_guess = CellGuess(self._type_instances)
        for ci, cell in enumerate(column):
            for _cell_type in cell_guess.guess(cell):
                if _cell_type not in self._guesses:
                    self._guesses[_cell_type] = 1
                else:
                    self._guesses[_cell_type] += 1

        self._cells = ci + 1 if ci else 0
        return self._cells, self._guesses


    def stats(self):
        ''' return guessing stats
        '''
        return self._cells, self._guesses
