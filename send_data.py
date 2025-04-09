# import requests
# import random
# import time

# # Simulate getting sensor data
# def get_sensor_data():
#     temperature = random.uniform(20, 30)  # Random temperature between 20°C and 30°C
#     water_level = random.randint(0, 100)  # Random water level between 0 and 100%
#     light = random.randint(0, 1000)  # Random light level between 0 and 1000 lux
#     dust_density = random.uniform(0, 500)  # Random dust density between 0 and 500 µg/m³
#     co = random.uniform(0, 10)  # Random CO level between 0 and 10 ppm
#     co2 = random.uniform(300, 500)  # Random CO2 level between 300 and 500 ppm
#     return {
#         'temperature': temperature,
#         'water_level': water_level,
#         'light': light,
#         'dust_density': dust_density,
#         'co': co,
#         'co2': co2
#     }

# # Send sensor data to the Flask server
# def send_data_to_server(sensor_data):
#     url = 'http://127.0.0.1:5000/data'  # Flask server running locally (you can replace with your server URL)
#     try:
#         response = requests.post(url, json=sensor_data)
#         if response.status_code == 200:
#             print("Data sent successfully!")
#         else:
#             print(f"Failed to send data: {response.status_code}")
#     except Exception as e:
#         print(f"Error sending data: {e}")

# while True:
#     # Get simulated sensor data
#     sensor_data = get_sensor_data()
    
#     # Send data to Flask server
#     send_data_to_server(sensor_data)
    
#     # Wait for 5 seconds before sending data again
#     time.sleep(5)
