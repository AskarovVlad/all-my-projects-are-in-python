import os
import json

sourse_dir = 'C:/Users/DESKTOP-65L32PF/Desktop/Program\\PythonProject'
files_list = os.listdir(sourse_dir)  # список, показ все файлии в данной директории
print(files_list)
ccurrent_cwd = os.getcwd()      # показ путь к этой директории
print(ccurrent_cwd)
new_dir = os.path.join(sourse_dir, 'lollololol')
total_files = []
for filename in files_list:
    path_filename = os.path.join(sourse_dir, filename)
    if os.path.isfile(path_filename):
        total_files.append(filename)
print(total_files)
# os.mkdir('LOLOLOLOLOLOL')   # создает папку в текущей директории, там где и написан код, не умеет складывать вложенные директории
os.makedirs('LOooooo/123/321', exist_ok=True)   # создает папку в текущей директории, там где и написан код, но если она существует,
# то ничего не создается
with open('dz 2.py', 'r') as txt_file:
    # data = txt_file.read()  # метод считывает файл и возвращает как 1 строку
    data = txt_file.readline()  # метод считывает файл и возвращает построчно
print(data)

with open('dz 2_test.py', 'w') as json_file:
    json_file.writelines(data)
print(data)

def list_writer(filename, data):
    with open(filename, 'w') as json_file:
        json_file.writelines(str(data))

def list_reader(filename):
    with open(filename, 'r') as json_file:
        data = json.readline()
        return data

filename = 'lesson 10.json'
data = [1, 2, 3, 4, 5]
