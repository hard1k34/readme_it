films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
favorite = []
print("Сколько фильмов хотите добавить ")
kolvo = int(input("Количество "))
for i in range(kolvo):
    love = input(f"Введите название {i+1} фильма ")
    if love in films:
        favorite.append(love)
    else:
        print("Такого фильма не найдено")

print(f"Ваши любимые фильма: {favorite}")

