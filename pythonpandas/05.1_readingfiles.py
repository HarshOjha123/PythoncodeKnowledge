# If your data sets are stored in a file, Pandas can load them into a DataFrame.
import pandas as pd

# If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows

df = pd.read_csv('data.csv')

print(df) 
# Tip: use to_string() to print the entire DataFrame.
print(df.to_string())

# You can check your system's maximum rows with the pd.options.display.max_rows statement.

'''JSON = Python Dictionary

JSON objects have the same format as Python dictionaries.'''
'''js={"player_of_team_a":{
    0:"rahul",
    1:"raj",
    2:"ram"
},"player of team b":{
    0:"lakshya",
    1:"rajat",
    2:"op"
}}'''
# js=pd.read_json("filename")

# json=to_json("")