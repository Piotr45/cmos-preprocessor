from itertools import count


class CMRRBlock(object):
    """"""

    id = count(0)

    def __init__(self) -> None:
        self.id = next(self.id)
        self._input_positive: str = None
        self._input_negative: str = None
        self._output_positive: str = None
        self._output_negative: str = None
        self._vss: str = None
        self._vdd: str = None
        return

    def __str__(self) -> str:
        return f"xCM{self.id} {self._input_positive} {self._input_negative}"
