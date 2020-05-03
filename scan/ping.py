import os
from lib import status

def ping(target):
    packet = "10"
    print(status.st(), "Connecting to the target '%s'" % target)
    handshake = os.system("ping -c %s %s" % (packet, target))
    if handshake != 0:
        print(status.ko(), "Connection on target '%s' failed" % target)
        exit(84)
    else:
        print(status.ok(), "Connection successfully etablished on target '%s'" % target)