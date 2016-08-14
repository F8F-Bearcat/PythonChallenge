import os, sys, time
from stat import *

def walktree(top, callback):
    '''  comments to go here ... '''
    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname, mode)
        else:
            # unknown file type, print a message
            print 'Skipping ', str(pathname)

def visitfile(file, mode):
    print 'visiting', file
    print time.ctime(os.stat(file).st_atime)
    print time.ctime(os.stat(file).st_mtime)
    print time.ctime(os.stat(file).st_ctime)
    print os.stat(file).st_size
    print os.stat(file).st_mode

'''
if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)
'''

#dt_file = 'C:\Customers'
dt_file = 'C:\Program Files'

walktree(dt_file, visitfile)