from flask import Flask, request, jsonify
from flask_cors import CORS

from PIL import Image
import numpy as np
import os

def create_grayscale_image_from_log(file_path, output_dir='output'):
    pixels = {}

    # Lire et stocker les données
    with open(file_path, 'r') as f:
        last_val = None
        skip_mode = False
        last_x = None

        for line in f:
            parts = line.strip().split(',')
            if len(parts) != 3:
                continue
            x, y, val = map(int, parts)

            if last_val == 1 and val == 1:
                # Found two consecutive 1s -> enter skip mode
                skip_mode = True
                last_x = x
                continue  # Don't add this line

            if skip_mode:
                # Skip until x or y changes
                if x != last_x:
                    skip_mode = False  # Found a different coordinate
                else:
                    continue  # Still same, keep skipping


            pixels[(x, y)] = val
            last_val = val  # Update last value seen

    # Trouver dimensions de l'image
    all_x = [coord[0] for coord in pixels]
    all_y = [coord[1] for coord in pixels]

    width = max(all_x) + 1
    print(max(all_x))
    height = max(all_y) + 1
    print(max(all_y))

    # Créer une image vide blanche
    img_array = np.full((height, width), 255, dtype=np.uint8)  # par défaut tout blanc

    # Remplir avec les vraies valeurs
    for (x, y), value in pixels.items():
        if value > 37:                          # TODO: TEMPORAIRE
            value = 180                         # TODO: TEMPORAIRE
        img_array[y][x] = value

    # Créer le dossier de sortie si besoin
    os.makedirs(output_dir, exist_ok=True)

    # Trouver un nom de fichier disponible
    i = 1
    while True:
        output_path = os.path.join(output_dir, f"img{i}.png")
        if not os.path.exists(output_path):
            break
        i += 1

    # Créer et sauvegarder l'image
    img = Image.fromarray(img_array, mode='L')
    img.save(output_path)
    print(f"Image sauvegardée sous : {output_path}")

# --------------------------------------------
# --------------------------------------------

app = Flask(__name__)
CORS(app)  # Autorise les requêtes cross-origin

LOG_FILE = 'pixels_log.txt'

@app.route('/', methods=['POST', 'OPTIONS'])
def collect():
    if request.method == 'OPTIONS':
        return '', 200  # Répond proprement au preflight

    data = request.get_json()
    if not data or not all(k in data for k in ('x', 'y', 'rgb')):
        return jsonify({'error': 'Invalid payload'}), 400

    try:
        x = int(data['x'])
        y = int(data['y'])
        rgb = int(float(data['rgb']))  # cast float → int (juste au cas où c'est un float)
    except Exception as e:
        return jsonify({'error': f'Invalid data: {str(e)}'}), 400

    with open(LOG_FILE, 'a') as f:
        f.write(f"{x},{y},{rgb}\n")

    return jsonify({'status': 'ok'}), 200

@app.route('/generate-image', methods=['GET'])
def generate_image():
    try:
        create_grayscale_image_from_log(LOG_FILE)
        return jsonify({'status': 'image generated'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000)
    create_grayscale_image_from_log("pixels_log.txt")

