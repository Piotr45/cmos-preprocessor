import numpy as np


class ModelParser:
    """"""

    def __init__(self, neural_network: np.array, grid: dict[str, float]) -> None:
        self._input_size: int = len(neural_network[0])
        self._input: np.array  = neural_network[0]
        self._layers: np.array  = neural_network[1:-1]
        self._output: np.array = neural_network[-1].reshape((1, -1))
        self._grid: dict = grid
        return

    def parse_model(self) -> str:
        result = []
        current_mirrors = []
        current_inputs = [f"IN{i}p IN{i}m" for i in range(self._input_size)]
        preprocessor_outputs = [f"OUT{i}p OUT{i}m" for i in range(len(self._output))]

        includes = f"*** PREPROCESSOR\n.INCLUDE components/AXON.sp\n.INCLUDE components/DENDRITE.sp\n.INCLUDE components/CMRR.sp\n\n"
        preamble = f".subckt PREPROCESSOR {' '.join(current_inputs)} {' '.join(preprocessor_outputs)} VSS VDD\n\n"
        result.append(includes)
        result.append(preamble)
        
        result += self._create_current_mirrors(current_inputs, current_mirrors)
        result += self._create_layer(self._input, 0, current_mirrors)
        result += self._create_layer(self._output, 1, current_mirrors, preprocessor_outputs)

        result.append(f".ends PREPROCESSOR")
        return "".join(result)

    def _create_current_mirrors(self, current_inputs: list, current_mirrors: list) -> list:
        result = []
        for i in range(self._input_size):
            inp, inm = current_inputs[i].split(' ')
            cmp = f"xCMp_{i} {inp} OUTn_n1p{i} OUTn_n2p{i} VSS VDD CM2\n"
            cmm = f"xCMm_{i} {inm} OUTp_n1p{i} OUTp_n2p{i} VSS VDD CM2\n"
            result.append(cmp)
            result.append(cmm)
            current_mirrors.append((f"OUTn_n1p{i}", f"OUTp_n1p{i}"))

        result.append("\n")
        return result

    def _create_layer(self, weights: list, n: int, current_mirrors: list, preprocessor_outputs: list = None) -> list:
        result = []
        layer_size = len(weights)

        # Weights
        for i in range(layer_size):
            res = []
            wg = [w[i] for w in weights]
            for j, weight in enumerate(wg):
                prefix = f"xDENDRYTw{n}n{i}d{j}"
                if weight < 0: # zamienić na > jeśli będą odwrotne połączenia 
                    inputs = " ".join(reversed(current_mirrors[i]))
                else:
                    inputs = " ".join(current_mirrors[i])
                
                outputs = f"OUTmw{n}_n{i} OUTpw{n}_n{i}"

                code = self._find_closest_weight(self._grid, weight)
                weight_vector = " ".join(self.parse_weight_vector(code))
                
                suffix = "VSS VDD DENDRYT\n"
                res.append(" ".join([prefix, inputs, outputs, weight_vector, suffix]))
            result += res
            result.append("\n")

        # Activation
        for i in range(layer_size):
            axon = f"xAKSONw{n}n{i} OUTpw{n}_n{i} OUTmw{n}_n{i} OUTp_w{n}n{i} OUTm_w{n}n{i} VSS VDD AKSON\n"
            result.append(axon)
        result.append("\n")

        current_mirrors = []
        # CMMRR
        for i in range(layer_size):
            # .subckt CMRR inp inm outp outm vss vdd
            if preprocessor_outputs:
                outp, outm = preprocessor_outputs[i].split(' ')
                cmrr = f"xCMRRw{n}n{i} OUTp_w{n}n{i} OUTm_w{n}n{i} {outp} {outm} VSS VDD CMRR\n" 
            else:
                cmrr = f"xCMRRw{n}n{i} OUTp_w{n}n{i} OUTm_w{n}n{i} INw2p_n{n+1}p{i} INw2m_n{n+1}p{i} VSS VDD CMRR\n" 
                current_mirrors.append(f"INw2p_n{n+1}p{i} INw2m_n{n+1}p{i}")
            result.append(cmrr)
        result.append("\n")

        return result

    @staticmethod
    def parse_weight_vector(weight_vector) -> str:
        if len(weight_vector) != 12:
            raise ValueError(f"Bad vector length ({len(weight_vector)} != 12)!")
        res = []
        for value in weight_vector:
            if value == '0':
                res.append("VSS")
            if value == '1':
                res.append("VDD")
        return res
    
    @staticmethod
    def _find_closest_weight(grid: dict, target: float) -> str:
        def getClosest(val1, val2, target):
            if (target - val1 >= val2 - target):
                return val2
            else:
                return val1

        arr = [value for _, value in grid.items()]
        codes = [key for key, _ in grid.items()]
        n = len(arr)

        if (target <= arr[0]):
            return codes[0]
        if (target >= arr[n - 1]):
            return codes[n - 1]

        i = 0; j = n; mid = 0
        while (i < j):
            mid = (i + j) // 2
            if (arr[mid] == target):
                return codes[mid]
            if (target < arr[mid]) :
                if (mid > 0 and target > arr[mid - 1]):
                    val = getClosest(arr[mid - 1], arr[mid], target)
                    return codes[arr.index(val)]
                j = mid
            else :
                if (mid < n - 1 and target < arr[mid + 1]):
                    val = getClosest(arr[mid], arr[mid + 1], target)
                    return codes[arr.index(val)]
                i = mid + 1

        return codes[mid]