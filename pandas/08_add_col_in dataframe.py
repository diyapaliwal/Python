import pandas as pd

data = {"Name": ["Spongebob","Patrick","Squidward"],
        "Age":[30,35,50]}

df = pd.DataFrame(data) 

# add column to the given DataFrame
df["Job"] = ["Cook", "N/A", "Cashier"]

# Add a new row
new_row = pd.DataFrame([{"Name":"Sandy","Age":28, "Job":"Engineer"}])
df = pd.concat([df, new_row],ignore_index=True)
print(df)
