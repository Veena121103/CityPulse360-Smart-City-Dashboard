import streamlit as st
import pandas as pd

# ====================================
# PAGE SETTINGS
# ====================================

st.set_page_config(
    page_title="CityPulse360",
    layout="wide"
)

# ====================================
# TITLE
# ====================================

st.title("🚀 CityPulse360 - Smart City Dashboard")

# ====================================
# LOAD DATASETS
# ====================================

traffic_df = pd.read_csv("data/traffic_cleaned.csv")

aqi_df = pd.read_csv("data/aqi_cleaned.csv")

# ====================================
# KPI CALCULATIONS
# ====================================

avg_traffic = int(
    traffic_df["traffic_volume"].mean()
)

max_pm25 = round(
    aqi_df["pm25"].max(),
    2
)

good_days = len(
    aqi_df[
        aqi_df["pollution_level"] == "Good"
    ]
)

# ====================================
# KPI CARDS
# ====================================

col1, col2, col3 = st.columns(3)

col1.metric(
    "🚗 Average Traffic",
    avg_traffic
)

col2.metric(
    "🌫 Max PM2.5",
    max_pm25
)

col3.metric(
    "✅ Good AQI Days",
    good_days
)

st.divider()

# ====================================
# TRAFFIC ANALYTICS
# ====================================

st.header("🚦 Traffic Analytics")

st.dataframe(
    traffic_df.head()
)

st.bar_chart(
    traffic_df["traffic_volume"].head(30)
)

# High congestion alerts
high_congestion = traffic_df[
    traffic_df["congestion_level"] == "High"
]

st.warning(
    f"⚠ High congestion records found: {len(high_congestion)}"
)

st.divider()

# ====================================
# AQI ANALYTICS
# ====================================

st.header("🌫 AQI Analytics")

st.dataframe(
    aqi_df.head()
)

st.line_chart(
    aqi_df["pm25"].head(50)
)

# Pollution alerts
poor_air = aqi_df[
    aqi_df["pollution_level"] == "Poor"
]

st.error(
    f"🚨 Poor AQI records found: {len(poor_air)}"
)

# ====================================
# SYSTEM STATUS
# ====================================

st.success(
    "✅ CityPulse360 Streaming System Operational"
)

# ====================================
# AI ALERT ENGINE
# ====================================

st.divider()

st.header("🤖 AI Smart Alerts")

# Traffic anomaly detection
if avg_traffic > 3000:

    st.error(
        "🚨 AI ALERT: Unusual traffic congestion detected!"
    )

# Pollution anomaly detection
if max_pm25 > 300:

    st.warning(
        "⚠ AI ALERT: Dangerous pollution levels detected!"
    )

# Stable city condition
if avg_traffic < 3000 and max_pm25 < 300:

    st.success(
        "✅ AI Status: City conditions are stable."
    )

# ====================================
# AI SUMMARY
# ====================================

st.divider()

st.header("🧠 AI City Summary")

summary = f'''
Average city traffic volume is {avg_traffic} vehicles.

Maximum PM2.5 recorded is {max_pm25}.

Total high congestion records detected:
{len(high_congestion)}

Total poor AQI records detected:
{len(poor_air)}

AI recommends monitoring congestion and pollution hotspots continuously.
'''

st.info(summary)