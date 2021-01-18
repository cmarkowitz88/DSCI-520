# A1:Function(3/3)
# get_shape_and_column('./data/demographics.csv'):data,shape,column

import pandas as pd


def get_shape_and_columns(csv_path):

    df = ''
    shape = ''
    columns = ''

    try:
        df = pd.read_csv(csv_path)
        shape = df.shape
        columns = df.columns
    except FileNotFoundError:
        print("File Not Found, Aborting")

    return df, shape, columns


d, s, c = get_shape_and_columns("./data/demographics.csv")

print(d, s, c)
