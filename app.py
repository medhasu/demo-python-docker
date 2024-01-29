from flask import Flask,render_template,request,redirect
import redis
import os
config_cache={}
def config_value(key,default_value):
    if key in config_cache:
        return config_cache[key]
    v = ''
    if key in os.environ:
        return os.environ[key]
    if len(v)==0:
        v = default_value
    config_cache[key] = v
    return v

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/items')
@app.route('/items')
def list_items():
    r = redis.Redis(host=config_value('REDIS_HOST','localhost'), port=int(config_value('REDIS_PORT','8001')), db=int(config_value('REDIS_DB','0')))
    items = []
    for key in r.scan_iter():
        items.append(key)
    return render_template('list.html',keys=items)
@app.route('/items',methods=["POST"])
def createjob():
    r = redis.Redis(host=config_value('REDIS_HOST','localhost'), port=int(config_value('REDIS_PORT','8001')), db=int(config_value('REDIS_DB','0')))
    job=request.form['key']
    val=request.form['val']
    r.set(job,val)
    return 'created'
@app.route('/items/<job>',methods=["GET"])
def fetch_job(job):
    r = redis.Redis(host=config_value('REDIS_HOST','localhost'), port=int(config_value('REDIS_PORT','8001')), db=int(config_value('REDIS_DB','0')))
    return  r.get(job).decode('ascii')  
    
app.run(host='0.0.0.0', port=8009)