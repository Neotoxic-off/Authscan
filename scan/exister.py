from __future__ import print_function
import urllib.request
import datetime
import os
import sys
from lib import status
from lib import colors

def exister(target, path, proto, folder):
    percent = 0
    total_success = 0
    tested = 0
    found = 0
    total_lines = 0
    if target[len(target) - 1] != '/':
        baseURL = proto + "://" + target + '/'

    if path != None and os.path.isfile(path):
        f = open(path, "r")
        r = open(path, "r")
        log = open(folder + "/logs.txt", 'w')
    
        line = f.readline()
        tmp = r.readline()
        while tmp:
            total_lines += 1
            tmp = r.readline()
        r.close()
        while line:
            tested += 1
            if line[len(line) - 1] == '\n' or line[len(line) - 1] == '\0':
                line = line[:-1]
            fullURL = baseURL + line
            try:
                req = urllib.request.Request(fullURL)
                resp = urllib.request.urlopen(req)
                if resp.getcode() == 404:
                    log.write("Error 404 '{0}'\n").format(fullURL)
                else:
                    log.write("Found '{0}' Response: {1}\n".format(fullURL, resp.getcode()))
                    total_success += 1
            except:
                log.write("Not found '{0}'\n".format(fullURL))

            percent = ((tested / total_lines) * 100)
            sys.stdout.write("Found: %d Tested: %d Total: %d Progress: %d" % (total_success, tested, total_lines, percent))
            sys.stdout.write("%")
            sys.stdout.flush()
            sys.stdout.write('\b' * (7 + 9 + 8 + 12 + len(str(total_success)) + len(str(tested)) + len(str(total_lines)) + len(str(percent))))
            sys.stdout.flush()
            line = f.readline()
        f.close()
        log.close()
        print('Found: %d Tested: %d Total: %d\n' % (total_success, tested, total_lines))
    else:
        print(status.ye() + " Skipping brute-force part, due to uninitialiation of the path")
        return