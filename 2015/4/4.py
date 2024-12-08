from hashlib import md5

secret_key, code = 'yzbqklnj', 0
while not md5(f'{secret_key}{code}'.encode()).hexdigest().startswith('0' * 5):
    code += 1

print(code)
