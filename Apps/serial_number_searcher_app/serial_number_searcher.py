import re
import os
import time
import datetime
from pathlib import Path
import math

ruta_inicial = os.getcwd()

ruta = ruta_inicial + '\\Mi_Gran_Directorio'

my_patron = r'N\D{3}-\d{5}'

today = datetime.date.today()

found_numbers = []

found_files = []

start = time.time()


def search_number(file,patron):
    file_opener = open(file,'r')
    text = file_opener.read()
    if re.search(patron,text):
        return re.search(patron,text)
    else:
        return ''

def create_list():
    for folder,subfolder,file in os.walk(ruta):
        for i in file:
            result = search_number(Path(folder,i),my_patron)
            if result != '':
                found_numbers.append((result.group()))
                found_files.append((i.title()))

def show_all():
    index = 0
    print("*" * 25)
    print(f'Search date: {today}')
    print('FILE NAME\t\t\tSerie Number')
    print('*********\t\t\t************')

    for i in found_files:
        print(f'{i}\t\t{found_numbers[index]} ')
        index += 1

    print('\n')
    print(f'Found numbers: {len(found_numbers)}')
    end = time.time()
    process_length = end - start
    print(f'Research time: {math.ceil(process_length)} seconds')
    print("*" * 25)



create_list()
show_all()



