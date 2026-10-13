spisok = []
pervoya = int(input("Введите количество видеокарт "))
for i in range(pervoya):
    model = int(input(f"{i+1} Видеокарта "))
    spisok.append(model)
print(f"Старый список {spisok}")
max_card = max(spisok)
while max_card in spisok:
    spisok.remove(max_card)
print(print(f"новый список {spisok}"))



