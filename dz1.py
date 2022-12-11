#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = "абв Напишите программу, удаляющую абв из текста все абв слова, содержащие абв буквы абв"
def filter_words(text):
    text = list(filter(lambda x: "абв" not in x, text.split()))
    return " ".join(text)

print(filter_words(text))