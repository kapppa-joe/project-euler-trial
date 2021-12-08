names = ''
with open('constant_inputs/p022_names.txt', 'r') as f:
    names = f.read()

Q022_names = names.replace('"', '').split(',')
