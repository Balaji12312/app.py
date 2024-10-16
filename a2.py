import streamlit as st
import yfinance as yf
import pandas as pd

st.title("Stock Market Predictor")

stock_symbol = st.text_input("Enter Stock Symbol", "GOOG")


start_date = st.date_input("Start date", pd.to_datetime("2021-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2022-12-31"))

data = yf.download(stock_symbol, start=start_date, end=end_date)


st.subheader(f"Stock Data for {stock_symbol}")
st.write(data)


st.line_chart(data['Close'])
