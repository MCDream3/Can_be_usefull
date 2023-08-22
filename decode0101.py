import getopt
#getopt: Библиотека для обработки аргументов командной строки
import sys
#sys: Библиотека для взаимодействия с системой (например, для выхода из программы)
from PIL import Image
#PIL (Python Imaging Library): Библиотека для работы с изображениями

def usage():
  print('Usage: monika_decode.py [-v] [FILE]')
  sys.exit(2)
  #Функция выводит сообщение о том, как использовать программу, затем завершает выполнение с кодом завершения 2

def main(argv):    #-Получает аргументы командной строки (за исключением имени скрипта) и начинает их обработку
  if len(argv) == 0:
    usage()        #-Если нет аргументов командной строки, вызывается функция usage()
  verbose = False
  input = ''
  for arg in argv:
    if arg == '-v':
      verbose = True
    else:
      input = arg  #-Обрабатывает аргументы и определяет, нужно ли включить режим вывода подробной информации (-v)
  if len(input) == 0:
    usage()
  image = Image.open(input)
  width, height = image.size
  #Функции main(argv):
  #-Определяет имя входного файла из аргументов.
  #-Открывает изображение с помощью библиотеки PIL и получает его размеры.
  #-Затем начинает декодирование данных из изображения
  
  i = 0
  value = 0
  bits = ''
  text = ''
  for y in range(height):
    for x in range(width):
      pixel = image.getpixel((x, y))
      mean = (pixel[0] + pixel[1] + pixel[2]) / 3
      bit = 1 if mean >= 128 else 0
      bits += str(bit)
      value = value | (bit << (7 - i))
      i += 1
      if i >= 8:
        text += chr(value)
        value = 0
        i = 0
    bits += '\n'                                          #Создает строку битов (bits) и значения (value) для каждых 8 битов.
  if verbose:
    print('Input image: {}x{}'.format(width, height))
    print('Bits:')
    print(bits)
    print('Result string:')
  print(text)                                            #Когда набрано 8 битов, конвертирует значение в символ ASCII и добавляет его к текстовой строке (text)

if __name__ == '__main__':
  main(sys.argv[1:])                                     #После обработки всех пикселей выводит полученный текст.

#ФУНКЦИЯ КОДА!!!!!:
#-Программа проходит через каждый пиксель изображения, вычисляет среднюю яркость (по RGB компонентам) и на основе этой яркости определяет бит (0 или 1)(0-чёрный,1-белый)
#-Таким образом, данный код берет изображение, извлекает биты из яркости каждого пикселя, собирает их в байты и декодирует в текстовую строку
#-Код внутри этой секции будет выполнен только в том случае, если скрипт запущен напрямую, а не импортирован как модуль
#                                                                  W    A   R   N   I   N   G
#Этот код сделан в моих личных целях для декода файла игры. Только ради интереса
#На моём устройстве код рабочий
#ДАННЫЙ КОД НЕ УЧАСТВУЕТ В НАУКЕ ЭТО ТОЛЬКО ТРЕНИРОВКА

#Ten kod zrobiłam dla moich osobistych celów dla odszyfrowania pliku gry. Tylko dla "zabawy"
#Na moim urządzeniu kod działa
#KOD POWYŻEJ NIE UCZĘSZCZA W NAUCE TO JEST TYLKO TRENING
