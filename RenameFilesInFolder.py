
# Python program to rename all file's names in your directory
import os
 
os.chdir("C:\\Users\\x\\Desktop\\x")
print(os.getcwd())
 
for count, f in enumerate(os.listdir()):
    f_name, f_ext = os.path.splitext(f)
    f_name = "CHOOSE WHAT YOU LIKE_" + str(count) 
    #f_name = f_name.upper()
    new_name = f'{f_name}{f_ext}'
    os.rename(f, new_name)
