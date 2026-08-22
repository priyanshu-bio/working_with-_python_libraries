import pandas as pd

data = pd.read_csv('crop_production.csv', index_col='Crop')

cropp = input("enter the crop name:- ").capitalize()

try:
    print(data.loc[cropp].to_string())

except KeyError:
    print(f"{cropp} not found")
