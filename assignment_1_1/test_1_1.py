import pandas 
from assignment_1_1.function_1_1 import convert_names
df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
full_df = convert_names(df)
print(full_df.head())