from datetime import datetime, date, time

start = datetime.now()

i = 0
while(i < 10000000):
    h = ((((((37)*37+37)*37+37)*37+37)*37+37)*37+37)*37
    i += 1

end = datetime.now()

print start
print end

