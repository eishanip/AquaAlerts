# IoT-Based Water Quality Monitoring Project: pH, Turbidity, and Total Dissolved Solids (TDS)

## Overview

AquaAlerts is an IoT-based water quality monitoring system designed for aquaculture environments like fish ponds. It helps fish farmers track essential physio-chemical parameters such as temperature, pH, turbidity, and water levels. The system includes real-time alerts and a web dashboard, empowering users to maintain healthy aquatic conditions and reduce fish mortality.

- **Real-time Monitoring**: Measures pH, turbidity, temperature, and water level using sensors
- **Live Dashboard**: Visualizes water quality parameters with easy-to-read graphs and indicators
- **SMS Alerts**: Sends SMS notifications when values exceed critical thresholds
- **Historical Data Logging**: Stores past data to identify trends and support long-term analysis
- **User-friendly Interface**: Minimal and functional web dashboard built with Flask and HTML/CSS
- **Offline Edge Sensing**: On-device microcontroller continuously collects data even when offline

## Technologies Used

- **ESP32 (with Arduino)**: Microcontroller to interface with water sensors
- **Sensors**:
  - pH Sensor
  - Turbidity Sensor
  - Temperature Sensor (DS18B20)
  - Ultrasonic Sensor for water level
- **Python Flask**: Backend for data ingestion, processing, and visualisation
- **SQLite**: Lightweight database for logging sensor data
- **Twilio API**: Sends SMS alerts for abnormal water conditions
- **Chart.js**: Renders dynamic charts on the dashboard
- **Bootstrap**: Styling framework for responsive UI

## Live Website

The website is currently deployed on -
https://iot-water-quality-monitor-2.onrender.com/

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/eishanip/AquaAlerts.git
   ```

2. Navigate to the project directory:

   ```bash
   cd AquaAlerts
   ```

3. Install required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask server:

   ```bash
   python app.py
   ```

5. Open your browser and go to `http://localhost:5000` to view the dashboard.

## Usage

- Upload sensor data to the ESP32 via Arduino code (`iot_code/`)
- The ESP32 pushes data to the Flask backend via HTTP
- The Flask app logs data to SQLite and updates the dashboard
- When values like pH or turbidity cross danger levels, SMS alerts are sent
- The dashboard provides a snapshot of current values and trends

## Project Structure

```
AquaAlerts/
├── iot_code/               # Arduino code for ESP32 + sensors
├── static/                 # Static assets (CSS, JS)
├── templates/              # HTML templates for Flask
├── app.py                  # Main Flask server
├── database.db             # SQLite database
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Alert System

- **pH Threshold**: Below 6.5 or above 8.5 triggers an alert
- **Turbidity Threshold**: Above 100 NTU triggers an alert
- **Temperature**: Alerts if outside optimal fish-farming range (25°C–30°C)
- **Water Level**: Alerts if water is too low or overflowing

## Sensors and Calibration

Each sensor is calibrated and tested for use in field conditions:
- **DS18B20**: Waterproof, calibrated for 0.5°C accuracy
- **pH Sensor**: Calibrated using buffer solutions (pH 4, 7, 10)
- **Turbidity Sensor**: Based on light scattering method
- **Ultrasonic Sensor**: Distance measured and mapped to water depth

## Dashboard Features

- Live readings with timestamps
- Color-coded cards indicating safe or dangerous ranges
- Trendline graphs for each parameter over time
- Auto-refresh every 10 seconds for near real-time updates

## Team Members

- **Eishani Purohit** (22BIT0362)
- **Aaryan Malik** (22BIT0520)
- **Siddhartha Pal** (22BIT0024)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Developed as part of the "Industry 4.0 and Enabling Technologies" VAC at VIT
- Selected for presentation before professors from Middlesex University, UK
- Special thanks to the faculty mentors and field experts for their valuable feedback
