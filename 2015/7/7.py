class Circuit:

    def __init__(self):
        self.signals_provides: dict[str, int] = {}
        self.wires_instructions: dict[str, set[tuple[str, str]]] = {}  # in vers instruction, out
        with open('7.txt') as f:
            for line in f:
                match line.split():

                    case [value, '->', wire_in]:
                        self.wires_instructions[wire_in] = value

                    case [wire_in_a, shift, impulsion, '->', wire_out] if shift.endswith('SHIFT'):
                        if wire_in not in self.wires_instructions:
                            self.wires_instructions[wire_in] = set()
                        self.wires_instructions[wire_in].add((f'{shift} {impulsion}'), wire_out)

                    case [wire_in_a, instruction, wire_in_b, '->', wire_out] if not wire_in_b.isdigit():
                        if wire_in_a not in self.wires_instructions:
                            self.wires_instructions[wire_in_a] = set()
                        self.wires_instructions[wire_in_a].add(f'{instruction} {impulsion}')

                    case [instruction, wire_in, '->', wire_out]:
                        print(instruction, wire_in, "dans", wire_out)

                    case whut:
                        print(whut)


circuit = Circuit()
