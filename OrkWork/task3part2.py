def Recovery(rec):
    numbers = '0123456789'
    factor = rec[0]
    with open('recovery.txt', 'w') as rc:
        for i in range(1,len(rec)):
            if rec[i] in numbers:
                factor = factor + rec[i]
            else:
                rc.write(int(factor)*rec[i])
                factor = ''