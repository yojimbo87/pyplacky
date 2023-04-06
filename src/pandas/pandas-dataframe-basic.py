import pandas as pd

# DataFrame (DF) instantiation from dictionary
df = pd.DataFrame(
    data={
        "Name": ["John", "Lucy", "Karl"], 
        "Age": [23, 24, 33],
        "State": ["NY", "CA", "FL"]
    }
)

# Reverse rows in DF while preserving index
# https://stackoverflow.com/questions/20444087/right-way-to-reverse-a-pandas-dataframe
df_reversed = df.iloc[::-1]

# Print all the things
print(df_reversed)