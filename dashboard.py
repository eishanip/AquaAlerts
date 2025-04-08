import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(
    page_title="IoT Water Quality Dashboard",
    layout="wide",
    page_icon="💧"
)

st.markdown(
    "<h1 style='text-align: center; color: #4B9CD3;'>💧 IoT-Based Real-Time Water Quality Monitoring</h1>",
    unsafe_allow_html=True
)

firebase_url = "https://iot-water-quality-fa957-default-rtdb.firebaseio.com/water_quality_data.json"
response = requests.get(firebase_url)
data = response.json()

if not data:
    st.warning("⚠️ No data received from Firebase.")
else:
    # 🔄 Convert Firebase data to DataFram
    records = [entry for entry in data.values()]
    df = pd.DataFrame(records)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    df.sort_values('Timestamp', inplace=True)

    for col in ['SampleType', 'Warning']:
        if col in df.columns:
            df.drop(columns=[col], inplace=True)


    showable = df.dropna(subset=["pH", "TDS", "Turbidity", "Temperature", "Humidity"])

    def is_ecosystem_healthy(row):
        if 6.5 <= row['pH'] <= 8.5 and row['TDS'] < 500 and row['Turbidity'] < 10:
            return "🟢 Healthy Ecosystem"
        elif 6.0 <= row['pH'] <= 9.0 and row['TDS'] < 1000 and row['Turbidity'] <= 15:
            return "🟡 Moderate – Monitor Closely"
        else:
            return "🔴 Unhealthy – Needs Attention"

    showable['Suitability'] = showable.apply(is_ecosystem_healthy, axis=1)
    latest = showable.iloc[-1]

  
    st.markdown(f"### 🌿 Ecosystem Health Status: **{latest['Suitability']}**")
    if "Healthy" in latest['Suitability']:
        st.success("✅ Water conditions are optimal for aquatic life.")
    elif "Moderate" in latest['Suitability']:
        st.warning("⚠️ Water quality is within tolerable range. Monitoring recommended.")
    else:
        st.error("🚨 Water quality is poor. May harm aquatic organisms.")

    # 📊 Key Sensor Metrics
    st.markdown("---")
    st.subheader("📊 Latest Sensor Readings")
    cols = st.columns(5)
    cols[0].metric("🌡️ Temperature (°C)", f"{latest['Temperature']:.2f}")
    cols[1].metric("💧 pH Level", f"{latest['pH']:.2f}")
    cols[2].metric("🔍 TDS (ppm)", f"{latest['TDS']:.2f}")
    cols[3].metric("🌫️ Turbidity (NTU)", f"{latest['Turbidity']:.2f}")
    cols[4].metric("💨 Humidity (%)", f"{latest['Humidity']:.2f}")

    # 📋 Table View
    st.markdown("### 🗂️ Sensor Data (Latest 10 entries)")
    st.dataframe(showable.tail(10).reset_index(drop=True), use_container_width=True)

    # 📈 Trends with Slider
    st.markdown("### 📈 Sensor Trends Over Time")
    limit = st.slider("📉 Select number of recent readings to visualize:",
                      min_value=10, max_value=len(showable), value=30, step=5)
    filtered = showable.tail(limit)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**pH & TDS**")
        st.line_chart(filtered.set_index('Timestamp')[['pH', 'TDS']])
    with col2:
        st.markdown("**Turbidity, Temperature & Humidity**")
        st.line_chart(filtered.set_index('Timestamp')[['Turbidity', 'Temperature', 'Humidity']])

    # 💾 CSV Export
    with st.container():
        st.markdown("### 📥 Export")
        st.download_button(
            label="⬇️ Download CSV",
            data=showable.to_csv(index=False),
            file_name="iot_water_data.csv",
            mime="text/csv"
        )

# ♻️ Carbon Emission Estimator
with st.expander("♻️ Estimate Carbon Emission of This Dashboard"):
    if st.button("🔍 Calculate Carbon Impact"):
        page_size_kb = 150
        load_time_min = 0.1
        carbon_per_kwh = 442
        energy_per_gb = 0.81

        data_transfer_carbon = ((page_size_kb / 1024) / 1024) * energy_per_gb * carbon_per_kwh
        server_carbon = 0.0001 * carbon_per_kwh
        client_carbon = 0.00043 * load_time_min * carbon_per_kwh
        total_carbon = data_transfer_carbon + server_carbon + client_carbon

        st.success(f"🌍 Estimated Carbon Footprint: **{total_carbon:.4f} g CO₂** per visit")
        st.caption("Based on the formulas from your Cloud Computing Research Paper.")
