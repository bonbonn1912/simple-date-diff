import os,time, shutil, keyboard
from pathlib import Path

source_path = r"F:\Coding\Test"
destination_path = r'F:\Coding\New' 


def list_files():
    r = []
    number = 0
    for root,dirs, files in os.walk(source_path):
        for name in files:      
            r = os.path.join(root, name)
            last_time = os.path.getmtime(r)
            if(round(time.time()) - round(last_time) < 120):
                number += 1
                new_dest = r.replace(source_path, destination_path)
                shutil.copy(r, new_dest)
                print('\x1b[6;30;42m' + '\tupdated: {}'.format(new_dest) +'\x1b[0m')
    return number

def run():
    os.system('cls')
    start = time.time()
    number = list_files()
    end = time.time()
    print("moved " + str(number) + " files in " + str(round(end - start, 3)) + " seconds")


keyboard.add_hotkey('ctrl + s', run)
  
keyboard.wait('ctrl + l') 
