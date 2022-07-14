import sys, zlib, os
import random
import string

Name_A = ''.join(random.choices(string.ascii_letters, k=15))
Name_B = ''.join(random.choices(string.ascii_letters, k=15))
while Name_B == Name_A:
    Name_B = ''.join(random.choices(string.ascii_letters, k=15))

try:
    exe_one = sys.argv[1]
    exe_two = sys.argv[2]
    Final_Exe_Name = sys.argv[3]
except:
    print(f'usage: {__file__} [Exe File Location] [second Exe File Location] [Final Exe Name]')
    exit(1)

try:
    fin_exe = open(Final_Exe_Name, 'w')
    exe_A = open(exe_one, 'rb')
    exe_B = open(exe_two, 'rb')
except:
    print(f'Cannot accese 1 or more files')
    exit(1)

Exe_A_Data = exe_A.read()
Exe_B_Data = exe_B.read()
exe_A.close()
exe_B.close()

Exe_A_Data = zlib.compress(Exe_A_Data)
Exe_B_Data = zlib.compress(Exe_B_Data)

tmp = os.popen("echo %TEMP%").read()

fin_exe.write(f"""
import zlib, os
Exe_A = {Exe_A_Data}
Exe_B = {Exe_B_Data}
Exe_A = zlib.decompress(Exe_A)
Exe_B = zlib.decompress(Exe_B)
a = open('{tmp}\\\\{Name_A}.exe', 'wb')
b = open('{tmp}\\\\{Name_B}.exe', 'wb')
a.write(Exe_A)
a.close()
b.write(Exe_B)
b.close()
os.system("start {tmp}\\\\{Name_A}.exe && start {tmp}\\\\{Name_B}.exe && del {tmp}\\\\{Name_A}.exe && del {tmp}\\\\{Name_B}.exe")
""")

if not os.path.exists('Scripts/pyinstaller'):
    os.system('pip install pyinstaller')
os.system(f'pyinstaller -F {Final_Exe_Name}')


