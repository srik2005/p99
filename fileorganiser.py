import os
import shutil
path= input("Enter the Path of the Folder which needs to be Sorted:")
listoffiles = os.listdir(path)
for file in listoffiles:
    name,ext = os.path.splitext(file)
    ext=ext[1:]
    print(ext)
    if ext=='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)    

 
    