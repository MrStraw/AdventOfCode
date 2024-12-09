raw, interpreted, encoded = 0, 0, 0

with open('8.txt') as f:
    for line_raw in f:
        line_raw = line_raw.rstrip()
        interpreted_content = eval(line_raw)
        
        raw += len(line_raw)
        interpreted += len(interpreted_content)
        encoded_len = len(line_raw) + line_raw.count(r'"') + line_raw.count('\\') + 2
        print(line_raw, encoded_len)
        encoded += encoded_len
print()
print(raw - interpreted)
print(encoded - raw)
