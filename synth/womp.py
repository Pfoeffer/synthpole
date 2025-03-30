"""
% Boom.
where we at?

space is so convoluted. It's not even funny.'
'Thanks for the speech recognition, I guess. I just gotta THINK about the next words I've gotta say.
where we at?

import numpy as np
import 

the motherload 
"""

'''
Maybe I should use python to solve the equations.
'''
import math as m
import scipy as s
import sys as y
import random as r
import os as o
import time as t
import numpy as n
#import pyqt6 as g

import sounddevice as a

def playNote(tone, duration):
    fs, dt = 44100, duration
    N = int(fs * dt)
    f = fq(tone)
    tab = n.linspace(0, dt, N, endpoint=False)# What does the last condition mean?
    samples = n.sin(2*m.pi*f*tab) # Sine blip
    print("Playing")
    a.play(samples, fs)
    a.wait()
    print("Sample over")

def makeNotes(A0, names):
    names=names
    notes = {}
    for i in range(144):
        octave = i // 12
        note_idx = i % 12
        note = names[note_idx]
        fn = A0 * 2 ** (note_idx/12) * 2 ** octave
        var_name = f'n{note}{octave}'
        notes[var_name] = fn
    return notes

def fq(note):
    names = ['A', 'Ab', 'G', 'Gb', 'F', 'E', 'Eb', 'D', 'Db', 'C', 'B', 'Bb']
    A0 = 440.0 / 2 ** 4
    notes = makeNotes(A0, names)
    return notes[note]

playNote("nAb4", .25)
playNote("nF4", .25)
playNote("nF3", .1)
playNote("nC3", .1)
playNote("nBb2", .5)


"""
#1. fully define x axis
a, b = 0, m.pi #Interval
N = 100 #Amount of pieces
x = n.linspace(a, b, N) # == x vector
h = (b - a) / (N - 1) # h
#2. We're solving for the same amount of points.
# So solution vector of length N, using A [N x N]
A, Y = n.zeros(N, N), n.zeros(N)
#3. Introduce function
Q, R = 10, 1
#4. Build interior...
for i in range(1, N-1):
    A[i, i] = -1 / h
    A[i, i-1] = 2 / h + Q*h
    A[i+1, 1] = -1 / h
#5. Apply boundary coditions
A


# Solve the system

zQ, zR = 9.9, 1
"""