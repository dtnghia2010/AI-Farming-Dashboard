from flask import render_template, request, jsonify
from datetime import datetime, timedelta
from application import app, db  # Import app and db from __init__.py
from application.models import SensorData

@app.route('/')
def plant():
    # Get the latest sensor data from the database
    latest_data = SensorData.query.order_by(SensorData.timestamp.desc()).first()
    return render_template('dashboard.html', latest_data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()  # Get data sent by Raspberry Pi

    # Print the incoming data for debugging
    print(f"Received data: {data}")

    # Extract data from the incoming JSON payload
    temp = data.get('temp')
    water_level = data.get('wtlv')
    light = data.get('lux')
    dust_density = data.get('dust')
    co = data.get('co')
    co2 = data.get('co2')

    # Store the data in the database
    new_data = SensorData(
        temperature=temp,
        water_level=water_level,
        light=light,
        dust_density=dust_density,
        co=co,
        co2=co2,
        timestamp=datetime.utcnow()
    )
    db.session.add(new_data)
    db.session.commit()

    return jsonify({'status': 'success'}), 200

@app.route('/latest_data', methods=['GET'])
def latest_data():
    # Get the latest sensor data from the database
    latest = SensorData.query.order_by(SensorData.timestamp.desc()).first()
    
    if latest:
        return jsonify({
            'temperature': f"{latest.temperature:.2f}",
            'water_level': f"{latest.water_level:.2f}",
            'light': f"{latest.light:.2f}",
            'dust_density': f"{latest.dust_density:.2f}",
            'co': f"{latest.co:.2f}",
            'co2': f"{latest.co2:.2f}"
        })
    else:
        return jsonify({'error': 'No data available'}), 404

@app.route('/temperature_data', methods=['GET'])
def temperature_data():
    # Calculate the timestamp for 30 minutes ago
    thirty_minutes_ago = datetime.utcnow() - timedelta(minutes=30)
    
    # Query the temperature data for the last 30 minutes
    data = SensorData.query.filter(SensorData.timestamp >= thirty_minutes_ago).order_by(SensorData.timestamp.asc()).all()
    
    # Format data to send to the frontend (time and temperature)
    temperatures = [{'timestamp': d.timestamp, 'temperature': d.temperature} for d in data]
    
    if temperatures:
        return jsonify(temperatures)
    else:
        return jsonify({'error': 'No data available'}), 404
