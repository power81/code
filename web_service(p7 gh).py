'''7. Create a simple web service and write any distributed application to consume the 
web service.'''

#web_service2.py

from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/api/service', methods=['GET'])
def service():
    message = request.args.get('message')
    return jsonify(message = f'Your name is {message}')
if __name__ == '__main__':
    app.run(debug=True)




#distributed_application2.py
import requests
def consume_web_service(message):
    response = requests.get(f'http://127.0.0.1:5000/api/service?message={message}')
    print(response.json()['message'])
if __name__ == '__main__':
    message = 'sample'
    consume_web_service(message)
 
