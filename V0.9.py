import pandas as pd

try:
    df = pd.read_csv("account-2.csv")
except:
    print("File not recognize as a valid file. Please be sure to upload a DeGiro .csv file. Re-run "
          "the program to try again.")
    exit()

my_cols = set(df.columns)

# Rename columns
df = df.copy()
df.rename(columns={"Mutatie": "Valuta", "Unnamed: 8": "Bedrag"}, inplace=True)

# Remove irrelevant columns
df.drop(df.columns[[1, 2, 6, 9, 10, 11]], axis=1, inplace=True)

# Filter dataframe to only show rows that contain "Dividend"
df2 = df.loc[df["Omschrijving"] == "Dividend"]

# Count total dividend
count_dividend = sum(df2["Bedrag"])

# Count dividend per currency
div_currency_EUR = df2.loc[df2["Valuta"] == "EUR", "Bedrag"].sum()
div_currency_USD = df2.loc[df2["Valuta"] == "USD", "Bedrag"].sum()

# Dividend per stock
div_per_stock = df2.groupby(["Product", "Valuta"])[["Bedrag"]].sum()

print(f"Your total dividend is: €/$ {count_dividend:.2f}.")
print(f"Your total dividend in Euro's is € {div_currency_EUR:.2f}.")
print(f"Your total dividend in US Dollars $ is {div_currency_USD:.2f}.\n")
print(div_per_stock)