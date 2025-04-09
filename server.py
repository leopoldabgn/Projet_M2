from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Autorise les requêtes cross-origin

LOG_FILE = 'pixels_log.txt'

@app.route('/', methods=['POST', 'OPTIONS'])
def collect():
    if request.method == 'OPTIONS':
        return '', 200  # Répond proprement au preflight

    data = request.get_json()
    if not data or not all(k in data for k in ('x', 'y', 'time')):
        return jsonify({'error': 'Invalid payload'}), 400

    try:
        x = int(data['x'])
        y = int(data['y'])
        time = float(data['time'])
    except:
        return jsonify({'error': 'Invalid data'}), 400

    with open(LOG_FILE, 'a') as f:
        f.write(f"{x},{y},{time:.6f}\n")

    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
