import os, re, glob

if 'RobloxPlayerBeta.exe' in os.popen('tasklist').read():

    nl = "\n"

    list_of_files = glob.glob(fr'C:\Users\{os.popen("echo %USERNAME%").read().replace(nl, "")}\AppData\Local\Roblox\logs\*')
    latest_file = max(list_of_files, key=os.path.getctime)

    f = open(latest_file, 'r')
    data = f.read()
    f.close()

    data = "".join(re.findall('\d*\.\d*\.\d*\.\d*:\d*\n', data))
    data = "".join(data.split(':')[0])

    os.system(f'echo {str(data)}')
else:
    os.system('echo no roblox instance found')
