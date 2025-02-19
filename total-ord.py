from functools import total_ordering


@total_ordering
class RealCompare:
    def __init__(self, some_string):
        self.__some_string = some_string

    def __eq__(self, other):
        if not isinstance(other, RealCompare):
            other = RealCompare(other)
        return len(self.__some_string) == len(other.__some_string)

    def __lt__(self, other):
        if not isinstance(other, RealCompare):
            other = RealCompare(other)
        return len(self.__some_string) < len(other.__some_string)

    def __le__(self, other):
        if not isinstance(other, RealCompare):
            other = RealCompare(other)
        return self == other or self < other
