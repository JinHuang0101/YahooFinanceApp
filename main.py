import streamlit as st
import yfinance as fn
import datetime as dt

st.write(""" # Yahoo Finance App with *Streamlit*""")

st.title("Stock Market Info")

# st.header("Data Science Web App")
st.sidebar.header("Jin Huang \n Finance Web App ...")

# get ticker input from user
ticker_list = ['Select a stock']

ticker_input = st.text_input(
    "Enter tickers seperated by comma. No space.", "e.g., AMZN,TSLA,AAPL")
individual_ticker = ticker_input.split(",")

if individual_ticker[0] != 'e.g.':
    for ind in individual_ticker:
        ticker_list.append(ind)

ticker = st.selectbox('Select a stock', ticker_list)

if ticker != "Select a stock":
    # Markdown and confirmation
    html_str = f"""
    <style>
    p.a {{
    font: bold 30px Courier;
    }}
    </style>
    <p class="a">{ticker}</p>
    """
    st.markdown(html_str, unsafe_allow_html=True)
    stock = fn.Ticker(ticker)

    # output current market price of the ticker:
    st.write("Regular Market Previous Close: ",
             stock.info["regularMarketPreviousClose"])
    st.write("Regular Market Open: ", stock.info["regularMarketOpen"])
    st.write("Regular Market Day Low: ", stock.info["regularMarketDayLow"])
    st.write("Regular Market Day Hight: ", stock.info["regularMarketDayHigh"])
    st.write("Regular Market Volume: ", stock.info["regularMarketVolume"])

    # select different info sections
    category_list = ["Select a category ", "Company Business Summary", "Key Financial Metrics", "Full Company Info",
                     "Historical Data", "Historical Data Chart"]
    category = st.selectbox("Select a category ", category_list)

    if category == "Company Business Summary":
        st.write("Country: ", stock.info["country"])
        st.write("Industry: ", stock.info["industryKey"])
        st.write("Sector: ", stock.info["sectorKey"])
        st.write("Business summary: ", stock.info["longBusinessSummary"])

    elif category == "Key Financial Metrics":
        st.write("Trailing earnings per share: ", stock.info["trailingEps"])
        st.write("Forward earnings per share: ", stock.info["forwardEps"])
        st.write("Price-to-Book Ratio: ", stock.info["priceToBook"])
        st.write("Debt-to-Equity Ratio: ", stock.info["debtToEquity"])
        st.write("Free Cash Flow: ", stock.info["freeCashflow"])
        st.write("PEG Ratio: ", stock.info["pegRatio"])
        st.write("Return-on-Equity Ratio: ", stock.info["returnOnEquity"])
        st.write("Operating margin: ", stock.info["operatingMargins"])

    elif category == "Full Company Info":
        # output company info
        st.write(stock.info)
        print(stock.info)

    elif category == "Historical Data":
        # ask user input for start date and end date
        start = st.date_input("Specify a start date ")
        end = st.date_input("Specify an end date ")

        # fetch dataframe within the range
        finance_data = fn.download(
            ticker, start, end)

        st.write(finance_data)

    elif category == "Historical Data Chart":

        # fecth historical data by valid periods
        hist_data = stock.history(period="6mo")

        # History Chart
        st.line_chart(hist_data)
