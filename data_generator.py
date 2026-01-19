import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import os

# Create directories if they don't exist
os.makedirs('ai_marketing_intelligence/data', exist_ok=True)

def generate_sentence():
    sentiments = [
        "Great campaign, loved the visuals!",
        "The ad was okay but a bit repetitive.",
        "Not interested, irrelevant content.",
        "Amazing offer! bought it immediately.",
        "Worst experience, link didn't work.",
        "Decent, but could be better.",
        "Highly recommended!",
        "Spammy ad, hidden it.",
        "Love this brand!",
        "Too expensive for me."
    ]
    return random.choice(sentiments)

def generate_data(num_samples=1000):
    channels = ['Email', 'Social Media', 'Website', 'SMS']
    data = []
    
    start_date = datetime.now() - timedelta(days=365)
    
    for i in range(num_samples):
        date = start_date + timedelta(days=random.randint(0, 365))
        campaign_id = f"CMP_{random.randint(1000, 9999)}"
        channel = random.choice(channels)
        budget = round(random.uniform(500, 50000), 2)
        
        # Correlate metrics slightly with budget
        impressions = int(budget * random.uniform(10, 50))
        clicks = int(impressions * random.uniform(0.01, 0.10))
        conversions = int(clicks * random.uniform(0.05, 0.20))
        
        # roi = (revenue - budget) / budget * 100
        # Assume average sale value around $50-$200
        avg_sale = random.uniform(20, 100)
        revenue = conversions * avg_sale
        
        feedback = generate_sentence()
        
        data.append([
            campaign_id, channel, date.strftime('%Y-%m-%d'), budget, 
            impressions, clicks, conversions, revenue, feedback
        ])
        
    df = pd.DataFrame(data, columns=[
        'Campaign_ID', 'Channel', 'Date', 'Budget', 
        'Impressions', 'Clicks', 'Conversions', 'Revenue', 'Customer_Feedback'
    ])
    
    # Save to CSV
    df.to_csv('ai_marketing_intelligence/data/campaign_data.csv', index=False)
    print("Data generated successfully at ai_marketing_intelligence/data/campaign_data.csv")

if __name__ == "__main__":
    generate_data()
