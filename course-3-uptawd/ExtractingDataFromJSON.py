import urllib.request, urllib.parse, urllib.error
import json

location = input('Enter Location: ')
print('Retrieving', location)

url = urllib.request.urlopen(location)
data = url.read().decode()

sum = 0
js = json.loads(data)
for item in js['comments']:
    num = int(item['count'])
    sum += num

print(sum)

