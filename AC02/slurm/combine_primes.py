#!/bin/python3

import os

files = os.listdir('./results');
files.sort(key=lambda x: int(x[6:-4]))
suma = ''

for result in filter(lambda x: x.endswith('out'), files):
    with open('./results/' + result, 'r') as f:
        suma += f.read()

with open('results.out', 'w') as f:
    f.write(suma)





