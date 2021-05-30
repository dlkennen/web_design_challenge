import pandas as pd
import os


file_one = os.path.join('..', 'Resources', 'cities.csv')

file_one_df = pd.read_csv(file_one, encoding="ISO-8859-1")

file_one_df.to_html()

