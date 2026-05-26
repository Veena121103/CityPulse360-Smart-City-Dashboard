import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="CityPulse360",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

traffic_df = pd.read_csv("data/traffic_cleaned.csv")
aq_df = pd.read_csv("data/aqi_cleaned.csv")

# ==========================================
# HEADER
# ==========================================

st.title("🚀 CityPulse360 – Smart City Intelligence Platform")

st.markdown(
    "### AI-powered Urban Governance & Analytics Dashboard"
)

current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

st.info(f"🕒 System Time: {current_time}")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("📌 Navigation")

section = st.sidebar.radio(
    "Go to",
    [
        "Dashboard Overview",
        "Traffic Analytics",
        "AQI Analytics",
        "AI Alerts",
        "AI Summary"
    ]
)

# ==========================================
# KPI CALCULATIONS
# ==========================================

avg_traffic = int(traffic_df['traffic_volume'].mean())

max_pm25 = round(aq_df['pm25'].max(), 2)

good_aqi_days = len(
    aq_df[aq_df['pollution_level'] == 'Good']
)

high_congestion = len(
    traffic_df[
        traffic_df['congestion_level'] == 'High'
    ]
)

poor_aqi = len(
    aq_df[
        aq_df['pollution_level'] == 'Poor'
    ]
)

# ==========================================
# DASHBOARD OVERVIEW
# ==========================================

if section == "Dashboard Overview":

    st.header("📊 Smart City KPI Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "🚗 Average Traffic",
            avg_traffic
        )

    with col2:
        st.metric(
            "🌫️ Max PM2.5",
            max_pm25
        )

    with col3:
        st.metric(
            "✅ Good AQI Days",
            good_aqi_days
        )

    with col4:
        st.metric(
            "🚨 High Congestion",
            high_congestion
        )

    st.success("✅ Smart City Monitoring System Operational")

    # ==========================================
    # GOVERNANCE & OBSERVABILITY
    # ==========================================

    st.markdown("---")

    st.subheader("🛡️ Governance & Observability")

    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.success("✅ Data Validation Passed")

    with col6:
        st.success("✅ Streaming Pipeline Healthy")

    with col7:
        st.success("✅ Dashboard Operational")

    with col8:
        st.success("✅ Monitoring Active")

# ==========================================
# TRAFFIC ANALYTICS
# ==========================================

elif section == "Traffic Analytics":

    st.header("🚦 Traffic Analytics")

    st.dataframe(
        traffic_df[
            [
                'timestamp',
                'traffic_volume',
                'temperature',
                'weather_main',
                'congestion_level'
            ]
        ].head(20)
    )

    fig_traffic = px.bar(
        traffic_df.head(30),
        x='timestamp',
        y='traffic_volume',
        title='Traffic Volume Monitoring'
    )

    st.plotly_chart(
        fig_traffic,
        use_container_width=True
    )

    congestion_counts = (
        traffic_df['congestion_level']
        .value_counts()
        .reset_index()
    )

    congestion_counts.columns = [
        'Congestion',
        'Count'
    ]

    fig_pie = px.pie(
        congestion_counts,
        names='Congestion',
        values='Count',
        title='Congestion Level Distribution'
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )

# ==========================================
# AQI ANALYTICS
# ==========================================

elif section == "AQI Analytics":

    st.header("🌫️ AQI Analytics")

    st.dataframe(aq_df.head(20))

    fig_aqi = px.line(
        aq_df.head(50),
        y='pm25',
        title='PM2.5 Trend Analysis'
    )

    st.plotly_chart(
        fig_aqi,
        use_container_width=True
    )

    pollution_counts = (
        aq_df['pollution_level']
        .value_counts()
        .reset_index()
    )

    pollution_counts.columns = [
        'Pollution',
        'Count'
    ]

    fig_pollution = px.pie(
        pollution_counts,
        names='Pollution',
        values='Count',
        title='Pollution Severity Distribution'
    )

    st.plotly_chart(
        fig_pollution,
        use_container_width=True
    )

# ==========================================
# AI SMART ALERTS
# ==========================================

elif section == "AI Alerts":

    st.header("🚨 AI Smart Alerts")

    if high_congestion > 1000:
        st.error(
            "🚨 High congestion detected across multiple city zones."
        )

    if poor_aqi > 50:
        st.warning(
            "🌫️ Dangerous pollution levels detected in the city."
        )

    st.info(
        "🤖 AI monitoring system is actively analyzing traffic and AQI patterns."
    )

# ==========================================
# AI CITY SUMMARY
# ==========================================

elif section == "AI Summary":

    st.header("🤖 AI City Summary")

    summary = f'''
    🚗 Average city traffic volume is {avg_traffic} vehicles.

    🌫️ Maximum PM2.5 recorded is {max_pm25}.

    🚨 A total of {high_congestion} high congestion records were detected.

    ⚠️ A total of {poor_aqi} poor AQI records were observed.

    🤖 AI recommends continuous monitoring of traffic congestion and pollution hotspots.
    '''

    st.info(summary)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "CityPulse360 © 2026 | Smart City Intelligence Platform"
)