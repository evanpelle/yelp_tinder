#!venv/bin/python

import json
import threading
import Queue
import time

from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/swipe', methods=['GET'])
def swipe():
    rest_data = getYelpData(request.args.get('city'))
    return render_template('swipe.html', rest_data=rest_data)


def getData(q,city, offset):
    q.put(client.search(city, term='food', offset=offset).businesses)

def getYelpData(city):
    #r1 = client.search(city, term='food')
    #r2 = client.search(city, term='food', offset=20)
    #r3 = client.search(city, term='food', offset=40)
    #businesses = r1.businesses + r2.businesses + r3.businesses
    q = Queue.Queue()
    for offset in [0,20,40]:
        t = threading.Thread(target=getData, args = (q,city, offset))
        t.daemon = True
        t.start()
    while q.qsize() < 3:
        time.sleep(.01)
    businesses = []
    while not q.empty():
        businesses += q.get()
    response_list = []
    for restaurant in businesses:
        img_list = list(restaurant.image_url)
        img_list[-5] = 'o'
        del img_list[-6]
        image_url = u''.join(img_list)
        response_list.append(
            {
                'name': restaurant.name,
                'rating': restaurant.rating.rating,
                'image': image_url,
                'url': restaurant.url
            }
        )
    return json.dumps(response_list)

auth = Oauth1Authenticator(
    consumer_key="6U-EYdtGCpNoaq5PqqQz-g",
    consumer_secret="RfOJP1Dlzz-J0h-k1fu9O_tdMT8",
    token="0WujndcH-wshwjSHdTm1x-hWh52YytIX",
    token_secret="3O1Nyl4E2glK5Eo3MzrjlEXoOMw"  
)
client = Client(auth)

if __name__ == '__main__': 
    app.run(debug=True)
