import os
import shutil

from lib import colors
from lib import status
from scan import ping

def extract_script(scripts):
    real = scripts.split('/')

    return (real[len(real) - 1])

def execute(target, script):
    try:
        print(status.st(), "Executing: 'nmap --script %s %s'" % (script, target))
        os.system('nmap --script %s %s' % (script, target))
    except:
        print(status.ko(), "Error occured during the NMAP's scan")
    else:
        print(status.ok(), "Execution: 'nmap --script %s %s' completed" % (script, target))

def custom(target):
    script = None
    extracted = None
    choice = input(status.iu() + " Do you want to start custom nmap's scripts [Y|n]: ")

    if choice == 'Y':
        print(status.io(), "When you finished type 'exit' to stop 'NMAP' session")
        print(status.io(), "Default path of the nmap's scripts: '" + colors.purple() + "/usr/share/nmap/scripts" + colors.reset() + "'")
        while script != "exit":
            script = input(status.iu() + " FULL path of the nmap script: ")
            if script != "exit":
                print(status.st(), "Checking the script's file")
                if os.path.exists(script):
                    print(status.ok(), "Script's file found")
                    extracted = extract_script(script)
                    execute(target, extracted)
                else:
                    print(status.ko(), "Script's file no found")

def basic(target):
    try:
        print(status.st(), "Executing: 'nmap %s'" % target)
        os.system('nmap %s' % target)
    except:
        print(status.ko(), "Error occured during the NMAP's scan")
    else:
        print(status.ok(), "Execution: 'nmap %s' completed" % target)

def nmap(target):
    print(status.st(), "Starting session 'NMAP'")

    basic(target)
    custom(target)
    print(status.ok(), "Session 'NMAP' ended")
