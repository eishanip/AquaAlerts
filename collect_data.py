import serial
import time
import firebase_admin
from firebase_admin import credentials, db

# Firebase setup
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://iot-water-quality-fa957-default-rtdb.firebaseio.com/'
})

# Arduino setup
arduino = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

# Classification logic
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

# Collect and send
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
