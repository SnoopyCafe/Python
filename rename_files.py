
import os

def rename_files():
    # 1 - get file names in folrder
    dir = "/Users/preston/Downloads/prank"
    file_list = os.listdir(dir)

    # 2 loop through the files, rename each file

    for file_name in file_list:
        os.chdir(dir)
        print 'Old: %s \t New: %s' % (file_name, file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))

    # get update file list
    file_list = os.listdir(dir)
    print (file_list)

rename_files()