from flask import Flask,json,request
import os

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhookjotForm',methods=['POST','GET'])
def get_api():
    if(request.headers['Content-Type']=='application/json'):
        return json.dumps(request.json)


if __name__ == '__main__':
  app.run(port = int(os.environ.get("PORT", 5000)))