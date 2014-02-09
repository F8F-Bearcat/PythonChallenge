import requests
import string

partial_u = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
nothing = '8022'

i = 0

while( i < 400 ):
    u = partial_u + nothing
    r = requests.get(u)
    print r.text.encode('ascii', 'ignore')
    new_nothing = r.text.encode('ascii', 'ignore').split()[-1]
    #print new_nothing
    nothing = new_nothing
    i += 1
    
