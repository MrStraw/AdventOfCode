from hashlib import md5

secret_key = 'yzbqklnj'
code = 1
while not md5(f'{secret_key}{code}'.encode()).hexdigest().startswith('0'*6):
    code += 1
print(code)
print(md5(f'{secret_key}{code}'.encode()).hexdigest())

