import os
import sys
from lib import status
from lib import colors

def total_lines(folder, out):
    fullpath = str(folder) + "/" + str(out)
    total = 0

    if os.path.exists(fullpath):
        f = open(fullpath, 'r')
        line = f.readline()
        while line:
            line = f.readline()
            total += 1
    return (total)

def linker(target, path, proto, folder, out):
    fullpath = str(folder) + "/" + str(out)
    fulllinks = str(folder) + "/links.txt"
    url = 0
    parsing = 0
    i = 0
    progress = 0
    percent = 0
    nb_lines = total_lines(folder, out)

    if os.path.exists(fullpath):
        print(status.ok(), "File found: " + fullpath)
        f = open(fullpath, 'r')
        if os.path.exists(fulllinks):
            os.remove(fulllinks)
        r = open(fulllinks, 'w+')
        print(status.st(), "Searching Urls")
        line = f.readline()
        while line:
            progress += 1
            sys.stdout.write("Found: " + colors.green() + str(url) + colors.reset() + " Progress: " + colors.cyan() + "%d" % percent + colors.reset() + "%")
            sys.stdout.flush()
            sys.stdout.write('\b' * (7 + 11 + len(str(url)) + len(str(percent))))
            sys.stdout.flush()
            while i < len(line) - 1:
                if line[i] == '/' and line[i - 1] == "\"" and line[i + 1] != '>':
                    while line[i] != "\"" and i < len(line) - 1:
                        r.write(line[i])
                        i += 1
                    r.write('\n')
                    url += 1
                if line[i] == '/' and line[i - 1] == "'" and line[i + 1] != '>':
                    while line[i] != "'" and i < len(line) - 1:
                        r.write(line[i])
                        i += 1
                    r.write('\n')
                i += 1
            i = 0
            line = f.readline()
            percent = ((nb_lines / progress) * 100)
        f.close()
        r.close()
        print("Found: " + colors.green() + str(url) + colors.reset() + " Progress: " + colors.cyan() + "%d" % percent + colors.reset() + "% => '" + colors.purple() + fulllinks + colors.reset() + "'")
    else:
        print(status.ok(), "File not found: " + fullpath)
