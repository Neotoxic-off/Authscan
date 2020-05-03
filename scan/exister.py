from __future__ import print_function
import urllib.request
import datetime
from lib import status
from lib import colors


def exister(target, path, proto):
    total_success = 0
    total_url = 0
    if target[len(target) - 1] != '/':
        baseURL = proto + "://" + target + '/'

    f = open(path, "r")
    line = f.readline()
    while line:
        total_url += 1
        if line[len(line) - 1] == '\n' or line[len(line) - 1] == '\0':
            line = line[:-1]
        fullURL = baseURL + line
        try:
            req = urllib.request.Request(fullURL)
            resp = urllib.request.urlopen(req)
            if resp.getcode() == 404:
                print(status.no() + "'{0}' Error 404 has been detected").format(fullURL)
            else:
                print(status.ye(), "'{0}' has been found, Response code:" + colors.red() + "{1}".format(fullURL, resp.getcode()) + colors.reset())
                total_success += 1
        except:
            print(status.no() + "'{0}' has not been found".format(fullURL))
        line = f.readline()
    f.close()
    print(status.ok() + "Resume: " + colors.green(), total_success, colors.reset() + " / " + colors.white(), total_url, colors.reset() + " Urls have been founds")