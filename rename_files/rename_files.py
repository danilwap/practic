# Программа меняет имя файла
import os

# Константа директории, r указана для того, чтобы не ставить 2 слэша
DIRECTORY = r'C:\Users\PK\Desktop\Клипы'


# функция принимает путь, с помощью функции walk
# перебирает и возвращает путь - root, dirs и files - названия
def rename_files(path_dir):
    for root, dirs, files in os.walk(path_dir):
        print(files)
        for name in files:
            rename_file(root, name)


# функция переименовывает файлы, в rename передаётся полный путь с названием файла
def rename_file(root, name):
    valid_name = get_valid_name(root, name)
    old_file = os.path.join(root, name)
    new_file = os.path.join(root, valid_name)
    print(new_file)

    os.rename(old_file, new_file)


# функция добавляет кли к названию
def get_valid_name(root, name):
    old_file = os.path.join(root, name)

    name = '''Тут ввести изменения, только без ковычек'''
    return name


# запускает всё
if __name__ == '__main__':
    rename_files(DIRECTORY)
