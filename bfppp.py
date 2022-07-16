import contextlib, sys, platform, os
from time import sleep

"""
'#' reads next letters on the tape till a 0 and opens the file with that name, if file is already open, closes the file
':' put the ascii value of the next file letter on the current tape postion and advances the pointer
';' takes the next letters on the tape till a 0 and replaces the opened file data and makes changes when the file gets closed
'/' jump with next numbers till a 0 to a location on the tape
'$' jump to after last jmp location (used for make shift functions)
"""

def parse(code: str):
    return [c for c in list(code) if c in ('+', '-', '>', '<', '[', ']', '.', ',', '#', ':', ';', '/', '$')]

def run(code: str):
    tokens = parse(code)
    n_tokens = len(tokens)
    jmp_stor = ''
    file_name_raw = []
    file_name = []
    tape=[0, 0]
    pointer = 0
    last_loop_start = 0
    token_idx = 0
    file = ''
    File_Open = False
    File_Data = ''
    File_postion = 0
    New_File_Data = ''
    while token_idx < n_tokens:
        token = tokens[token_idx]
        if token == '+':
            tape[pointer] += 1
        elif token == '-':
            tape[pointer] -= 1
        elif token == '>':
            if pointer <= len(tape) - 1:
                if tape[pointer+1] <= 0:
                    tape.append(0)
                    tape.append(0)
                pointer += 1
        elif token ==  '<':
            if pointer-1 != -1:
                pointer -= 1
        elif token ==  '[':
            last_loop_start = token_idx
        elif token ==  ']':
            if tape[pointer] != 0:
                token_idx = last_loop_start
        elif token ==  '.':
            print(chr(tape[pointer]), end='')
        elif token ==  ',':
            with contextlib.suppress(IndexError):
                tape[pointer] = ord(input()[0])
        elif token == '#':
            if File_Open:
                if New_File_Data != '':
                    file.write(New_File_Data)
                file.close()
                File_Open = False
            else:
                for i in range(1000):
                    if tape[pointer+i] != 0:
                        file_name_raw.append(tape[pointer+i])
                    else:
                        end = pointer+i-1
                        for i in file_name_raw:
                            i = chr(i)
                            file_name.append(i)
                        file_name = ''.join(file_name)
                        file_name_raw = []
                        pointer = end + 1
                        file = open(file_name, 'w+')
                        File_Open = True
                        File_Data = file.read()
                        break
        
        elif token == ':':
            try:
                tape[pointer] = ord(File_Data[File_postion:File_postion+1])
                File_postion += 1
                pointer = pointer + 1
            except:
                Nul = None
        
        elif token == ';':
            buff = []
            for i in range(1000):
                if tape[pointer+i] != 0:
                    buff.append(chr(tape[pointer+i]))
                else:
                    New_File_Data = New_File_Data + ''.join(buff)
                    break
        elif token == '/':
            buff=[]
            for i in range(1000):
                if tape[pointer+i] != 0:
                    buff.append(str(tape[pointer+i]))
                else:
                    jmp_stor = pointer+i+1
                    pointer = int(''.join(buff))
                    break
        elif token == '$':
            pointer = jmp_stor
        
        token_idx += 1
    while tape[-1] == 0: tape = tape[:-1]
    print(tape)
    return tape

def main() -> None:
    
    if len(sys.argv) < 2:
        print(f'Usage: python3 {sys.argv[0]} yourfile.bf')
        return
    
    with open(sys.argv[1], 'r') as f:
        run(f.read())

if __name__ == "__main__":
    main()

