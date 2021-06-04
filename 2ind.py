# /usr/bin/env python3
# -*- coding: utf-8 -*-

import json

if __name__ == '__main__':
    with open("ks.json", 'w') as f:
        json.dump(f)
    with open("ks.json", "r") as f:
        text = json.load(f)
    # Заменить символы конца предложения.
    text = text.replace("!", ".")
    text = text.replace("?", ".")
    # Удалить все многоточия.
    while ".." in text:
        text = text.replace("..", ".")
    # Разбить текст на предложения.
    sentences = text.split(".")
    words = text.split(" ")
    # Вывод предложений с запятыми.
    print(text)
    answer = ""
    sCaps = text.title()
    #  Делает все первые буквы слов заглавными
    for letter in sCaps:
        if (letter not in "aeiouAEIOU"):
            answer = answer + letter.lower()
        else:
            answer = answer + letter
        # проверяет каждую букву, если она не гласная делает ее маленькой\
    print(answer)
