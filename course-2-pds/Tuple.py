name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hourDict = dict()
for line in handle:
    if line.startswith('From '):
        words = line.split()
        times = words[5]
        timeSplit = times.split(':')
        hour = timeSplit[0]
        
        if hour not in hourDict:
            hourDict[hour] = 1
        else:
            hourDict[hour] += 1

for (h, c) in sorted(hourDict.items()):
    print(h + ' ' + str(c))