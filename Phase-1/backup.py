import os
import shutil
import datetime

def backup_files(source_dir, destination_dir):
   

    today_date = datetime.date.today().strftime('%Y-%m-%d')
    backup_dir = os.path.join(destination_dir, today_date)

    
    os.makedirs(backup_dir, exist_ok=True)

    for root, directories, files in os.walk(source_dir):
        for file in files:
            source_file = os.path.join(root, file)
            destination_file = os.path.join(backup_dir, os.path.relpath(source_file, source_dir))
            shutil.copy2(source_file, destination_file) 

    print(f"Backup completed to: {backup_dir}")


source_directory = "G:/videos"
destination_directory = "C:/"
backup_files(source_directory, destination_directory)
