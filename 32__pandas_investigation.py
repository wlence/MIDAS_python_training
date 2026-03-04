import pandas as pd

# Pandas creates a DataFrame from a dictionary of lists, where each key is a column name and the corresponding list contains the column values.
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

# Accessing columns
print("\nNames:")
print(df["Name"])
# Accessing rows using loc (label-based) and iloc (integer-based)
print("\nFirst Row (loc):")
print(df.loc[0])
print("\nFirst Row (iloc):")
print(df.iloc[0])

# Read json data into a DataFrame
sales_records = pd.read_json("https://api.acodingtutor.com/sales_records")

print(sales_records.head())

# Create a pivot table to summarize total quantity sold for each product and colour combination
sales_pt = pd.pivot_table(sales_records, index="Product", columns="Colour", values="Quantity", aggfunc="sum")
sales_pt.fillna(0, inplace=True)

sales_pt["Total"] = sales_pt.sum(axis=1)

print(sales_pt)

totals_row = sales_pt.sum(axis=0).to_frame().T
totals_row.index = ["Total"]

print(totals_row)

totals_pt = pd.concat([sales_pt, totals_row])
print(totals_pt)


