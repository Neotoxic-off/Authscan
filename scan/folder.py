import os
import shutil

from lib import status

def folder(folder):
    remove = None
    print(status.st(), "Creating the folder's scan: '%s'" % folder)
    if os.path.exists(folder):
        print(status.iu(), "The folder named '%s' already exists" % folder)
        remove = input(status.iu() + " Do you want to remove the folder '%s' [Y|n]: " % folder)
        if remove == 'Y':
            print(status.st(), "Removing the folder '%s'" % folder)
            try:
                shutil.rmtree(folder)
            except OSError:
                print(status.ko(), "Deletion of the directory '%s' failed" % folder)
            else:
                print(status.ok(), "Successfully deleted the directory '%s'" % folder)
        else:
            print(status.ko(), "Aboarting the creation, exiting program")
            exit(0)
    try:
        os.mkdir(folder)
    except OSError:
        print(status.ko(), "Creation of the directory '%s' failed" % folder)
    else:
        print(status.ok(), "Successfully created the directory '%s'" % folder)
