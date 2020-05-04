import os
from lib import colors
from lib import status
from scan import ping

def nmap(target):
    print(status.st(), "Starting session 'NMAP'")
    try:
        os.system('nmap %s' % target)
    except:
        print(status.ko(), "Error occured during the NMAP's scan")
    else:
        print(status.ok(), "Session 'NMAP' ended")
