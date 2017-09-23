import platform
import codecs
import re
# Калькуляторы
CALC_SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','+','-','*','÷','=','.']
WORD_DIGITS_DICT = {'нуль':'0','ноль':'0','один':'1','два':'2','три':'3',
'четыре':'4','пять':'5','шесть':'6','семь':'7','восемь':'8','девять':'9'}
WORD_CALC_DICT = {'плюс':'+','минус':'-','умножить':'*'}
WORD_CALC_DICT_ALTERNATIVE = {'умножить на':'*','поделить на':'÷','разделить на':'÷'}
DELETE_WORDS = {'сколько будет':'','посчитай':''}

calc_data_dict = {}

def key_calc(text, chat_id):
    if text == "=":
        result = chat_calc(calc_data_dict.get(chat_id) + '=')        
        calc_data_dict[chat_id] = None
    else:
        if calc_data_dict.get(chat_id) == None:
            calc_data_dict[chat_id] = text
        else:
            calc_data_dict[chat_id] += text
        result = 'calc_continue'
    return result

def clear_calc(chat_id):
    if calc_data_dict.get(chat_id) != None:
        calc_data_dict[chat_id] = None

def chat_calc(str):
    numbers = re.findall(r'\d+\.?\d*',str)
    if len(numbers) < 2:
        result = 'Не хватает аргументов для расчета'
    else:
        for symbol in str:
            if symbol not in CALC_SYMBOLS:
                str = str.replace(symbol, '')
        if str.find('+') != -1:
            result = float(numbers[0]) + float(numbers[1])
        elif str.find('-') != -1:
            result = float(numbers[0]) - float(numbers[1])
        elif str.find('*') != -1:
            result = float(numbers[0]) * float(numbers[1])
        elif str.find('÷') != -1:
            if float(numbers[1]) == 0:
                result = 'Ошибка деления на ноль'
            else:
                result = float(numbers[0]) / float(numbers[1])
                result = round(result,4)
        result = 'Результат: {}{}'.format(str,result)
    return result

def word_calc(str):
    str = str.lower()
    print(str)
    for step in DELETE_WORDS:
        str = re.sub(step,DELETE_WORDS[step],str)
    for step in WORD_DIGITS_DICT:
        str = re.sub(step,WORD_DIGITS_DICT[step],str)
    for step in WORD_CALC_DICT_ALTERNATIVE:
        str = re.sub(step,WORD_CALC_DICT_ALTERNATIVE[step],str)
    for step in WORD_CALC_DICT:
        str = re.sub(step,WORD_CALC_DICT[step],str)
    for symbol in str:
        if symbol not in CALC_SYMBOLS:
            str = str.replace(symbol, '')
    return chat_calc(str + '=')

# возвращает корректный слэш, в зависимости от ОС
def correct_slash():
    if platform.system() == "Windows":
        result = '\\'
    else:
        result = '/'
    return result

# не используется
def key_calc_txt_file(text, chat_id):
    calc_file_name = 'calc{}calc{}.txt'.format(correct_slash(), chat_id)
    if text == "=":
        with open(calc_file_name, 'r', encoding = 'utf-8') as local_file:
            result = chat_calc(local_file.read() + '=')
        clear_calc(chat_id)
    else:
        with open(calc_file_name, 'a') as local_file:
            local_file.write(str(text))
            result = 'calc_continue'
    return result

# не используется
def clear_calc_txt_file(chat_id):
    calc_file_name = 'calc{}calc{}.txt'.format(correct_slash(), chat_id)
    with open(calc_file_name, 'w') as local_file:
        local_file.write('')


if __name__ == '__main__':
    # str = 'девять      умножить на  шесть'
    # print(str)
    # print(word_calc(str))
    # print(chat_calc(word_calc(str)))
    # print(WORD_DIGITS_DICT['один'])
    # print(WORD_CALC_DICT_ALTERNATIVE['разделить на'])
    # print(chat_calc('6÷3='))
    # chat_calc('25  55 - 33  31  =')

    #calc('6/0=')
    # calc('25  55 + 33  31  =')
    # key_calc('1',192204203)
    # keyp_calc('1',1)
    # key_calc('=',192204203)
    print(calc_data_dict)
    str1 = "ававлалзвла 1115.155552 ÷ ыывы 22.2 5 sdsds =   8."
    # res = re.findall(r'\d*\.\d*',str1) + re.findall(r'[0-9]+',str1)
    res = re.findall(r'\d+\.?\d*',str1)
    print (res)
    # print(chat_calc(str1))