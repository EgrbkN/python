import os
import dz_eazy
9
exitos ='a'
while exitos != '0':
    print('Перейти в папку - выбрать 1')
    print('Просмотреть содержимое текущей папки - выбрать 2')
    print('Удалить папку - выбрать 3')
    print('Создать папку - выбрать 4')
    print('Для выхода - выбрать 0')
    exitos = input('Выбрать: ' )
    print(exitos)
    if exitos == '1':
        dir_name = input ('Наберите полный путь папки: ')
        easy.change_dir(dir_name)
    elif exitos == '2':
        dir_name = os.getcwd()
        easy.list_dir(dir_name)
    elif exitos == '3':
        dir_name = input('Наберите полный путь папки: ')
        easy.delete_dir(dir_name)
    elif exitos == '4':
        dir_name = input('Наберите полный путь папки: ')
        easy.make_dir(dir_name)
    elif exitos == '0':
        pass
    else:
        print('Такого пункта меню нет')