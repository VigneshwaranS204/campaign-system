import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import pickle
import os

class CampaignPredictor:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.features = ['Budget', 'Impressions', 'Clicks']
        self.target = 'ROI'

    def preprocess_data(self, df):
        """
        Cleans data, calculates ROI, and prepares features/target.
        """
        # Calculate ROI if not present (although synthetic data has Revenue)
        # ROI = (Revenue - Budget) / Budget
        df['ROI'] = (df['Revenue'] - df['Budget']) / df['Budget']
        
        # Handle outliers/missing values if any (simple fill for now)
        df.fillna(0, inplace=True)
        
        return df

    def train(self, data_path='ai_marketing_intelligence/data/campaign_data.csv'):
        df = pd.read_csv(data_path)
        df = self.preprocess_data(df)
        
        X = df[self.features]
        y = df[self.target]
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        self.model.fit(X_train, y_train)
        
        predictions = self.model.predict(X_test)
        mae = mean_absolute_error(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        print(f"Model Trained. MAE: {mae}, R2: {r2}")
        return mae, r2

    def predict(self, budget, impressions, clicks):
        input_data = pd.DataFrame([[budget, impressions, clicks]], columns=self.features)
        prediction = self.model.predict(input_data)
        return prediction[0]

    def save_model(self, path='ai_marketing_intelligence/model/rf_model.pkl'):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'wb') as f:
            pickle.dump(self.model, f)

    def load_model(self, path='ai_marketing_intelligence/model/rf_model.pkl'):
        if os.path.exists(path):
            with open(path, 'rb') as f:
                self.model = pickle.load(f)
            return True
        return False

# Self-training on import if wanted, or explicitly called.
if __name__ == "__main__":
    predictor = CampaignPredictor()
    predictor.train()
    predictor.save_model()
