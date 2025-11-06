# Quick Start Guide - Stock Prediction Project

This guide will help you get the Stock Prediction project up and running.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Installation

### 1. Clone the repository (if not already done)

```bash
git clone https://github.com/ajaygm18/Stock-Predictionl.git
cd Stock-Predictionl
```

### 2. Install dependencies

#### Option A: Install all dependencies (recommended for full functionality)

```bash
pip install -r requirements.txt
```

**Note:** This may take 10-15 minutes as it includes deep learning libraries (TensorFlow, PyTorch, etc.)

#### Option B: Install minimal dependencies (for basic functionality)

```bash
pip install jupyter nbconvert ipykernel numpy pandas matplotlib yfinance mplfinance seaborn
```

This takes 1-2 minutes and is sufficient for running the basic Technical Analysis notebooks.

### 3. Additional Setup for NLP Features (Optional)

If you plan to use the Sentiment Analysis notebooks:

```bash
# Download NLTK data
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt'); nltk.download('stopwords')"

# Download spaCy language model
python -m spacy download en_core_web_sm
```

## Running the Project

### Option 1: Test Scripts (Quick Verification)

Run the test script to verify the setup:

```bash
python3 run_notebook.py
```

Run the demonstration script to see actual execution:

```bash
python3 demo_execution.py
```

This will:
- Download real stock data
- Perform time series analysis
- Create visualizations
- Verify all core libraries work

### Option 2: Jupyter Notebooks (Full Analysis)

1. Start Jupyter:

```bash
jupyter notebook
```

2. Navigate to one of the three main directories:
   - **Technical_Analysis/** - Chart patterns and technical indicators
   - **Time_Series/** - ARIMA, LSTM, and other forecasting models
   - **Sentiment_Analysis/** - NLP and sentiment analysis

3. Open any notebook and run the cells

### Recommended Starting Points

For beginners, start with these notebooks in order:

1. **Technical_Analysis/FTSE100_data_collection_and_EDA.ipynb**
   - Basic data collection and exploration
   - No complex dependencies

2. **Time_Series/ARIMA.ipynb**
   - Time series analysis fundamentals
   - Requires: statsmodels

3. **Sentiment_Analysis/Stock_news_data_collection.ipynb**
   - Web scraping and sentiment analysis
   - Requires: beautifulsoup4, selenium, nltk

## Project Structure

```
Stock-Predictionl/
├── Technical_Analysis/          # Technical indicators and chart patterns
│   ├── FTSE100_data_collection_and_EDA.ipynb
│   ├── Chart_patterns_and_technical_indicators.ipynb
│   ├── Trading_Dashboards.ipynb
│   └── Hypothesis_Testing.ipynb
│
├── Time_Series/                 # Time series forecasting models
│   ├── ARIMA.ipynb
│   ├── SARIMA.ipynb
│   ├── LSTM.ipynb
│   ├── RNN_LSTM_GRU.ipynb
│   ├── Facebook_Prophet.ipynb
│   ├── Regression_Models.ipynb
│   └── Classifier_Models.ipynb
│
├── Sentiment_Analysis/          # NLP and sentiment analysis
│   ├── Stock_news_data_collection.ipynb
│   ├── Sentiment_Analysis_and_Classifiers.ipynb
│   ├── NLP_Text_Preprocessing_and_Classification.ipynb
│   └── BERT_Long_Text_Classification.ipynb
│
├── requirements.txt             # Python dependencies
├── run_notebook.py             # Test script
├── demo_execution.py           # Demonstration script
└── README.md                   # Project overview
```

## Troubleshooting

### Issue: "Module not found" error

**Solution:** Install the missing module:
```bash
pip install <module-name>
```

### Issue: Jupyter not starting

**Solution:** Ensure Jupyter is installed:
```bash
pip install jupyter
```

### Issue: Stock data download fails

**Solution:** This usually means:
- No internet connection
- Yahoo Finance API is temporarily down
- The stock symbol is invalid

Try using a different stock symbol like "AAPL" or "MSFT" instead of FTSE stocks.

### Issue: Out of memory when running deep learning notebooks

**Solution:** 
- Close other applications
- Reduce the batch size in the notebook
- Use smaller datasets for testing

## Data Sources

- **Historical Stock Data:** Yahoo Finance (via yfinance API)
- **News Articles:** Investing.com (via web scraping)

## Key Technologies

- **Data Processing:** NumPy, Pandas
- **Visualization:** Matplotlib, Seaborn, Plotly
- **Machine Learning:** Scikit-learn
- **Deep Learning:** TensorFlow, Keras, PyTorch
- **Time Series:** Statsmodels, Prophet
- **NLP:** NLTK, TextBlob, spaCy, Transformers

## Performance Expectations

- **Data Collection:** 5-30 seconds per stock (depending on time range)
- **Model Training:** 
  - Simple models (ARIMA): 1-5 minutes
  - LSTM/RNN: 5-30 minutes
  - BERT: 30-60 minutes (requires GPU for reasonable speed)

## Notes

- Some notebooks may take significant time to run (especially deep learning models)
- GPU is recommended but not required for deep learning notebooks
- Internet connection is required for downloading stock data
- Some features (web scraping) may require ChromeDriver for Selenium

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review the README.md for project details
3. Open an issue on the GitHub repository

## License

See the repository for license information.
