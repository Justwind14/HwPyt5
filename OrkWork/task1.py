# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

with open ('c:/Users/justwind/Desktop/PytSem5/OrkWork/file.txt', 'r', encoding='UTF-8') as file:
    S = file.read()
    print(S)
    listS = list(map(str, S.split()))
    i=0
    for _ in range(len(listS)):
        if 'а' in listS[i] or 'б' in listS[i] or 'в' in listS[i]:
            listS.remove(listS[i])
        else:
            i += 1
    print(listS)