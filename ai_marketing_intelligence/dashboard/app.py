import streamlit as st
import pandas as pd
import plotly.express as px
import sys
import os

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.ml_model import CampaignPredictor
from model.sentiment import SentimentAnalyzer, AnomalyDetector

# Page Config
st.set_page_config(page_title="AI Marketing Intelligence", layout="wide")

# Load Data & Models
@st.cache_resource
def load_resources():
    data = pd.read_csv('ai_marketing_intelligence/data/campaign_data.csv')
    
    predictor = CampaignPredictor()
    if not predictor.load_model():
        predictor.train()
        predictor.save_model()
        
    sentiment_analyzer = SentimentAnalyzer()
    anomaly_detector = AnomalyDetector()
    
    # Pre-process sentiment
    data = sentiment_analyzer.batch_analyze(data)
    
    return data, predictor, sentiment_analyzer, anomaly_detector

data, predictor, sentiment_analyzer, anomaly_detector = load_resources()

# Sidebar
st.sidebar.title("Campaign Filters")
selected_channel = st.sidebar.multiselect("Select Channel", data['Channel'].unique(), default=data['Channel'].unique())

filtered_data = data[data['Channel'].isin(selected_channel)]

# Main Dashboard
st.title("📊 AI-Driven Marketing Intelligence Dashboard")

# KPI Section
st.header("Key Performance Indicators")
col1, col2, col3, col4 = st.columns(4)

total_spend = filtered_data['Budget'].sum()
total_conversions = filtered_data['Conversions'].sum()
avg_roi = ((filtered_data['Revenue'] - filtered_data['Budget']).sum() / total_spend) * 100
avg_ctr = (filtered_data['Clicks'].sum() / filtered_data['Impressions'].sum()) * 100

col1.metric("Total Spend", f"${total_spend:,.2f}")
col2.metric("Total Conversions", f"{total_conversions:,}")
col3.metric("Average ROI", f"{avg_roi:.2f}%")
col4.metric("Avg CTR", f"{avg_ctr:.2f}%")

# Visualizations
st.markdown("---")
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Campaign Performance (Budget vs Revenue)")
    fig_scatter = px.scatter(
        filtered_data, x="Budget", y="Revenue", 
        color="Channel", size="Conversions", 
        hover_data=['Campaign_ID', 'sentiment'],
        title="Budget vs Revenue w/ Sentiment"
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

with col_chart2:
    st.subheader("Sentiment Distribution")
    sentiment_counts = filtered_data['sentiment'].value_counts()
    fig_pie = px.pie(
        values=sentiment_counts.values, 
        names=sentiment_counts.index,
        title="Customer Sentiment Breakdown",
        color_discrete_map={'Positive':'green', 'Neutral':'grey', 'Negative':'red'}
    )
    st.plotly_chart(fig_pie, use_container_width=True)

# Performance Trend
st.subheader("Performance Trend Over Time")
daily_data = filtered_data.groupby('Date')[['Budget', 'Revenue']].sum().reset_index()
fig_line = px.line(daily_data, x='Date', y=['Budget', 'Revenue'], title="Daily Spend vs Revenue")
st.plotly_chart(fig_line, use_container_width=True)

# ML Prediction Section
st.markdown("---")
st.header("🤖 AI Campaign Predictor")
st.write("Predict the ROI of a future campaign based on planned metrics.")

col_pred1, col_pred2, col_pred3 = st.columns(3)
p_budget = col_pred1.number_input("Planned Budget ($)", min_value=100.0, value=1000.0)
p_impressions = col_pred2.number_input("Est. Impressions", min_value=100, value=5000)
p_clicks = col_pred3.number_input("Est. Clicks", min_value=1, value=200)

if st.button("Predict ROI"):
    predicted_roi = predictor.predict(p_budget, p_impressions, p_clicks)
    st.success(f"Predicted ROI: {predicted_roi * 100:.2f}%")
    
    if predicted_roi > 0.5:
        st.info("Recommendation: High ROI expected! Consider increasing budget.")
    elif predicted_roi < 0:
        st.warning("Recommendation: Negative ROI expected. Optimize targeting or creatives.")

# Anomaly Detection & Recommendations
st.markdown("---")
st.header("⚠️ Anomalies & Insights")
anomalies = anomaly_detector.detect_anomalies(filtered_data)

if not anomalies.empty:
    st.write(f"Detected {len(anomalies)} potential issues in campaigns.")
    st.dataframe(anomalies.head(10))
else:
    st.success("No significant anomalies detected.")

# Recommendations Logic (Simple Rule-based)
st.subheader("📢 System Recommendations")
top_campaigns = filtered_data.sort_values('Revenue', ascending=False).head(5)
st.write("Top Performing Campaigns (Scale these up!):")
for i, row in top_campaigns.iterrows():
    st.markdown(f"- **{row['Campaign_ID']}** ({row['Channel']}): ROAS {row['Revenue']/row['Budget']:.2f}x")

low_campaigns = filtered_data[filtered_data['sentiment'] == 'Negative'].head(5)
if not low_campaigns.empty:
    st.write("Campaigns with Negative Feedback (Action Required):")
    for i, row in low_campaigns.iterrows():
        st.markdown(f"- **{row['Campaign_ID']}**: \"{row['Customer_Feedback']}\"")
