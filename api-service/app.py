from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/send-task', methods=['POST'])
def send_task():
    data = request.json
    response = requests.post('http://worker-service:6000/process', json=data)
    return jsonify({"worker_response": response.json()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
