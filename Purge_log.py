#!/bin/python3

import shutil     # для копирования файлов
import sys        # для аргументов командной строки
import os         # для получения размера файла

# purge_log.py   log.txt  10   5

if len(sys.argv) < 4:
    print("Не хватает аргумента")
    exit(1)

file_name = sys.argv[1]
limit_size = int(sys.argv[2])
logs_number = int(sys.argv[3])

if os.path.isfile(file_name) is True:             # проверка на существование файла
    file_size = os.stat(file_name).st_size        # размер файла в байтах
    file_size = file_size / 1024                  # конверт. а килобайты

    if file_size >= limit_size:
        if logs_number > 0:
            for currentFileNumber in range(logs_number, 1, -1):
                source = file_name + "_" + str(currentFileNumber-1)
                destination = file_name + "_" + str(currentFileNumber)
                if os.path.isfile(source) is True:
                    shutil.copyfile(source, destination)
                    print("Скопировано" + source + "в" + destination)

            shutil.copyfile(file_name, file_name + "_1")

        my_file = open(file_name, "w")
        my_file.close()








