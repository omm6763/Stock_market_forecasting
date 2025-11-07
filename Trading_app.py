import streamlit as st

st.set_page_config(
    page_title="Trading App",
    page_icon="heavy_dollar_sign:",
    layout="wide")

st.title("Trading Guide App:bar_chart:")

st.header("We provide the Greatest Platform for you to collect all information prior to investing in stocks.")

st.image("app.webp")

st.markdown("## We provide the following services:")

st.markdown("#### :one:Stock Information")
st.write("Through this page you can see all the information about stock.")

st.markdown("#### :two:Stock Prediction")
st.write("Through this page you can see the predicted stock price for the next 30 days based on historical data and advanced forecasting models.")

st.markdown("#### :three:CAPM Return ")
st.write("Through this page you can calculate the expected return of a stock based on the Capital Asset Pricing Model (CAPM).")

st.markdown("#### :four:CAPM Beta")
st.write("Calculate beta And Expected return for individual stocks.")