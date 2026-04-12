"""
weather_prediction_app/app.py
=============================
Flask web application using Open-Meteo API
No API key needed!
"""

from flask import Flask, render_template, request, jsonify
import requests
import joblib
import numpy as np

app = Flask(__name__)

# ============================================
# Load trained ML model and scaler
# ============================================
model = joblib.load('model/weather_model.pkl')
scaler = joblib.load('model/scaler.pkl')

# ============================================
# Weather Code to Description Mapping
# ============================================
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    80: "Rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with hail",
    99: "Thunderstorm with heavy hail"
}

# ============================================
# Helper Functions
# ============================================

def get_coordinates(city):
    """
    Get latitude and longitude for a city using Open-Meteo geocoding
    """
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1&language=en"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if 'results' not in data or not data['results']:
            return None
        
        result = data['results'][0]
        return {
            'lat': result['latitude'],
            'lon': result['longitude'],
            'timezone': result.get('timezone', 'UTC'),
            'name': result['name'],
            'country': result.get('country', '')
        }
    except Exception as e:
        print(f"Geocoding error: {e}")
        return None

def get_weather_data(lat, lon, timezone):
    """
    Get current weather data from Open-Meteo API
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&current_weather=true"
        f"&hourly=relative_humidity_2m,pressure_msl,cloudcover,visibility"
        f"&timezone={timezone}"
        f"&forecast_days=1"
    )
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        current = data.get('current_weather', {})
        hourly = data.get('hourly', {})
        
        # Get current hour values
        humidity = hourly.get('relative_humidity_2m', [50])[0]
        pressure = hourly.get('pressure_msl', [1013])[0]
        cloudcover = hourly.get('cloudcover', [50])[0]
        visibility = hourly.get('visibility', [10])[0]
        
        return {
            'temperature': current.get('temperature', 0),
            'windspeed': current.get('windspeed', 0),
            'winddirection': current.get('winddirection', 0),
            'weathercode': current.get('weathercode', 0),
            'time': current.get('time', ''),
            'humidity': humidity if humidity is not None else 50,
            'pressure': pressure if pressure is not None else 1013,
            'cloud_cover': cloudcover if cloudcover is not None else 50,
            'visibility': (visibility / 1000) if visibility is not None else 10  # Convert to km
        }
    except Exception as e:
        print(f"Weather API error: {e}")
        return None

def get_forecast(lat, lon, timezone):
    """
    Get 5-day forecast from Open-Meteo API
    """
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}"
        f"&daily=temperature_2m_max,temperature_2m_min,weathercode,precipitation_sum"
        f"&timezone={timezone}"
        f"&forecast_days=5"
    )
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        daily = data.get('daily', {})
        
        forecast = []
        for i in range(len(daily.get('time', []))):
            forecast.append({
                'date': daily['time'][i],
                'temp_max': daily['temperature_2m_max'][i],
                'temp_min': daily['temperature_2m_min'][i],
                'weathercode': daily['weathercode'][i],
                'precipitation': daily['precipitation_sum'][i]
            })
        
        return forecast
    except Exception as e:
        print(f"Forecast API error: {e}")
        return []

def predict_temperature(weather_data):
    """
    Use ML model to predict next hour temperature
    """
    features = np.array([[
        weather_data['temperature'],
        weather_data['humidity'],
        weather_data['pressure'],
        weather_data['windspeed'],
        weather_data['cloud_cover'],
        weather_data['visibility']
    ]])
    
    # Scale features
    features_scaled = scaler.transform(features)
    
    # Predict
    prediction = model.predict(features_scaled)[0]
    
    return round(prediction, 2)

# ============================================
# Routes
# ============================================

@app.route('/')
def home():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/weather', methods=['POST'])
def weather_api():
    """
    API endpoint to get weather data and ML prediction
    """
    try:
        data = request.get_json()
        city = data.get('city', '').strip()
        
        if not city:
            return jsonify({'success': False, 'error': 'Please enter a city name'}), 400
        
        # Step 1: Get coordinates
        coords = get_coordinates(city)
        if not coords:
            return jsonify({'success': False, 'error': f'City "{city}" not found'}), 404
        
        # Step 2: Get current weather
        weather = get_weather_data(coords['lat'], coords['lon'], coords['timezone'])
        if not weather:
            return jsonify({'success': False, 'error': 'Could not fetch weather data'}), 500
        
        # Step 3: Get forecast
        forecast = get_forecast(coords['lat'], coords['lon'], coords['timezone'])
        
        # Step 4: ML prediction
        predicted_temp = predict_temperature(weather)
        
        # Step 5: Prepare response
        response = {
            'success': True,
            'location': {
                'city': coords['name'],
                'country': coords['country'],
                'lat': coords['lat'],
                'lon': coords['lon']
            },
            'current': {
                'temperature': weather['temperature'],
                'humidity': weather['humidity'],
                'pressure': weather['pressure'],
                'wind_speed': weather['windspeed'],
                'cloud_cover': weather['cloud_cover'],
                'visibility': round(weather['visibility'], 1),
                'weather_code': weather['weathercode'],
                'weather_description': WEATHER_CODES.get(weather['weathercode'], 'Unknown')
            },
            'prediction': {
                'predicted_temperature': predicted_temp,
                'description': 'Next hour temperature prediction'
            },
            'forecast': forecast
        }
        
        return jsonify(response)
    
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# ============================================
# Run Server
# ============================================

if __name__ == '__main__':
    print("\n" + "=" * 50)
    print("🌤️  WEATHER PREDICTION APP")
    print("=" * 50)
    print("🚀 Server starting at: http://127.0.0.1:5000")
    print("=" * 50 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
