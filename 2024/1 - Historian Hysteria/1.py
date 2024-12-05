dict_l, dict_r = {}, {}
all_ids = set()

with open('input.txt') as f:
    for row in f:
        id_l = int(row[:5])
        id_r = int(row[8:13])
        dict_l[id_l] = 1 if id_l not in dict_l else dict_l[id_l] + 1
        dict_r[id_r] = 1 if id_r not in dict_r else dict_r[id_r] + 1
        all_ids.add(id_l)
        all_ids.add(id_r)

similarity = 0
for id_ in all_ids:
    similarity += id_ * dict_l.get(id_, 0) * dict_r.get(id_, 0)

print(format(similarity, ','))
# 19678534