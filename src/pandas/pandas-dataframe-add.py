import pandas as pd

# DataFrame (DF) instantiation from dictionary
df = pd.DataFrame(
    data={
        "Name": ["John", "Lucy"], 
        "Age": [23, 24]
    }
)

# Add new column to DF (at the end)
df.loc[:, "State"] = ["NY", "CA"]

# Add new row to DF (at the end) when default index is used
df.loc[len(df)] = { 
    "Name": "Karl", 
    "Age": 33,
    "State": "FL"
}

# Print all the things
print(df)