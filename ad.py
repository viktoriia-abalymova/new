import redis
from flask import Flask
from time import strftime
from flask import request
from flask import jsonify


app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route('/', methods=["GET"])
def counter_ip():
    if redis.set("ip:", 1):
       return request.set("ip")[0]
    else:
       return ip = request.remote_addr

def theanswer():
    day = strftime("%Y-%m-%d")
    r.incr('page:index:counter:'+day)
    return '42 - ' + str(r.get('page:index:counter:'+day))

