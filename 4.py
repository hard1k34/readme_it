word = input("Ввелите слово ")
res_word = word[::1]
if res_word == word:
    print("Слово является палиндромом")
else: print("Слово НЕ является палиндромом")

