import pandas as pd

data = {"Name": ["Spongebob","Patrick","Squidward"],
        "Age":[30,35,50]}

df = pd.DataFrame(data) 

# add column to the given DataFrame
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new row
new_row = pd.DataFrame([{"Name":"Sandy","Age":28, "Job":"Engineer"},{"Name":"diya","Age":"21","Job":"Data Analyst"}])
df = pd.concat([df, new_row],ignore_index=True)
# Ignore Index is used so that new index is created and the concated row will get numbering from start not as (0)
print(df)

df["Age"] = df["Age"].astype(int)
young = df[df["Age"]<30]
print(young)