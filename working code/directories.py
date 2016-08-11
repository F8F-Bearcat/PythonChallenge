import os

top = 'C:/'
desktop = 'C:/Users/andyd/desktop'
os.chdir(top)
dirs = os.listdir('.')
os.chdir(desktop)

for d in dirs:
    print top + d


