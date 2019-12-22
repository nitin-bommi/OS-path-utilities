# playing with shell methods.

# importing the necessary libraries.
import shutil
from shutil import make_archive
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("textfile.txt"):
    
    #get the path to the file in the current directory
    src = path.realpath("textfile.txt")
    
    # make a backup copy by appending ".bak" to the name
    dst = src + ".bak"
    
    # copy over the permissions, modification time, and other info
    shutil.copy(src, dst)
    shutil.copystat(src, dst)
    
    # rename the original file
    os.rename("textfile.txt", "newfile.txt")
    
    # put the files in a ZIP archive
    root_dir, tail = path.split(src)
    shutil.make_archive("archive", "zip", root_dir)
    
    # fine zip
    with ZipFile("test_zip.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")
