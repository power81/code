#webservice
from flask import Flask, jsonify
app = Flask(__name__) #createing object of flask module
@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello, World!')
if __name__ == '__main__':
    app.run(debug=True)
    
#distributed_application
import requests
def consume_web_service(app_id):
    response = requests.get('http://127.0.0.1:5000/api/hello?app_id=1')
    print( response.json()['message'])
if __name__ == '__main__':
    consume_web_service(1)


    
