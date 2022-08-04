import math, sys
from time import perf_counter
from PIL import Image

file = sys.argv[1]

def beautifier(B):
    C = float
    B=C(B);A=C(1024);D=C(A**2);E=C(A**3);F=C(A**4)
    if B<A:return '{0} {1}'.format(B,'Bytes'if 0==B>1 else'Byte')
    elif A<=B<D:return '{0:.2f} KB'.format(B/A)
    elif D<=B<E:return '{0:.2f} MB'.format(B/D)
    elif E<=B<F:return '{0:.2f} GB'.format(B/E)
    elif F<=B:return '{0:.2f} TB'.format(B/F)

f = open(file, 'rb')
data = f.read()
f.close()

print(f'total size: {beautifier(len(data))}')

lens = int(math.ceil(math.sqrt(len(data)/4)))
print(lens, 'x', lens)
xy = (lens, lens)

im = Image.new(mode = 'CMYK', size = xy)
pixels = im.load()
n = 0
last = 0

for i in range(im.size[0]):
    for a in range(im.size[1]):
        try:
            persent = round(i/im.size[0], 2)
            if persent != last:
                last = persent
                persent = str(int(persent * 100)) + '%'
                print(persent, end='\r')
                pixels[i, a] = data[n], data[n+1], data[n+2], data[n+3]
        except Exception as errr:
            pixels[i, a] = (0, 0, 0, 0)

im.save(f'{sys.argv[2]}.jpg')

f = open(sys.argv[2] + '.jpg', 'rb')
length = len(f.read())
f.close()
print('')
print(f'Done, saved as {sys.argv[2]}.jpg, final size: {beautifier(length)}')