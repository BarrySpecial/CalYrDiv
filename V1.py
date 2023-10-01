import streamlit as st
import pandas as pd

# Streamlit title, welcome and file uploader
st.title("DeGiro dividend calculator")
st.markdown("Hello! This is a web-app that calculates the amount of dividend that you've "
            "received from your DeGiro stock portfolio.")
with st.expander("Instructions"):
    st.markdown("Log in with your DeGiro account, go to 'inbox' and select 'account statement'. Select the "
                "start and end date. Then export as .csv file. Use the file selector below to select or drag and drop "
                "the file from your downloads folder. ")
st.markdown("")

uploaded_file = st.file_uploader("Select your account.csv file", type=".csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Rename columns
    df = df.copy()
    df.rename(columns={"Mutatie": "Valuta", "Unnamed: 8": "Bedrag"}, inplace=True)

    # Remove irrelevant columns
    try:
        df.drop(df.columns[[1, 2, 6, 9, 10, 11]], axis=1, inplace=True)
    except:
        st.markdown("## Error")
        st.write("The file you uploaded is a not a DeGiro file. Please select the right file and try again. Refer "
                 "to the instructions for more information.")
        st.stop()

    # Filter dataframe to only show rows that contain "Dividend"
    df2 = df.loc[df["Omschrijving"] == "Dividend"]

    # Count total dividend
    count_dividend = sum(df2["Bedrag"])

    # Count dividend per currency
    div_currency_EUR = df2.loc[df2["Valuta"] == "EUR", "Bedrag"].sum()
    div_currency_USD = df2.loc[df2["Valuta"] == "USD", "Bedrag"].sum()

    # Dividend per stock
    div_per_stock = df2.groupby(["Product", "Valuta"])[["Bedrag"]].sum()

    # Streamlit write results
    st.markdown("## Dividend")
    st.markdown(f"Your dividend in Euro's is € {div_currency_EUR:.2f}")
    st.markdown(f"Your dividend in US Dollars is $ {div_currency_USD:.2f}")
    st.markdown("### Total dividend per stock")
    st.write(div_per_stock)
