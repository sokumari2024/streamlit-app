import streamlit as st
import yfinance as yf

ticker_symbol="AAPL"
ticker_data=yf.Ticker(ticker_symbol)
ticker_df=ticker_data.history(start="2025-12-01",
                                end="2026-01-01")
st.dataframe(ticker_df) 
