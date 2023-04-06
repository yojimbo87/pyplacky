import pandas as pd

# DataFrame (DF) instantiation from dictionary
df = pd.DataFrame(
    data={
        "Name": ["John", "Lucy", "Karl"], 
        "Age": [23, 24, 33],
        "State": ["NY", "CA", "FL"]
    }
)

# Get DF row count
# https://stackoverflow.com/questions/15943769/how-do-i-get-the-row-count-of-a-pandas-dataframe
# - Using len() should be fastest
df_row_count = len(df.index)

# Get DF column count
df_column_count = len(df.columns)

# Print all the things
print(f"DF row count: {df_row_count}")
print(f"DF column count: {df_column_count}")