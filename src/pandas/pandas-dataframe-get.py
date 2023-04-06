import pandas as pd

# DataFrame (DF) instantiation from dictionary
df = pd.DataFrame(
    data={
        "Name": ["John", "Lucy", "Karl"], 
        "Age": [23, 24, 33],
        "State": ["NY", "CA", "FL"]
    },
    index=["J23NY", "L24CA", "K22FL"]
)

# Get "Name" column values
names = df["Name"]

names2 = df.Name

# Print all the things
print(f"Names:\n{names}")
print(f"Names2:\n{names2}")