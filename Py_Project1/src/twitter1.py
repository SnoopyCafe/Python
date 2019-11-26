import urllib
import twurl
from _socket import socket

TWITTER_URL = 'https://api.twitter.com/1.1/statuses/user_timeline.json'

while True:
    print('')
    acct = input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': '2'} )
    print('Retrieving', url)
    #connection = urllib.urlopen(url)
    connection = urllib.request.urlopen(url, None, socket.timeout)
    data = connection.read()
    print(data[:250])
    headers = connection.info().dict
    # print headers
    print('Remaining', headers['x-rate-limit-remaining'])
