import urllib.request, urllib.parse, urllib.error
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Twurl is a curl-like application, tailored specifically for the Twitter API.
# Need to install Twurl.
while True:
    print(' ')
    acc = input('Enter Twitter Account: ')
    if (len(acc) < 1):
        break

    url = twurl.argument(TWITTER_URL,
                         {'screen_name' : acc, 'count' : 5})
    print('Retrieving', url)

    connection = urllib.request.urlopen(url)
    data = connection.read().decode()
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.load(data)
    print(json.dumps(js, indent=4))

    for user in js['users']:
        print(user['screen_name'])
        s = user['status']['text']
        print('  ', s[:50])
