import os
import shutil 
from datetime import datetime

def create_backup(source_dir, backup_dir):

    # Обраточик ошибок на проверку существуюищей директории
    if not os.path.exists(source_dir):
        print(f"Исходня директория '{source_dir}' не найдена." )
        return
    
    # Создание директории для резервных копий, если её нет - можно разбить на отдельную швирлу но нужно придумать связь косвенную
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    # Уникальное имя и бэкапа по дате и времени
    backup_name = f"backup_{datetime.now().strftime('%Y%m%d_%H%M%S')}" 
    backup_path = os.path.join(backup_dir,backup_name)

    # Копирование из В
    try:
        shutil.copytree(source_dir,backup_path)
        print(f"Резервная копия успешно создана: {backup_path}")
    except Exception as e:
        print(f"Ошибка при создании резервной копии: {e}")

# Обработчик ошибок на / расписать 
source_directory = "C:/Users/User/Downloads"
backup_directory = "D:/TestBack"

# Тоже написать отдельную швирлу 
create_backup(source_directory, backup_directory)