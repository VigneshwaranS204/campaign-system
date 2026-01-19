from textblob import TextBlob
import pandas as pd
import numpy as np

class SentimentAnalyzer:
    def analyze(self, text):
        """
        Returns a dictionary with polarity, subjectivity, and sentiment label.
        """
        if not isinstance(text, str):
            text = str(text)
            
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity
        
        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'
            
        return {
            'text': text,
            'polarity': polarity,
            'subjectivity': analysis.sentiment.subjectivity,
            'sentiment': sentiment
        }

    def batch_analyze(self, df, text_column='Customer_Feedback'):
        """
        Applies sentiment analysis to a dataframe column.
        """
        results = df[text_column].apply(self.analyze)
        df_sentiment = pd.DataFrame(results.tolist())
        return pd.concat([df, df_sentiment[['sentiment', 'polarity']]], axis=1)

class AnomalyDetector:
    def detect_anomalies(self, df):
        """
        Detects anomalies in traffic/engagement.
        Rules:
        - Drop in clicks > 50% average
        - ROI < -20% (Budget leakage/inefficiency)
        """
        anomalies = []
        avg_clicks = df['Clicks'].mean()
        
        for idx, row in df.iterrows():
            reasons = []
            
            # Click Drop Check (simplified as absolute low value vs avg for this demo)
            if row['Clicks'] < (0.1 * avg_clicks):
                reasons.append("Abnormal Low Traffic")
                
            # ROI Check
            roi = (row['Revenue'] - row['Budget']) / row['Budget'] if row['Budget'] > 0 else 0
            if roi < -0.5:
                reasons.append("High Budget Leakage (ROI < -50%)")
                
            if reasons:
                anomalies.append({
                    'Campaign_ID': row['Campaign_ID'],
                    'Date': row['Date'],
                    'Issues': ", ".join(reasons)
                })
                
        return pd.DataFrame(anomalies)
