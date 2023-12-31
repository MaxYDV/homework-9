import re  # Вывел библиотеку регулярных выражений

# Создал переменную в которую буду записывать некий текст
some_txt = ""
# Открыл  файл  для чтения
with open("start_file.txt", "r") as my_start_file:
    # Создал цыкл который перебрал весь текст посимвольно и обьеденил все в одну строку ( я знаю что можно было сразу весь текст передать решил так сделать для себя для практики)
    for row in my_start_file:
        for letter in row:
            some_txt = some_txt + letter

# Создал регулярку нахождения слов (я использовал в середине слова дополнительный символ который не обязателен но в английском может присутствовать как для короткой записи ('))
# И записал все в лист.
find_words = re.findall(r"[a-zA-Z]{1,20}[']*[a-zA-Z]{,20}", some_txt)

# Вывел длину листа, поскольку в листе каждая запись является словом, то его длина = количеству слов
print(f"Количество слов в тексте: {len(find_words)}")

# Записал в новый файл все слова из  предыдущего текста которые равны 7 или более букв
with open("final_file.txt", "w") as final_file:
    for i in find_words:
        if len(i) >= 7:
            final_file.write(f"- {i}\n")

# Вывел все слова длиной 7 и более букв
with open("final_file.txt", "r") as final_file:
    print(f"Слова из 7 и более букв из текста: \n{final_file.read()}")

# Свою задачу выполняет.  Есть куча способов улучшения))