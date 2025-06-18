from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
API_KEY = 'your APIKEY'

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/weather', methods=['POST'])
def weather_result():
    city = request.form['city']
    url = f'網站的API'
    response = requests.get(url)
    if response.status_code != 200:
        return render_template('result.html', error='查詢失敗，請確認城市名稱是否正確')
    data = response.json()
    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind': data['wind']['speed'],
        'icon': data['weather'][0]['icon']
    }
    return render_template('result.html', weather=weather)

@app.route('/map')
def map_page():
    return render_template('index.html')

@app.route('/weather_by_coords', methods=['POST'])
def weather_by_coords():
    data = request.get_json()
    lat = data.get('lat')
    lon = data.get('lon')
    if lat is None or lon is None:
        return jsonify({'error': '經緯度無效'})
    url = f'網站的API'
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({'error': '查詢失敗'})
    data = response.json()
    weather = {
        'city': data['name'],
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description'],
        'humidity': data['main']['humidity'],
        'wind': data['wind']['speed'],
        'icon': data['weather'][0]['icon']
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
