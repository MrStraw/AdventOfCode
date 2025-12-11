import heapq

ti = tuple[int, ...]


class Machine:
    def __init__(self, power_need: str, butons: list[str]):
        self.power_need: ti = tuple(int(i) for i in power_need.strip('{}').split(','))
        self.butons: tuple[ti, ...] = tuple(tuple(
            int(i in {int(led_pos) for led_pos in buton_schema.strip('()').split(',')})
            for i in range(len(self.power_need))) for buton_schema in butons)
        self._range_butons: range = range(len(self.butons))
        self._range_power: range = range(len(self.power_need))

    def find_quikest(self) -> int | None:
        def heuristic(current):
            return max(self.power_need[i] - current[i] for i in self._range_power)
        initial_joltage = tuple(0 for _ in self._range_power)
        start_h = heuristic(initial_joltage)
        queue = [(start_h, 0, initial_joltage)]
        seen_joltages = {initial_joltage}
        while queue:
            est_score, steps, current_joltage = heapq.heappop(queue)
            if current_joltage == self.power_need:
                return steps
            for i in self._range_butons:
                new_joltage = tuple(current_joltage[k] + self.butons[i][k] for k in self._range_power)
                if new_joltage in seen_joltages or any(new_joltage[k] > self.power_need[k] for k in self._range_power):
                    continue
                seen_joltages.add(new_joltage)
                h = heuristic(new_joltage)
                heapq.heappush(queue, (steps + 1 + h, steps + 1, new_joltage))
        return None


total = 0
for machine_schema in open('prod.txt'):
    _, *butons, powers_need = machine_schema.strip().split(' ')
    total += Machine(powers_need, butons).find_quikest()
print(total)
