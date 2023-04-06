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

# Reset DataFrame index and drop original one
df_resetted = df.reset_index(drop=True)

# Print all the things
print("Original DF:")
print(df)
print("Resetted DF:")
print(df_resetted)