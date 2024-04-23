import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import yfinance as yf

from datetime import datetime

st.title("My financial dashboard")
st.write("This dashboard is made to display some aggregated stats")

def plot_my_df(values):
    fig, ax = plt.subplots()
    plt.xticks(rotation=90)
    ax.plot(values, color="green", label="Open")
    ax.legend()
    st.pyplot(fig)

def plot_my_stats(values):
  st.write("Summary of the stock")
  st.write(values.agg(["min","max","mean"]))
  if st.button("Plot the stats"):
      st.write("Plot the Open Price")
      plot_my_df(values['Open'])
  else:
      st.write("Not yet plotted")

start_time = st.slider("When to start",
                       min_value=datetime(2020, 1, 1, 9, 30),
                       max_value=datetime(2022, 1, 1, 9, 30),
                       format="MM/DD/YYYY")

stock_name = st.selectbox("Stock-Name", ["GOOGL","AAPL","TSLA","AMD"])
st.write(f"You have selected {stock_name}")

# Download Google stock data
df = yf.download(stock_name, start=start_time, end='2024-01-01')

plot_my_stats(df)

