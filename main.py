import os
import time
import shutil

keep_downloads_day = 7

current_time = time.time()
keep_downloads_day_time = keep_downloads_day*24*60*60


def stat_to_json(s_obj):
    return {k: getattr(s_obj, k) for k in dir(s_obj) if k.startswith('st_')}


# organize downloads
with os.scandir('/home/maicon/Downloads') as dir_entries:
    for entry in dir_entries:
        name = entry.name
        path = entry.path
        is_folder = entry.is_dir()
        stat = entry.stat()
        stat = stat_to_json(stat)

        keep = current_time - stat['st_mtime'] < keep_downloads_day_time

        extension = '__FOLDERS__' if is_folder else False

        if not extension:
            if name.split('.')[-1] == name.split('.')[0]:
                extension = '__?????__'
            else:
                extension = name.split('.')[-1]

        if not keep:
            try:
                print(f'Movendo {name}')

                try:
                    os.mkdir(
                        f'/home/maicon/Downloads/__OLD(BOT)__/{extension}/')
                except:
                    print(
                        f'/home/maicon/Downloads/__OLD(BOT)__/{extension}/ ja existe')

                shutil.move(
                    f'/home/maicon/Downloads/{name}', f'/home/maicon/Downloads/__OLD(BOT)__/{extension}/{name}')
            except Exception as e:
                print(f'falha ao mover {name}')
                print(e)
