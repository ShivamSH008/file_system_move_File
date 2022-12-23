import os

#Source file path
source = 'main.txt'

#Destination file path
dest = 'newfile.txt'

os.rename(source, dest)

print("Source path renamed to Destination path succesefully.")

