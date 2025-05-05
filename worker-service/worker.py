from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    result = f"Processed data: {data}"
    print(result)
    return jsonify({"status": "success", "result": result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000)
