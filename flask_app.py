from flask import Flask, jsonify

app = Flask(__name__)

# Create a global variable to store GPS coordinates
gps_coordinates = {'latitude': 0, 'longitude': 0}

# Route to retrieve the GPS coordinates
@app.route('/get_gps_coordinates', methods=['GET'])
def get_gps_coordinates():
    return jsonify(gps_coordinates)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Run on a different port, e.g., 5001