# AI-Driven Marketing Intelligence System

An intelligent system that integrates marketing data, analyzes campaign performance using Machine Learning, performs sentiment analysis using NLP, and provides actionable insights through an interactive dashboard.

## Features
- **Unified Data Platform**: Aggregates data from Email, Social Media, Website, and SMS (Synthetic data generated).
- **ML-Based Analysis**: Random Forest Regressor to predict ROI and performance.
- **NLP Sentiment Analysis**: TextBlob integration to analyze customer feedback.
- **Interactive Dashboard**: Streamlit-based UI with Plotly visualizations.
- **Anomaly Detection**: Flags low-performing campaigns and budget leakage.
- **Smart Recommendations**: Suggests budget adjustments based on predicted ROI.

## Project Structure
```
ai_marketing_intelligence/
├── data/               # Contains campaign_data.csv
├── model/              # ML and NLP models
│   ├── ml_model.py     # Random Forest implementation
│   └── sentiment.py    # TextBlob sentiment analysis
├── dashboard/          # UI Logic
│   └── app.py          # Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

## Setup & Installation

1. **Clone the repository** (or unzip the project folder).
2. **Install dependencies**:
   ```bash
   pip install -r ai_marketing_intelligence/requirements.txt
   ```
3. **Generate Data (Optional)**:
   The project comes with a data generator. If you want fresh data:
   ```bash
   python data_generator.py
   ```
4. **Train Model**:
   Models are trained automatically on first run, but you can force training:
   ```bash
   python ai_marketing_intelligence/model/ml_model.py
   ```

## Running the Dashboard

Run the Streamlit app:
```bash
streamlit run ai_marketing_intelligence/dashboard/app.py
```

## Technologies Used
- **Python**: Core logic
- **Pandas/NumPy**: Data manipulation
- **Scikit-Learn**: Machine Learning (Random Forest)
- **TextBlob**: Natural Language Processing
- **Streamlit**: Web Dashboard
- **Plotly**: Interactive Visualizations
