import pandas 
from assignment_1_2.function_1_2 import convert_names_bd
df = pandas.DataFrame({"abbrev": ["DHK", "BAR", "CTG", "SYL"]})
full_df = convert_names_bd(df)
print(full_df.head())