# импорт модулей
import os, re, time, datetime

# проверить ОС == Windows
from sys import platform 
if platform == 'win32':
  from win32_setctime import setctime

def finder():
  # все файлы в текущей директории
  names = os.listdir(os.getcwd())
  # цикл по всем файлам
  for name in names:
    # путь к текущему файлу
    fullname = os.path.join(os.getcwd(), name)
    if os.path.isfile(name):
      # если файл подходит под шаблон названия
      if (re.search('IMG|VID.\d{8}.*\.jpg|mp4', name)): 
        # получить год, месяц и день из названия
        y = int(name[4:8])
        m = int(name[8:10])
        d = int(name[10:12])
        # создать дату и превратить ее в timestamp
        date = datetime.datetime(y, m, d).timestamp()
        # изменить дату изменения (но не создания)
        os.utime(fullname, times=(date,date))
        # если Windows
        if platform == 'win32':
          # изменить дату создания
          setctime(fullname, date)
          # вывести дату создания
          print(os.path.getctime(fullname))

# выполнить функцию
if __name__ == '__main__':
  finder()