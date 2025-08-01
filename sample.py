# import sys
#
#
# a = int(sys.argv[1])
# b = int(sys.argv[2])
# print(a+b)




# import sys
#
#
# # Вывод всех аргументов командной строки
# print("Все аргументы:", sys.argv)
#
#
# # Работа с первым аргументом (если он передан)
# if len(sys.argv) > 1:
#     print(f"Переданный аргумент: {sys.argv[1]}")
# else:
#     print("Аы.")



#Пример: Обработка нескольких аргументов
import sys


if len(sys.argv) > 1:
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"Арент {i}: {arg}")
else:
    print("Аргументы не переданы.")

Запуск python файла через терминал:
python script.py arg1 arg2 arg3




# import sys
# import os
#
#
# # Проверяем, передан ли аргумент
# if len(sys.argv) != 2:
#     print("Использование: python script.py <директория>")
#     sys.exit()
#
#
# directory = sys.argv[1]
#
#
# # Проверяем существование директории
# if not os.path.isdir(directory):
#     print(f"Директория '{directory}' не существует.")
#     sys.exit()
#
#
# # Выводим содержимое директории
# print(f"Содержимое директории '{directory}':")
# for item in os.listdir(directory):
#     print(f"- {item}")

#Запуск:
#python script.py /home/user/documents