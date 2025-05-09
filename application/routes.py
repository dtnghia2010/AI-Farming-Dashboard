from flask import render_template, request, jsonify
from datetime import datetime, timedelta
from application import app, db  # Import app and db from __init__.py
from application.models import SensorData

points = 20

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

# @app.route('/temperature_data', methods=['GET'])
# def temperature_data():
#     # Calculate the timestamp for 30 minutes ago
#     thirty_minutes_ago = datetime.utcnow() - timedelta(minutes=30)
    
#     # Query the temperature data for the last 30 minutes
#     data = SensorData.query.filter(SensorData.timestamp >= thirty_minutes_ago).order_by(SensorData.timestamp.asc()).all()
    
#     # Format data to send to the frontend (time and temperature)
#     temperatures = [{'timestamp': d.timestamp, 'temperature': d.temperature} for d in data]
    
#     if temperatures:
#         return jsonify(temperatures)
#     else:
#         return jsonify({'error': 'No data available'}), 404

@app.route('/temperature_data', methods=['GET'])
def temperature_data():
    # Get the 10 most recent sensor data entries
    data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(points).all()

    # Format the data to send to the frontend (time and temperature)
    temperatures = [{'timestamp': d.timestamp.isoformat(), 'temperature': d.temperature} for d in data]

    if temperatures:
        return jsonify(temperatures)
    else:
        return jsonify({'error': 'No data available'}), 404
    

@app.route('/water_level_data', methods=['GET'])
def water_level_data():
    # Get the 10 most recent water level data entries
    data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(points).all()

    # Format the data to send to the frontend (time and water level)
    water_levels = [{'timestamp': d.timestamp.isoformat(), 'water_level': d.water_level} for d in data]

    if water_levels:
        return jsonify(water_levels)
    else:
        return jsonify({'error': 'No data available'}), 404

@app.route('/light_data', methods=['GET'])
def light_data():
    # Get the 10 most recent light data entries
    data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(points).all()
    light_levels = [{'timestamp': d.timestamp.isoformat(), 'light': d.light} for d in data]
    if light_levels:
        return jsonify(light_levels)
    else:
        return jsonify({'error': 'No data available'}), 404

@app.route('/dust_density_data', methods=['GET'])
def dust_density_data():
    # Get the 10 most recent dust density data entries
    data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(points).all()
    dust_densities = [{'timestamp': d.timestamp.isoformat(), 'dust_density': d.dust_density} for d in data]
    if dust_densities:
        return jsonify(dust_densities)
    else:
        return jsonify({'error': 'No data available'}), 404

@app.route('/co_data', methods=['GET'])
def co_data():
    # Get the 10 most recent CO data entries
    data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(points).all()
    co_levels = [{'timestamp': d.timestamp.isoformat(), 'co': d.co} for d in data]
    if co_levels:
        return jsonify(co_levels)
    else:
        return jsonify({'error': 'No data available'}), 404

@app.route('/co2_data', methods=['GET'])
def co2_data():
    # Get the 10 most recent CO2 data entries
    data = SensorData.query.order_by(SensorData.timestamp.desc()).limit(points).all()
    co2_levels = [{'timestamp': d.timestamp.isoformat(), 'co2': d.co2} for d in data]
    if co2_levels:
        return jsonify(co2_levels)
    else:
        return jsonify({'error': 'No data available'}), 404
