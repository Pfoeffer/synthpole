# Make a 1 hz sound wave

import numpy as np

def init(file):
    x = [0, 0,0,0,0,0,0,0,0,0,0]
    L, N = 1, 10
    h = L/N
    i = 1
    while i <= N:
        x.append(N / i*L)
        i += 1
    with open(file, 'w') as f:
        f.writelines(x)
        
    return x

def run(file):
    n = init(file)
    with(open(file, 'r')) as f:
        lll = f.readlines()
        print(lll)
    if len(lll) == 0:
        return "Error"

# Create x array

#init(x, l, h)
run('signal.txt')