# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

from task3part2 import Recovery

def Compression(S):
    with open('compression.txt', 'w') as pr:              
        k = 1
        leng = len(S)      
        for i in range(1, leng):
            if S[i] == S[i-1]:
                k += 1
                if i == leng-1:
                    pr.write(f'{k}{S[i]}')
            elif S[i] != S[i-1]:
                pr.write(f'{k}{S[i-1]}')
                k = 1
                if i == leng-1:
                    pr.write(f'{k}{S[i]}')


S = 'AAAAAAAAAAAAAAAAAAAAAAAAAAlarisaBBCAA'
with open('compression.txt', 'r') as readrec:
    rec = readrec.read()
Compression(S)
Recovery(rec)
