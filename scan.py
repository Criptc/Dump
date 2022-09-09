import os, hashlib
from getpass import getuser

class scan_error(Exception):
    def __init__(self, error) -> None:
        self.error = error

    def __str__(self) -> str:
        return self.error
    
    def usererror(self):
        return f'user not found: {self.error}'


class file:
    def __init__(self, arg) -> None:
        self.users = os.listdir('C:\\Users\\')
        self.arg = arg

    def all(self):
        outfiles = []

        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                fullfile = root + file
                outfiles.append(fullfile)
        return outfiles

    def user(self):
        outfiles = []
        if self.arg not in self.users:
            raise scan_error(f'user not found: {self.arg}')
        
        for root, dirs, files in os.walk(f'C:\\Users\\{self.arg}'):
            for file in files:
                fullfule = root + file
                outfiles.append(fullfule)
        return outfiles

    def folder(self):
        outfiles = []
        if not os.path.exists(self.arg):
            raise scan_error(f'Folder doesn\'t exist: {self.arg}')
        elif not os.path.isdir(self.arg):
            raise scan_error(f'{self.arg} is not an folder, use scan.file.file')
        
        for root, dirs, files in os.walk(self.arg):
            for file in files:
                fullfile = root + file
                outfiles.append(fullfile)
        return outfiles

class hash:
    def __init__(self, arg):
        self.users = os.listdir('C:\\Users\\')
        self.arg = arg
    
    def all(self):
        outhashes = []

        for root, dirs, files in os.walk('C:\\'):
            for file in files:
                fullfile = root + file
                hash = hashlib.sha256(fullfile)
                outhashes.append(hash)
        return outhashes

    def user(self):
        outhashes = []
        if self.arg not in self.users:
            raise scan_error(f'user not found: {self.arg}')
        
        for root, dirs, files in os.walk(f'C:\\Users\\{self.arg}'):
            for file in files:
                fullfile = root + file
                hash = hashlib.sha256(fullfile)
                outhashes.append(hash)
        return outhashes

    def folder(self):
        outhashes = []
        if not os.path.exists(self.arg):
            raise scan_error(f'Folder doesn\'t exist: {self.arg}')
        elif not os.path.isdir(self.arg):
            raise scan_error(f'{self.arg} is not an folder, use scan.hash.file')
        
        for root, dirs, files in os.walk(self.arg):
            for file in files:
                fullfile = root + file
                hash = hashlib.sha256(fullfile)
                outhashes.append(hash)
        return outhashes

    def file(self):
        if not os.path.exists(self.arg):
            raise scan_error(f'file doesn\'t exist {self.arg}')
        elif not os.path.isfile(self.arg):
            raise scan_error(f'{self.arg} isn\'t an file, use scan.hash.folder')
        
        return hashlib.sha256(self.arg)


print(hash.folder('C:\\Users\\Joseph\\Desktop\\'))


