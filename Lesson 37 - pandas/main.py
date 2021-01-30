import pandas as pd
import numpy as np

df = pd.read_csv("sample.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.sample(n=10))

df["Height (inches)"] *= 0.0254
df = df.rename(columns={"Height (inches)":"Height","Weight (lbs)":"Weight"})
df["Height"] = df["Height"].round(decimals=2)
df["Weight"] *= 0.4539237
df["Weight"] = df["Weight"].apply(np.round).astype("Int32")
df["Age"] = df["Age"].apply(np.round).astype("Int32")
# print(df)
# print(df.corr())
df["First Name"] = df["Name"].apply(lambda x: x.split()[0])
df["Last Name"] = df["Name"].apply(lambda x: x.split()[-1])
del df["Name"]
df.sort_values(by=["Team","Position","Last Name","First Name"])

# df.to_excel("Players.xlsx",index=False)
teams = df["Team"].unique()
with pd.ExcelWriter("Players.xlsx") as writer:
    settings = []
    for column in df.columns:
        settings.append({"header":column})
    for team in teams:
        team_df = df.loc[np.where(df["Team"] == team)]
        team_df.to_excel(writer,sheet_name=team, index=False)

        worksheet = writer.sheets[team]
        rows, cols = team_df.shape
        worksheet.add_table(0,0,rows,cols-1,{"columns":settings})
        worksheet.set_column(0,cols-1,12)