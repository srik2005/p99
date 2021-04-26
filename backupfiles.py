import os
import shutil
source = input('Enter Source Folder:')
destination = input('Enter Destination Folder:')
source = source + '/'
destination = destination + '/'
listoffiles = os.listdir(source)
for file in listoffiles:
    shutil.copy((source+file),destination)