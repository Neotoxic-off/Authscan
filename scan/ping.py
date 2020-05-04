import os
from lib import status

def ping(target):
    packet = "10"
    cont = None
    print(status.st(), "Checking your internet connection with '8.8.8.8'")
    handshake = os.system("ping -c %s 8.8.8.8 -q" % packet)
    if handshake != 0:
        print(status.ko(), "Connection on your internet failed" % target)
        cont = input(status.iu() + " Continue [Y|n]: ")
        if cont != 'Y':
            exit(84)
    else:
        print(status.ok() + " Connection successfully etablished on your internet connection")
    print(status.st(), "Connecting to the target '%s'" % target)
    handshake = os.system("ping -c %s %s -q" % (packet, target))
    if handshake != 0:
        print(status.ko(), "Connection on target '%s' failed" % target)
        cont = input(status.iu() + " Continue [Y|n]: ")
        if cont != 'Y':
            exit(84)
    else:
        print(status.ok(), "Connection successfully etablished on target '%s'" % target)