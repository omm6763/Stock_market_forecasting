# 📈 Stock Market Forecasting & Analysis App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://stockmarketforecasting-i3pdjqrc5krpsrpticefzx.streamlit.app/)

A comprehensive web application for analyzing historical stock data and forecasting future prices using advanced time-series models. Built with Python and Streamlit.

**🔴 Live Demo:** [Click here to view the app](https://stockmarketforecasting-i3pdjqrc5krpsrpticefzx.streamlit.app/)

## 🚀 Features

### 1. **Stock Analysis**
   - **Real-time Data:** Fetches live stock data using `yfinance`.
   - **Interactive Charts:** Visualize price movements with Candlestick and Line charts using Plotly.
   - **Technical Indicators:**
     - **RSI** (Relative Strength Index)
     - **MACD** (Moving Average Convergence Divergence)
     - **SMA** (50-day Simple Moving Average)
   - **Fundamental Info:** Displays key metrics like Market Cap, Beta, EPS, P/E Ratio, and more.
   - **Timeframes:** Filter data by 5D, 1M, 6M, YTD, 1Y, 5Y, and MAX.

### 2. **Stock Prediction**
   - **Forecast:** Predicts stock closing prices for the next **30 days**.
   - **Machine Learning Model:** Uses the **ARIMA** (AutoRegressive Integrated Moving Average) model for time-series forecasting.
   - **Performance:** Displays the Root Mean Squared Error (RMSE) to evaluate model accuracy.
   - **Visuals:** Shows the forecasted trend line alongside historical data.

### 3. **Financial Insights** (Home Page)
   - Provides a centralized dashboard for accessing stock information, predictions, and CAPM analysis tools.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Data Source:** [yfinance](https://pypi.org/project/yfinance/)
* **Visualization:** [Plotly](https://plotly.com/python/)
* **Machine Learning:** [Statsmodels](https://www.statsmodels.org/) (ARIMA), Scikit-learn
* **Data Processing:** Pandas, NumPy

---

## 📦 How to Run Locally

If you want to run this app on your own machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/stock_market_forecasting.git](https://github.com/your-username/stock_market_forecasting.git)
    cd stock_market_forecasting
    ```

2.  **Create a virtual environment (Optional but recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the app:**
    ```bash
    streamlit run Trading_app.py
    ```

---

## 📂 Project Structure

```text
├── Trading_app.py          # Main entry point (Home Page)
├── requirements.txt        # Python dependencies
├── pages/
│   ├── Stock_analysis.py   # Analysis dashboard code
│   ├── Stock_prediction.py # Prediction model interface
│   └── utils/
│       ├── model_train.py  # ARIMA model training & forecasting logic
│       └── plotly_figure.py# Custom Plotly chart functions
└── assets/                 # Images and resources
