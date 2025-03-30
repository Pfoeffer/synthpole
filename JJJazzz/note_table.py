M, J = 12, 12
m, j = 0, 0
notes = []

while m < M:
    while j < J:
        notes[m][j] = 0
        j+=1
    m+=1
print(notes)