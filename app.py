from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "7e5f26fc1052c5a37ddcc39ac8ad43eb"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    
    if not city:
        return jsonify({"error": "Please provide a city name"}), 400

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url).json()

    if response.get("cod") != 200:
        return jsonify({"error": response.get("message", "City not found")}), 404

    data = {
        "city": response["name"],
        "temperature": response["main"]["temp"],
        "temp_min": response["main"]["temp_min"],
        "temp_max": response["main"]["temp_max"],
        "description": response["weather"][0]["description"],
        "humidity": response["main"]["humidity"],
        "wind_speed": response["wind"]["speed"],
        "weather_icon": response["weather"][0]["icon"]
    }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)