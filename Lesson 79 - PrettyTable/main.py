from prettytable import *
import pandas as pd
import numpy as np

table = PrettyTable()
df = pd.read_csv("data.csv")
# print(df)

header = list(df.columns)
data = list(map(list,np.array(df)))

table.field_names = header
# for row in data:
#     table.add_row(row)
table.add_rows(data)
# with open("data.csv") as file:
#     table = from_csv(file)


# print(table.get_string(fields=["City name","Area"],start=1,end=4))
# table.align = "l"
# table.align["City name"] = "c"

table.sortby = "City name"
table.sortby = "Annual Rainfall"
table.reversesort = True

# print(table.get_html_string(attributes={"id":"my_table","class":"red"}))
table.set_style(SINGLE_BORDER)
print(table)