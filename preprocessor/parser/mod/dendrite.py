from itertools import count


class Dendrite(object):
    """"""

    id: int = count(0)

    def __init__(
        self,
        inp: str,
        inm: str,
        outp: str,
        outm: str,
        a1: str,
        a2: str,
        a3: str,
        a4: str,
        a5: str,
        a6: str,
        b1: str,
        b2: str,
        b3: str,
        b4: str,
        b5: str,
        b6: str,
        vss: str,
        vdd: str,
    ) -> None:
        self.id = next(id)
        self._inp: str = inp
        self._inm: str = inm
        self._outp: str = outp
        self._outm: str = outm
        self._a1: str = a1
        self._a2: str = a2
        self._a3: str = a3
        self._a4: str = a4
        self._a5: str = a5
        self._a6: str = a6
        self._b1: str = b1
        self._b2: str = b2
        self._b3: str = b3
        self._b4: str = b4
        self._b5: str = b5
        self._b6: str = b6
        self._vss: str = vss
        self._vdd: str = vdd

    def __str__(self) -> str:
        return f"xDENDRITE{self.id} {self._inp} {self._inm} {self._outp} {self._outm} {self._a1} {self._a2} {self._a3} {self._a4} {self._a5} {self._a6} {self._b1} {self._b2} {self._b3} {self._b4} {self._b5} {self._b6}"
