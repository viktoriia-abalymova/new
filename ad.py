import redis
from flask import Flask
from time import strftime
from flask import request
from flask import jsonify


app = Flask(__name__)
r = redis.Redis(host='localhost', port=6379, db=0)

@app.route("/get_ip", methods=["GET"])
def get_ip():
    return jsonify({'ip': request.remote_addr}), 200

@app.route('/')
def theanswer():
    day = strftime("%Y-%m-%d")
    r.incr('page:index:counter:'+day)
    return '42 - ' + str(r.get('page:index:counter:'+day))
