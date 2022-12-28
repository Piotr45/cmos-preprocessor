from itertools import count


class Axon(object):
    """"""

    id: int = count(0)

    def __init__(self, inm: str, outp: str, outm: str, vss: str, vdd: str) -> None:
        self.id: int = next(self.id)
        self._inp: str = inm
        self._inm: str = inm
        self._outp: str = outp
        self._outm: str = outm
        self._vss: str = vss
        self._vdd: str = vdd

    def __str__(self) -> str:
        return f"xAK{self.id} {self._inp} {self._inm} {self._outp} {self._outm} {self._vss} {self._vdd}"
