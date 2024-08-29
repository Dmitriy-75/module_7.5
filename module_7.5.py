import os
import time

print('\nТекущая директоория',os.getcwd()+'\n')

for  root, dirs, files in os.walk('.'):
    for file in files:
        filepath=os.path.join(file)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize=os.path.getsize(file)
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, '
              f'Время изменения: {formatted_time}, Родительская директория: {os.path.dirname(file)}')











