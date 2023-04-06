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
names = df.loc[:, "Name"]

# Get second row with all column values
second_row_full = df.loc["L24CA"]

# Get second row, "Name" column value
second_name = df.loc["L24CA", "Name"]

# Get second and third row only with "Name" and "Age" columns as DF
df2 = df.loc[["L24CA", "K22FL"], ["Name", "Age"]]

# Get rows with "Name" and "Age" column where "Age" is between 20 and 30 as DF
df3 = df.loc[(df["Age"] >= 20) & (df["Age"] <= 30), ["Name", "Age"]]

# Print all the things
print(f"Names:\n{names}")
print(f"Second row full:\n{second_row_full}")
print(f"Second name: {second_name}")
print(f"df2:\n{df2}")
print(f"df3:\n{df3}")