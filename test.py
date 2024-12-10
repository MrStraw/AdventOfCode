# import timeit
# 
# # Tester les différentes méthodes
# setup = "way_ = [1, 2, 3, 4, 5]; next_cell = 6"
# 
# method1 = "new_list = way_.copy() + [next_cell]"
# method2 = "new_list = way_[:] + [next_cell]"
# method3 = "new_list = list(way_) + [next_cell]"
# method4 = "new_list = [*way_, next_cell]"
# 
# print("Method 1:", timeit.timeit(method1, setup=setup, number=1000000))
# print("Method 2:", timeit.timeit(method2, setup=setup, number=1000000))
# print("Method 3:", timeit.timeit(method3, setup=setup, number=1000000))
# print("Method 4:", timeit.timeit(method4, setup=setup, number=1000000))
import itertools
from datetime import datetime

start = datetime.now()
for i in itertools.permutations(range(11)):
    # for y in itertools.pairwise((*i, i[0])):
    #     pass
    pass
print(datetime.now() - start)
