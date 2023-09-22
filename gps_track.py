from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)

# Initialize variables to store GPS data
latitude = 0
longitude = 0

@app.route('/')
def index():
    return render_template('https://profile-nameless.github.io/prototypemap/')

@app.route('/get_gps_coordinates', methods=['GET'])
def get_gps_coordinates():
    global latitude, longitude
    return jsonify({'latitude': latitude, 'longitude': longitude})

@app.route('/simulate_gps', methods=['POST'])
def simulate_gps():
    global latitude, longitude
    # Simulate GPS data (for testing purposes)
    latitude = random.uniform(-90, 90)
    longitude = random.uniform(-180, 180)
    return jsonify({'status': 'Data updated successfully'})

if __name__ == '__main__':
    app.run(debug=True,port=8080,use_reloader=False)


 