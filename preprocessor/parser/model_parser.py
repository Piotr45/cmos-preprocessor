import numpy as np


class ModelParser:
    """Parser class, that converts TensorFlow model to spice component"""

    def __init__(self, neural_network: np.array, grid: dict[str, float]) -> None:
        self._input_size: int = len(neural_network[0])
        self._input: np.array = neural_network[0]
        self._output: np.array = neural_network[-1].reshape((1, -1))
        self._grid: dict = grid
        self._current_mirrors: list = []
        return

    def parse_model(self) -> str:
        """Parse TF model to preprocessor structure

        Return:
            str: Preprocessor structure
        """

        # Init inputs and outputs of preprocessor
        result = []
        current_inputs = [f"IN{i}p IN{i}m" for i in range(self._input_size)]
        preprocessor_outputs = [f"OUT{i}p OUT{i}m" for i in range(len(self._output))]

        # Create file preamble
        includes = f"*** PREPROCESSOR\n.INCLUDE components/AXON.sp\n.INCLUDE components/DENDRITE.sp\n.INCLUDE components/CMRR.sp\n\n"
        preamble = f".subckt PREPROCESSOR {' '.join(current_inputs)} {' '.join(preprocessor_outputs)} VSS VDD\n\n"
        result.append(includes)
        result.append(preamble)

        # Create preprocessor structure
        result += self._generate_current_mirrors(current_inputs)
        result += self._create_layer(self._input, 0)
        result += self._create_layer(self._output, 1, preprocessor_outputs)

        # End preprocessor structure
        result.append(f".ends PREPROCESSOR\n\n")

        # Create CM component structure
        result += self._generate_cm_component(self._input_size)

        return "".join(result)

    def _create_layer(
        self, weights: list, n: int, preprocessor_outputs: list = None
    ) -> list:
        """Creates layer of the neural network

        Args:
            weights (list): list of weights in layer
            n (int): layer number

        Return:
            List[str]: neural network layer structure for preprocessor circuit
        """
        result = []
        layer_size = len(weights)

        # Create multiplying blocks
        result += self._generate_dendrite_component(weights, n, preprocessor_outputs)

        # Create activation blocks and link them with multiplying blocks
        result += self._generate_axon_component(layer_size, n)

        # Create CMRR blocks and link them with activation functions
        result += self._generate_cmrr_component(layer_size, n, preprocessor_outputs)

        return result

    def _generate_current_mirrors(self, current_inputs: list) -> list:
        """Create current mirrors to prepare preprocessor input values for further processing

        Args:
            current_inputs (list): current voltage source values, that we want to duplicate

        Return:
            List[str]: spice code structure for CM components
        """
        result = []
        current_mirrors = []
        for i in range(self._input_size):
            inp, inm = current_inputs[i].split(" ")

            outs_p = [f"OUTn_n{j}p{i}" for j in range(self._input_size)]
            outs_m = [f"OUTp_n{j}p{i}" for j in range(self._input_size)]

            cmp = f"xCMp_{i} {inp} {' '.join(outs_p)} VSS VDD CM{self._input_size}\n"
            cmm = f"xCMm_{i} {inm} {' '.join(outs_m)} VSS VDD CM{self._input_size}\n"

            result.append(cmp)
            result.append(cmm)

            current_mirrors.append(list(zip(outs_p, outs_m)))

        self._current_mirrors = current_mirrors
        result.append("\n")
        return result

    def _generate_dendrite_component(
        self, weights: list, n: int, is_output_layer: bool = False
    ) -> list[str]:
        """Generate dendrite components based on TF model weights

        Args:
            weights (list): list of weights in layer
            n (int): layer number
            is_output_layer (bool): bool value for determining the output layer

        Return:
            List[str]: spice code structure for dendrite components
        """
        result = []
        layer_size = len(weights)

        # Create multiplying blocks
        for i in range(layer_size):
            res = []
            if is_output_layer:
                wg = weights[i]
            else:
                wg = [w[i] for w in weights]

            for j, weight in enumerate(wg):
                prefix = f"xDENDRYTw{n}n{i}d{j}"
                if weight < 0 and is_output_layer:
                    inputs = " ".join(reversed(self._current_mirrors[j]))
                elif weight < 0 and not is_output_layer:
                    inputs = " ".join(reversed(self._current_mirrors[j][i]))
                elif weight >= 0 and is_output_layer:
                    inputs = " ".join(reversed(self._current_mirrors[j]))
                else:
                    inputs = " ".join(self._current_mirrors[j][i])

                outputs = f"OUTmw{n}_n{i} OUTpw{n}_n{i}"

                code = self._find_closest_weight(self._grid, weight)
                weight_vector = " ".join(self._parse_bit_word(code))

                suffix = "VSS VDD DENDRYT\n"
                res.append(" ".join([prefix, inputs, outputs, weight_vector, suffix]))
            result += res
            result.append("\n")
        return result

    def _generate_cmrr_component(
        self, layer_size: int, n: int, preprocessor_outputs: list[str] = None
    ) -> list[str]:
        """Generate CMRR components based on TF model weights

        Args:
            layer_size (int): size of layer
            n (int): layer number
            preprocessor_outputs (list): outputs of preprocessor component

        Return:
            List[str]: spice code structure for CMRR components
        """
        result = []
        current_mirrors = []
        for i in range(layer_size):
            if preprocessor_outputs:
                outp, outm = preprocessor_outputs[0].split(" ")
                cmrr = f"xCMRRw{n}n{i} OUTp_w{n}n{i} OUTm_w{n}n{i} {outp} {outm} VSS VDD CMRR\n"
            else:
                cmrr = f"xCMRRw{n}n{i} OUTp_w{n}n{i} OUTm_w{n}n{i} INw2p_n{n+1}p{i} INw2m_n{n+1}p{i} VSS VDD CMRR\n"
                current_mirrors.append((f"INw2p_n{n+1}p{i}", f"INw2m_n{n+1}p{i}"))
            result.append(cmrr)
        result.append("\n")

        self._current_mirrors = current_mirrors

        return result

    @staticmethod
    def _generate_axon_component(layer_size: int, n: int) -> list[str]:
        """Generate axon components based on TF model weights

        Args:
            layer_size (int): size of layer
            n (int): layer number

        Return:
            List[str]: spice code structure for axon components
        """
        result = []
        for i in range(layer_size):
            axon = f"xAKSONw{n}n{i} OUTpw{n}_n{i} OUTmw{n}_n{i} OUTp_w{n}n{i} OUTm_w{n}n{i} VSS VDD AKSON\n"
            result.append(axon)
        result.append("\n")
        return result

    @staticmethod
    def _generate_cm_component(size: int) -> list[str]:
        """Generate current mirror component

        Args:
            size (int): the size of current mirror

        Return:
            List[str]: list of lines, that we will add to final preprocessor file
        """
        if size < 1:
            raise ValueError(
                "The size of CM component must be greater than or equal 1!"
            )
        result = []

        cm_name = f"CM{size}"
        cm_outputs = " ".join([f"OUT{i}" for i in range(1, size + 1)])
        preamble = f".subckt {cm_name} IN {cm_outputs} VSS VDD"

        result.append(preamble)
        result.append(
            f"Mn0 IN IN VSS VSS NCH W=0.265u L=0.835u\nMp0 IN IN VDD VDD PCH W=2.075u L=0.835u"
        )

        for i in range(1, size + 1):
            result.append(f"Mn{i} OUT1 IN VSS VSS NCH w=0.58u l=0.5u\n")
            result.append(f"Mp{i} OUT1 IN VDD VDD PCH w=2.05u l=0.5u\n")

        result.append(f".ends {cm_name}")
        return result

    @staticmethod
    def _parse_bit_word(bit_word: str) -> str:
        """Replace bits in a bit word with specific voltage source names

        Args:
            weight_vector (str):

        Return:
            str: string that contains voltage sources
        """
        if len(bit_word) != 12:
            raise ValueError(
                f"Bad bit word length! The multiplying block works on a bit word of length 12."
            )

        result = []
        for value in bit_word:
            if value == "0":
                result.append("VSS")
            if value == "1":
                result.append("VDD")
        return result

    @staticmethod
    def _find_closest_weight(grid: dict, target: float) -> str:
        """Find the nearest weight and return the bit word to it

        Args:
            grid (dict): dictionary with bit words and weights
            target (float): The value for which we want to find the nearest element in the grid

        Return:
            str: bit word for the nearesty element in the grid
        """

        def getClosest(val1, val2, target):
            if target - val1 >= val2 - target:
                return val2
            else:
                return val1

        arr = [value for _, value in grid.items()]
        codes = [key for key, _ in grid.items()]
        n = len(arr)

        if target <= arr[0]:
            return codes[0]
        if target >= arr[n - 1]:
            return codes[n - 1]

        i = 0
        j = n
        mid = 0
        while i < j:
            mid = (i + j) // 2
            if arr[mid] == target:
                return codes[mid]
            if target < arr[mid]:
                if mid > 0 and target > arr[mid - 1]:
                    val = getClosest(arr[mid - 1], arr[mid], target)
                    return codes[arr.index(val)]
                j = mid
            else:
                if mid < n - 1 and target < arr[mid + 1]:
                    val = getClosest(arr[mid], arr[mid + 1], target)
                    return codes[arr.index(val)]
                i = mid + 1

        return codes[mid]
