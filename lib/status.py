from lib import colors

def st():
    start   = colors.reset() + "[" + colors.cyan() + "----" + colors.reset() + "]"
    return (start)

def iu():
    iu    = colors.reset() + "[" + colors.yellow() + " >> " + colors.reset() + "]"
    return (iu)

def ko():
    ko   = colors.reset() + "[" + colors.red() + " KO " + colors.reset() + "]"
    return (ko)

def ok():
    ok      = colors.reset() + "[" + colors.green() + " OK " + colors.reset() + "]"
    return (ok)

def io():
    io      = colors.reset() + "[" + colors.purple() + " ?? " + colors.reset() + "]"
    return (io)

def ye():
    ye      = colors.reset() + "[" + colors.yellow() + " -> " + colors.reset() + "]"
    return (ye)

def no():
    no      = colors.reset() + "[" + colors.red() + " NO " + colors.reset() + "]"
    return (no)

def info():
    no      = colors.reset() + "[" + colors.white() + "INFO" + colors.reset() + "]"
    return (no)