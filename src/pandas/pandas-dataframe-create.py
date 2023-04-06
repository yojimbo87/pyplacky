import pandas as pd

# Create DataFrame (DF) from dictionary
df_dict = pd.DataFrame(
    data={
        "Name": ["John", "Lucy", "Karl"], 
        "Age": [23, 24, 33],
        "State": ["NY", "CA", "FL"]
    }
)

# Create DF from list of objects
class Obj:
    def __init__(self, x, y):
        self.x, self.y = x, y

# make an array of the class objects
objs = [Obj(1, 2), Obj(3, 4), Obj(5, 6)]

# fill dataframe with one row per object, one attribute per column
df_objs = pd.DataFrame([o.__dict__ for o in objs ])

# Print all the things
print(f"DF from dictionary:\n{df_dict}")
print(f"DF from objects:\n{df_objs}")