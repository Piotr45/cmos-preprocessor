from itertools import count


class Diode(object):
    """"""

    id: int = count(0)

    def __init__(self, input: str, vss: str, vdd: str) -> None:
        self.id: int = next(self.id)
        self._in: str = input
        self._vss: str = vss
        self._vdd: str = vdd

    def __str__(self) -> str:
        return f"D{self.id} {self._in} {self._vss} {self._vdd}"
