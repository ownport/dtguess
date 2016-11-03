

from utils import get_default_instances


class CellGuess():

    def __init__(self, type_instances=get_default_instances()):

        if not isinstance(type_instances, (list, tuple)):
            raise RuntimeError('Type instances shall be list or tuple of types, %s' % type(type_instances))
        self._type_instances = type_instances

    def guess(self, value):

        guesses = []
        for t in self._type_instances:
            if t.test(value):
                guesses.append((t.guessing_weight, t))
        max_weight = max([g[0] for g in guesses])
        return [g[1] for g in guesses if g[0] == max_weight]
