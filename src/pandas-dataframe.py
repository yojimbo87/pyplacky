import pandas as pd

# DataFrame instantiation from dictionary
df = pd.DataFrame(
    data={
        "Column 1": ["Col 1 row 1", "Col 1 row 2"], 
        "Column 2": ["Col 2 row 1", "Col 2 row 2"]
    }
)

# Add new column to DataFrame with constant value
df.loc["Column 3", :] = "Col 3 value"

# Reset DataFrame index
df.reset_index(inplace=True)

# Get DataFrame size (number of rows)
df_row_count = len(df.index)

# Reverse rows in DataFrame
df_reversed = df.iloc[::-1]

# Print all the things
print(df)
print(f"df row count: {df_row_count}")
print(df_reversed)