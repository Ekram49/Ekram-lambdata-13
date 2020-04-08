import pandas as pd


from my_lambdata.my_mod import enlarge
print("HELLO WORLD!")

df = pd.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())


print(enlarge(9))