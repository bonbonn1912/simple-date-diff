import os, datetime, time, shutil
from pathlib import Path

def list_files(dir):
    r = []
    source_path = 'insert_source_path'
    new_path = 'insert_new_dest'
    number = 0
    for root, files in os.walk(dir):
        for name in files:      
            r = os.path.join(root, name)
            last_time = os.path.getmtime(r)
            if(round(time.time()) - round(last_time) < 60):
                number += 1
                new_dest = r.replace(source_path, new_path)
                shutil.copy(r, new_dest)
                print(new_dest)
    return number
start = time.time()
all_files = list_files(os.getcwd())
end = time.time()
print("moved " + str(all_files) + " files in " + str(end - start) + " seconds")