from time import sleep

global Storage, Memory, Register, Data
Storage = [0x00 for x in range(1001)]
Memory = [0x00 for x in range(101)]
Register = [0x00 for x in range(5)]
Data = [0x00 for x in range(100)]

'''
Table:
0x00 Nothing
0x01 Clear Memory
0x02 Clear Storage
0x03 Store a in Memory, 0x03 {location in Memory}
0x04 Store b in Memory, 0x04 {location in Memory}
0x05 Store c in Memory, 0x05 {location in Memory}
0x06 Store d in Memory, 0x06 {location in Memory}
0x07 read memory, 0x07 {location in Memory}
0x0a Store in reg a, 0x0a {data to store}
0x0b store in reg b, 0x0b {data to store}
0x0c store in reg c, 0x0c {data to store}
0x0d store in reg d, 0x0d {data to store}
0x0e store a to, 0x0e {location to store to}
0x0f store b to, 0x0f {location to store to}
0x10 store c to, 0x10 {location to store to}
0x11 store d to, 0x11 {location to store to}
0x12 read storage location, write to a, 0x12 {storage location}
0x13 read storage location, write to b, 0x13 {storage location}
0x14 read storage location, write to c, 0x14 {storage location}
0x15 read storage location, write to d, 0x15 {storage location}
0x16 read storage location, 0x16 {storage location}
0x17 jump to location, 0x17, {location}
'''

def decode(values):
    jmp = False
    ReadMem = False
    ReadStorage = False
    MemoryStoreRegistry = False
    StoreMemA = False
    StoreMemB = False
    StoreMemC = False
    StoreMemD = False
    StoreRegA = False
    StoreRegB = False
    StoreRegC = False
    StoreRegD = False
    StoreATo = False
    StoreBTo = False
    StoreCTo = False
    StoreDTo = False
    WriteStorageA = False
    WriteStorageB = False
    WriteStorageC = False
    WriteStorageD = False
    n=0
    while True:
        n=n+1
        if values[n:n+1] == ['0x1a']:
            exit(0)
        value = int(''.join(values[n:n+1]))
        global Storage, Memory
        if MemoryStoreRegistry:
            MemoryStoreRegistry = False
            if StoreMemA:
                Register[0] = value
                StoreMemA = False
            if StoreMemB:
                Register[0] = value
                StoreMemB = False
            if StoreMemC:
                Register[0] = value
                StoreMemC = False
            if StoreMemD:
                Register[0] = value
                StoreMemD = False
        elif StoreRegA:
            StoreRegA = False
            Register[0] = value
        elif StoreRegB:
            StoreRegB = False
            Register[1] = value
        elif StoreRegC:
            StoreRegC = False
            Register[2] = value
        elif StoreRegD:
            StoreRegD = False
            Register[3] = value
        elif ReadMem:
            ReadMem = False
            print(Memory[value])
        elif ReadStorage:
            ReadStorage = False
            print(Storage[value])
        elif StoreATo:
            StoreATo = False
            Storage[value] = Register[0]
        elif StoreBTo:
            StoreBTo = False
            Storage[value] = Register[1]
        elif StoreCTo:
            StoreCTo = False
            Storage[value] = Register[2]
        elif StoreDTo:
            StoreDTo = False
            Storage[value] = Register[3]
        elif WriteStorageA:
            WriteStorageA = False
            Register[0] = Storage[value]
        elif WriteStorageB:
            WriteStorageB = False
            Register[1] = Storage[value]
        elif WriteStorageC:
            WriteStorageC = False
            Register[2] = Storage[value]
        elif WriteStorageD:
            WriteStorageD = False
            Register[3] = Storage[value]
        elif jmp:
            jmp = False
            n = value
        
        
        if value == 0x01:
            Memory = [0x00 for x in range(101)]
        elif value == 0x02:
            Storage = [0x00 for x in range(1001)]
        elif value == 0x03:
            MemoryStoreRegistry = True
            StoreMemA = True
        elif value == 0x04:
            MemoryStoreRegistry = True
            StoreMemB
        elif value == 0x05:
            MemoryStoreRegistry = True
            StoreMemC
        elif value == 0x06:
            MemoryStoreRegistry = True
            StoreMemD
        elif value == 0x07:
            ReadMem = True
        elif value == 0x0a:
            StoreRegA = True
        elif value == 0x0b:
            StoreRegB = True
        elif value == 0x0c:
            StoreRegC = True
        elif value == 0x0d:
            StoreRegD = True
        elif value == 0x0e:
            StoreATo = True
        elif value == 0x0f:
            StoreBTo = True
        elif value == 0x10:
            StoreCTo = True
        elif value == 0x11:
            StoreDTo = True
        elif value == 0x12:
            WriteStorageA = True
        elif value == 0x13:
            WriteStorageB = True
        elif value == 0x14:
            WriteStorageC = True
        elif value == 0x15:
            WriteStorageD = True
        elif value == 0x16:
            ReadStorage = True
        elif value == 0x17:
            jmp = True
        elif value == 0x1a:
            exit(0)

def Start():
    global Data
    n = 0
    f = open('Compileme.py', 'r')
    data = f.read()
    f.close()
    data = data.split('\n')
    for i in data:
        n = n + 1
        Data[n] = str(int(i, 16))
    return Data

Data = Start()
sleep(4)
decode(Data)