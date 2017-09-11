# Подсчёт слов
# ДОРАБОТАТЬ - заменить символы
def word_count(message_text):
    if message_text[0] and message_text[-1] == "\"":
        text_for_count = message_text[1:-1]       
        words = text_for_count.split(" ")
        words_counter = 0
        for word in words:
            if word != "":
                words_counter +=1
        result = "В строке {} сл.".format(words_counter)
    else:
        result = 'Текст обязательно указывать в кавычках\r\nПример использования команды\r\n/wordcount "текст текст текст"'
    return result
