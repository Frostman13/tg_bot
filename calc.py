# Калькуляторы
CALC_SYMBOLS = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','=']
DIGITS = ['0','1','2','3','4','5','6','7','8','9']

def calc(str):
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
    elif str.find('/') != -1:
        if numbers[1] == 0:
            result = 'Ошибка деления на ноль'
        else:
            result = float(numbers[0]) / float(numbers[1])
            result = round(result,2)
    print(numbers)
    print(result)
    return('Результат вычислений: {}{}'.format(str,result))

if __name__ == '__main__':
    calc('25  55 - 33  31  =')
    # calc('25  55 + 33  31  =')
    # calc('25  55 * 33  31  =')
    # calc('25  55 / 33  31  =')
