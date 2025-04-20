import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import random

# Simulasi data real-time dummy
def get_sensor_data():
    return {
        "Suhu": random.randint(50, 100),
        "Kelembaban": random.randint(30, 70),
        "CO2": random.randint(20, 60),
        "Okupansi": random.randint(10, 90),
        "Listrik": random.randint(5, 50),
        "Intensitas Cahaya": [random.randint(20, 100) for _ in range(4)],
        "Kebisingan": [random.randint(20, 100) for _ in range(4)],
        "LPG": [random.randint(20, 100) for _ in range(4)]
    }

# Function untuk membuat gauge chart
def gauge_chart(title, value, color):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = value,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': f"<b>{title}</b>", 'font': {'size': 16}},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': color},
            'bgcolor': "lightgray",
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 90}
        }
    ))
    fig.update_layout(margin=dict(t=20, b=10, l=10, r=10), height=220)
    return fig

# Layout
st.set_page_config(layout="wide")
st.title("📊 Smart Monitoring Dashboard")

# Auto refresh (simulasi real-time)
st.markdown(f'<meta http-equiv="refresh" content="5">', unsafe_allow_html=True)

# Get simulated data
data = get_sensor_data()

# Bagian atas: Gauge Charts
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.plotly_chart(gauge_chart("Suhu", data["Suhu"], "#00695C"), use_container_width=True)
with col2:
    st.plotly_chart(gauge_chart("Kelembaban", data["Kelembaban"], "#00897B"), use_container_width=True)
with col3:
    st.plotly_chart(gauge_chart("Kadar CO2", data["CO2"], "#00ACC1"), use_container_width=True)
with col4:
    st.plotly_chart(gauge_chart("Okupansi Ruangan", data["Okupansi"], "#00BCD4"), use_container_width=True)
with col5:
    st.plotly_chart(gauge_chart("Penggunaan Listrik", data["Listrik"], "#26C6DA"), use_container_width=True)

# Bar chart data
months = ["Jan", "Feb", "Mar", "Apr"]
df_cahaya = pd.DataFrame({"Month": months, "Value": data["Intensitas Cahaya"]})
df_kebisingan = pd.DataFrame({"Month": months, "Value": data["Kebisingan"]})
df_lpg = pd.DataFrame({"Month": months, "Value": data["LPG"]})

# Bar charts
st.markdown("### 📈 Monitoring Faktor Lingkungan")

col6, col7, col8 = st.columns(3)

def horizontal_bar(title, df, color):
    fig = px.bar(df, x="Value", y="Month", orientation='h', color_discrete_sequence=[color])
    fig.update_layout(title=title, height=300, margin=dict(t=40, b=10, l=10, r=10))
    return fig

with col6:
    st.plotly_chart(horizontal_bar("Intensitas Cahaya", df_cahaya, "#FBC02D"), use_container_width=True)

with col7:
    st.plotly_chart(horizontal_bar("Kebisingan", df_kebisingan, "#F9A825"), use_container_width=True)

with col8:
    st.plotly_chart(horizontal_bar("Kebocoran LPG", df_lpg, "#F57F17"), use_container_width=True)

st.caption("©️ 2025 Dashboard by Kamu 🚀")
