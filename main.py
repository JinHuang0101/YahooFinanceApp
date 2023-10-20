import streamlit as st
import yfinance as fn

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

    # select different info sections
    category_list = ["Select a category ", "Company Business Summary", "Key Financial Metrics", "Full Company Info",
                     "Current Data", "Historical Data Chart"]
    category = st.selectbox("Select a category ", category_list)
    stock = fn.Ticker(ticker)

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

    elif category == "Current Data":
        # fetch data from dataframe
        finance_data = fn.download(
            ticker, start="2023-01-01", end="2023-09-01")

        # Dataframe
        st.write(finance_data)

    elif category == "Historical Data Chart":

        # fecth historical data by valid periods
        hist_data = stock.history(period="6mo")

        # History Chart
        st.line_chart(hist_data)
