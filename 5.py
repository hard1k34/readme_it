spisok = [1, 4, -3, 0, 10]
n = len(spisok)
for i in range(n):
    for j in range(n - 1 - i):
        if spisok[j] > spisok[j + 1]:
            spisok[j], spisok[j + 1] = spisok[j +1 ], spisok[j]
            print(spisok)
