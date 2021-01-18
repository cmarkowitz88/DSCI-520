import pandas as pd
import numpy as np


# A3:Function(3/5)
# total_columns('./data/demographics.csv', "Male", "Female")

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


def total_columns(in_data, column1, column2):
    in_data['total'] = in_data[column1] + in_data[column2]

    return in_data


# A5:Function(4/5)
def total_columns_2(data, list_of_columns, total_name="total"):
    tmp = 0
    for col in list_of_columns:
        tmp += data[col]
    data[total_name] = tmp

    return data


# A4:Function(4/5)

def get_min_max_locations(data):
    df_max = data.nlargest(1, ['total'])
    max_location = df_max['Location'].values[0]
    max_total = df_max['total'].values[0]

    df_max_2 = data.sort_values('total', ascending=False)
    max_location = df_max_2.head(1)['Location'].values[0]
    max_total = df_max_2.head(1)['total'].values[0]

    df_min = data.nsmallest(1, ['total'])
    min_location = df_min['Location'].values[0]
    min_total = df_min['total'].values[0]

    df_min2 = data.sort_values('total', ascending=True)
    min_location = df_min2.head()['Location'].values[0]
    min_total = df_min2.head()['total'].values[0]

    # ---Your code ends here---

    return min_location, min_total, max_location, max_total


# A6:Function(2/2)

def are_columns_equal(data, column1, column2):
    comparison = np.where(data[column1] == data[column2], True, False)
    are_equal = (np.all(comparison))

    return are_equal


# A7:Function(2/3)

def get_location_difference_dict(data, column1, column2):
    data['diff'] = data[column1] - data[column2]
    df_diff = data[data['diff'] != 0]
    new = df_diff[['Location', 'diff']]
    location_diff_dict = new.set_index('Location')['diff'].to_dict()

    return location_diff_dict


def compute_cosine_similarity(data, similarity_columns):

    similarity_list = []
    tmp_df = pd.DataFrame()

    # np_ary = data.to_numpy()

    for col in similarity_columns:
        tmp_df[col] = data[col]

    tmp_df = tmp_df.fillna(0)

    for i, j in tmp_df.iterrows():
        # print(i)
        # print(j)
        loc1 = data.iloc[i]['Location']
        for x, y in tmp_df.iterrows():
            loc2 = data.iloc[x]['Location']
            sim = j.dot(y) / (np.linalg.norm(j) * np.linalg.norm(y))
            # print(sim)
            tmp_tupl = loc1, loc2, sim
            similarity_list.append(tmp_tupl)

    return similarity_list


# A9:Function(3/3)

def getKey(item):
    return item[2]

def get_min_max_similarity(similarity_list):

    min_sorted_tuple = sorted(similarity_list, key=getKey)
    min_similarity = min_sorted_tuple[0]

    max_sorted_tuple = sorted(similarity_list, key=getKey, reverse=True)
    max_similarity = max_sorted_tuple[0]

    return min_similarity, max_similarity


# --------- Start Main Program Below -----------#
data, shape, columns = get_shape_and_columns('./data/demographics.csv')
print(data)
print(shape)
print(columns)

d1 = total_columns(data, "Male", "Female")
print(d1[['total']].describe())
print(d1[['Location', 'total']])

out_min_location = get_min_max_locations(d1)
print(out_min_location)

d2 = total_columns_2(data, ["Male", "Female"], 'Sum')
print(d2[['Sum']].describe())
print(get_min_max_locations(d2))

adult_age_group_columns = ['Age_19_25', 'Age_26_34', 'Age_35_54', 'Age_55_64']
data = total_columns_2(data, adult_age_group_columns, "total_adult_age_groups")

# Create a total column for adults with and without children.
adults_columns = ['Adults_with_Children', 'Adults_with_No_Children']
data = total_columns_2(data, adults_columns, "total_adults")

# Compute the difference between these values
data['diff'] = data['total_adult_age_groups'] - data['total_adults']

# Look at the differences for Pennsylvania, Colorado, and Georgia
print("Pennsylvania difference: {}".format(data[data['Location'] == "Pennsylvania"]['diff'].values))
print("Colorado difference: {}".format(data[data['Location'] == "Colorado"]['diff'].values))
print("Georgia difference: {}".format(data[data['Location'] == "Georgia"]['diff'].values))
print("California difference: {}".format(data[data['Location'] == "California"]['diff'].values))

data['craig'] = 'craig'
data['ann'] = 'craig'

print(are_columns_equal(data, 'craig', 'ann'))
print(are_columns_equal(data, 'total_adult_age_groups', 'total_adults'))

get_location_difference_dict(data, 'total_adult_age_groups', 'total_adults')

race_columns = ['White', 'Black', 'Hispanic', 'Asian', 'American_Indian_or_Alaska_Native', \
                'Native_Hawaiian_or_Other_Pacific_Islander', 'Two_Or_More_Races']
race_similarity = compute_cosine_similarity(data, race_columns)
for item in race_similarity:
    print(item)

min_race_similarity, max_race_similarity = get_min_max_similarity(race_similarity)