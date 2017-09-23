import ephem
import re
from datetime import timedelta, date, time, datetime
PLANETS = ['Mercury', 'Venus','Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

# Определение созвездия
def get_constellation_name(planet_name):
    planet_name = planet_name.capitalize()
    if planet_name in PLANETS:
        planet = getattr(ephem, planet_name)
        result = ephem.constellation(planet(datetime.now()))[1]
    else:
        result = 'Нет такой планеты'
    return result

def next_full_moon(str):
    date = re.findall(r'\d{4}/\d{2}/\d{2}', str)
    if date != []:
        result = 'Ближайшее полнолуние: %s' % ephem.next_full_moon(date[0])
    elif re.findall(r'\d', str) != []:
        result = 'Укажите дату в формате ГГГГ/ММ/ДД'
    else:
        result = 'Ближайшее полнолуние: %s' % ephem.next_full_moon(datetime.now())
    return result

if __name__ == '__main__':
    # print(next_full_moon('2016/10/01'))
    # str1 = 'Когда ближайшее полнолуние после 2016-10-01?'
    # flag = re.search(r'ближайшее полнолуние',str1)
    # print(bool(flag))
    str = 'Когда ближайшее полнолуние после 2016/10/01?'
    print(next_full_moon(str))
    # print(datetime.strftime(next_full_moon(datetime.now()),'%d.%m.%y'))
