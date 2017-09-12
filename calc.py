import platform
import codecs
# Калькуляторы
CALC_SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','+','-','*','÷','=']
DIGITS = ['0','1','2','3','4','5','6','7','8','9']

def correct_slash():
    if platform.system() == "Windows":
        result = '\\'
    else:
        result = '/'
    return result

def chat_calc(str):
    numbers = ['','']
    numbers_count = 0
    for symbol in str:
        if symbol not in CALC_SYMBOLS:
            str = str.replace(symbol, '')
    for symbol in str:
        if symbol in DIGITS:
            numbers[numbers_count] += symbol
        else:
            numbers_count +=1
    if str.find('+') != -1:
        result = int(numbers[0]) + int(numbers[1])
    elif str.find('-') != -1:
        result = int(numbers[0]) - int(numbers[1])
    elif str.find('*') != -1:
        result = int(numbers[0]) * int(numbers[1])
    elif str.find('÷') != -1:
        if int(numbers[1]) == 0:
            result = 'Ошибка деления на ноль'
        else:
            result = float(numbers[0]) / float(numbers[1])
            result = round(result,2)
    return('Результат вычислений: {}{}'.format(str,result))

def key_calc(text, chat_id):
    print(text)
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

def clear_calc(chat_id):
    calc_file_name = 'calc{}calc{}.txt'.format(correct_slash(), chat_id)
    with open(calc_file_name, 'w') as local_file:
        local_file.write('')


if __name__ == '__main__':
    print(chat_calc('6÷3='))
    chat_calc('25  55 - 33  31  =')
    #calc('6/0=')
    # calc('25  55 + 33  31  =')
