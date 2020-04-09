import pandas
def convert_names_bd(my_df):
    """
    Creates a new column called "city_name" which has the corresponding city name.
​
    Params my_df (pandas.DataFrame) with with column called "abbrev" which has state abbrevs
​
    See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    """
    df = my_df.copy()
    names_map = {
        "DHK": "Dhaka",
        "CTG": "Chittagong",
        "KHU": "Khulna",
        "RAJ": "Rajshahi",
        "SYL": "Sylhet",
        "BAR": "Barisal"
    }
    print(type(df["abbrev"])) #> <class 'pandas.core.series.Series'>
    df["City_name"] = df["abbrev"].map(names_map)
    return df
if __name__ == "__main__":
    df = pandas.DataFrame({"abbrev": ["DHK", "CTG", "KHU", "RAJ"]})
    full_df = convert_names_bd(df)
    print(full_df.head())
    df2 = pandas.DataFrame({"abbrev": ["SYL", "BAR", "RON", "CU"]})
    full_df2 = convert_names_bd(df2)
    print(full_df2.head())