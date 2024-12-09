class Circuit:

    def __init__(self):
        self.wires_instructions: dict[str, str] = {}
        self.wires_power: dict[str, int] = {}
        with open('7.txt') as f:
            for line in f:
                instruction, wire = line.rstrip().split(' -> ')
                self.wires_instructions[wire] = instruction

    def __getitem__(self, wire: str) -> int:
        if wire.isdigit():
            return int(wire)
        elif wire not in self.wires_power:
            self.wires_power[wire] = self.__get_power_from_instruction(wire) & 0xFFFF
        return self.wires_power[wire]

    def __setitem__(self, wire: str, power: int):
        self.wires_power[wire] = power

    def __get_power_from_instruction(self, wire: str) -> int:
        match self.wires_instructions[wire].split():

            case [wire_from]:
                return self[wire_from]

            case [wire_from, shift, shift_impulsion] if shift in {'RSHIFT', 'LSHIFT'}:
                wire_, shift_ = self[wire_from], int(shift_impulsion)
                return wire_ << shift_ if shift == 'LSHIFT' else wire_ >> shift_

            case [wire_from_a, instruction, wire_from_b] if instruction in {'OR', 'AND'}:
                wire_a, wire_b = self[wire_from_a], self[wire_from_b]
                return wire_a & wire_b if instruction == 'AND' else wire_a | wire_b

            case ['NOT', wire_from]:
                return ~self[wire_from]

            case unscheduled_instruction:
                err = Exception("Instruction non prévue")
                err.add_note(unscheduled_instruction)
                raise err


circuit = Circuit()

first_a = circuit['a']
print(first_a)

circuit.wires_power.clear()
circuit['b'] = first_a
print(circuit['a'])
