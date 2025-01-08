import streamlit as st
import yfinance as yf
import plotly.express as pe

st.title("Yahoo Stock Dashboard")
#sidebar layout
st.sidebar.title("Please provide the following")
ticker_symbol = st.sidebar.text_input("Enter Ticker symbol", "AAPL")
start_date = st.sidebar.date_input("Start Date", value=None)
end_date = st.sidebar.date_input("End Date", value=None)

ticker = yf.Ticker(ticker_symbol)
#st.write("Hello")
historical_data = ticker.history(start=start_date, end=end_date)

if start_date is not None and end_date is not None:
    #st.write(historical_data)
    #Display historical data
    st.subheader(f'{ticker_symbol} Stock Overview')
    stockData = yf.download(ticker_symbol, start=start_date, end=end_date)
    price_tab, hist_tab, chart_tab = st.tabs(["Price Summary", "Historical Data", "Charts"])

    with price_tab:
        st.write("Price Summary")
        st.write(stockData)
    with hist_tab:
        st.write("Historical Data")
        st.write(historical_data)
    with chart_tab:
        st.write("Charts")
        line_charts = pe.line(stockData, stockData.index, y=stockData['Close'].iloc[:, 0], title=ticker_symbol)
        st.plotly_chart(line_charts)

