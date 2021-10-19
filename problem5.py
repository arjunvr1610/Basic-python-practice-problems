'''Problem statement:- Create an application to secure your folder.'''
import os, shutil
class folder_locker:
    def __init__(self, folderLocation, folderName, lockerName, pin):
        self.folderLocation = folderLocation
        self.folderName = folderName
        self.lockerName = lockerName
        self.pin = pin
    
    def create_main(self):       
        os.mkdir(f"{self.folderLocation}\\{self.lockerName}")
        shutil.move(f"{self.folderLocation}\\{self.folderName}", f"{self.folderLocation}\\{self.lockerName}")
    
    def authenticate(self):
        for i in range(10):
            os.mkdir(f"{self.folderLocation}\\{i}")
    

lock1 =  folder_locker("D:\\", "me", "SafeMe")
lock1.create_main()
