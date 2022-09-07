import pyautogui, zlib, time, socket
from PIL import Image

screenWidth, screenHeight = pyautogui.size()

def compress(data):
    if 'byte' not in str(type(data)):
        data = data.encode()
    zip = zlib.compressobj(level=7, memLevel=9) # max level is 9 (slower but more compression), mem should be fine
    data = zip.compress(data)
    data += zip.flush()
    return data

def decompress(data, decode=False):
    unzip = zlib.decompressobj()
    data = unzip.decompress(data)
    data += unzip.flush()
    if decode:
        return data.decode()
    else:
        return data

def get_frame():
    img = pyautogui.screenshot()
    img.resize((screenWidth / 2, screenHeight / 2),Image.ANTIALIAS)
    return img

def work():
    start = time.time() # test to see if we can get more then 30fps
    for i in range(29): # 30 frames
        frame = get_frame()
        frame_compressed = compress(frame)
    end = time.time()
    print(end-start)
