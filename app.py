import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="YarnVision Quality Dashboard",
    page_icon="🧵",
    layout="wide"
)

st.title("🧵 YarnVision Quality & Defect Detection")
st.caption("Real-Time Optical Yarn Monitoring & Quality Telemetry")

# Sidebar - Test Configuration
st.sidebar.header("Test Parameters")
batch_id = st.sidebar.text_input("Batch ID", value="BATCH-2026-001")
yarn_count = st.sidebar.number_input("Nominal Count (Ne)", value=30)
target_speed = st.sidebar.slider("Target Speed (m/min)", 100, 400, 300)
test_length = st.sidebar.number_input("Target Length (m)", value=1000)

st.sidebar.divider()
run_test = st.sidebar.button("Start Quality Inspection", type="primary")

# Main Dashboard
col1, col2, col3, col4 = st.columns(4)

if run_test:
    st.success(f"Running Optical Inspection for Batch: {batch_id}")
    
    # Simulated Live Telemetry Data
    np.random.seed(42)
    neps = np.random.randint(5, 25)
    thick_places = np.random.randint(10, 45)
    thin_places = np.random.randint(2, 15)
    cv_percent = round(np.random.uniform(11.5, 14.8), 2)
    
    col1.metric("Neps / km (+200%)", neps)
    col2.metric("Thick Places / km (+50%)", thick_places)
    col3.metric("Thin Places / km (-50%)", thin_places)
    col4.metric("CV %", f"{cv_percent}%")
    
    st.subheader("Yarn Diameter Profile (mm)")
    chart_data = pd.DataFrame(
        np.random.normal(0.22, 0.03, size=(100, 1)),
        columns=["Diameter (mm)"]
    )
    st.line_chart(chart_data)

else:
    col1.metric("Neps / km (+200%)", "0")
    col2.metric("Thick Places / km (+50%)", "0")
    col3.metric("Thin Places / km (-50%)", "0")
    col4.metric("CV %", "0.0%")
    st.info("Configure test parameters on the sidebar and click 'Start Quality Inspection' to begin.")
    
