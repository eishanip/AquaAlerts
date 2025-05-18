import os
import json
import serial
import time
import firebase_admin
from firebase_admin import credentials, db

# Get Firebase credentials from environment variable
firebase_key_json = os.getenv('FIREBASE_KEY')
if not firebase_key_json:
    raise Exception("Missing FIREBASE_KEY environment variable.")

firebase_dict = json.loads(firebase_key_json)
firebase_dict["private_key"] = firebase_dict["private_key"].replace("\\n", "\n")

cred = credentials.Certificate(firebase_dict)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-water-quality-fa957-default-rtdb.firebaseio.com/'
})

# Setup Arduino (COM6 should be changed depending on OS/environment)
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

def predict_water_type(ph, tds, turbidity):
    if ph > 9.0:
        return "Soapy Water"
    elif ph < 5.5:
        return "Acidic Water"
    elif turbidity > 10:
        return "Muddy Water"
    elif tds > 1000:
        return "Hard Water / Industrial Waste"
    else:
        return "Normal Water"

while True:
    try:
        data = arduino.readline().decode('utf-8').strip()
        print("Raw Data:", data)

        if data:
            values = data.split('|')
            print("Parsed Values:", values)

            if len(values) == 5:
                try:
                    ph = float(values[0].strip())
                    tds = float(values[1].strip())
                    turbidity = float(values[2].strip())
                    temperature = float(values[3].strip())
                    humidity = float(values[4].strip())
                    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')

                    predicted_type = predict_water_type(ph, tds, turbidity)

                    db.reference('/water_quality_data').push({
                        'Timestamp': timestamp,
                        'pH': ph,
                        'TDS': tds,
                        'Turbidity': turbidity,
                        'Temperature': temperature,
                        'Humidity': humidity,
                        'PredictedType': predicted_type
                    })

                    print(f"✅ Sent: {timestamp} | Type: {predicted_type} | pH: {ph:.2f}")
                except ValueError:
                    print("⚠️ Invalid numeric values. Skipped:", values)
            else:
                db.reference('/water_quality_data').push({
                    'Timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                    'Warning': data
                })
                print("⚠️ Malformed data pushed as warning.")
        else:
            print("⚠️ No data received.")

        time.sleep(2)

    except Exception as e:
        print(f"🔥 Error: {e}")
