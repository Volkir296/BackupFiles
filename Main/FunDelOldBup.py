import os
import shutil

def delete_old_back(backup_dir, max_backup = 5): # По дефолту можно оставить пять версий  можно ещё расписать случайные места хранения
    
    # Получает список всех версий мб переписать НОООООООООО
    all_backs = sorted([os.path.join(backup_dir, d) for d in os.listdir(backup_dir)], key=os.path.getctime) 

    # Удаляет старейший бэкап
    while len(all_backs) > max_backup:
        oldest_backs =  all_backs.pop(0)
        shutil.rmtree(oldest_backs)
        print(f"удалён старейщий backup: {oldest_backs}")
