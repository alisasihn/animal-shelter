import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, mean_absolute_error, \
    mean_squared_error
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('../data/outcomes.csv')
working_data = data.copy().dropna()

string_map = {}


# handle non-numeric data
def non_numeric_data(df):
    # take all columns
    columns = df.columns.values

    z = 0

    # create empty list
    for column in columns:
        values = {}

        def convert_to_int(val):
            return values[val]

        # if not a number, convert
        if df[column].dtype != np.int64 and df[column].dtype != np.float64:
            column_contents = df[column].values.tolist()
            make_unique = set(column_contents)
            x = 0
            for unique in make_unique:
                if unique not in values:
                    values[unique] = x
                    x += 1

            df[column] = list(map(convert_to_int, df[column]))

        string_map[z] = values
        z += 1

    return df


# convert strings to integers
working_data = non_numeric_data(working_data)

X = (working_data.drop(['outcome_type'], axis=1))
y = working_data['outcome_type']

# split data for training and testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# random forest classifier
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

rf_classification = RandomForestClassifier(n_estimators=200)
rf_classification.fit(X_train, y_train)


# feature importance graph
# features = X.columns
# importances = rf_classification.feature_importances_
# indices = np.argsort(importances)
# plt.title('Feature Importances')
# plt.barh(range(len(indices)), importances[indices], align='center')
# plt.yticks(range(len(indices)), [features[i] for i in indices])
# plt.show()

# test
# y_pred = rf_classification.predict(X_test)
# conf_mat = confusion_matrix(y_test, y_pred)
# sns.heatmap(conf_mat, annot=True)
# plt.show()
# print(classification_report(y_test, y_pred))
# print('Accuracy: ', accuracy_score(y_test, y_pred))

def predict_outcome(df):
    outcome = rf_classification.predict(df)
    outcome = outcome[0]
    outcome_keys = list(string_map[0].keys())
    outcome_values = list(string_map[0].values())
    outcome_value = outcome_keys[outcome_values.index(outcome)]
    return outcome_value


def predict_input_outcome(altered, sex, age, animal_type, color, month, breed, intake_condition):
    # create input dictionary to hold the input data
    input_dict = {'Altered/Intact': [], 'Sex': [], 'Age (years)': [], 'Animal Type': [], 'Color': [], 'Month': [],
                  'Breed': [], 'Intake Condition': []}

    # get integer values of string keys and insert into input dictionary
    altered_val = string_map[1].get(altered)
    input_dict['Altered/Intact'] = altered_val

    sex_val = string_map[2].get(sex)
    input_dict['Sex'] = sex_val

    input_dict['Age (years)'] = int(age)

    animal_type_val = string_map[4].get(animal_type)
    input_dict['Animal Type'] = animal_type_val

    color_val = string_map[5].get(color)
    input_dict['Color'] = color_val

    input_dict['Month'] = int(month)

    breed_val = string_map[7].get(breed)
    input_dict['Breed'] = breed_val

    intake_condition_val = string_map[8].get(intake_condition)
    input_dict['Intake Condition'] = intake_condition_val

    # turn dictionary into dataframe
    input_df = pd.DataFrame(data=input_dict, index=[0])

    return predict_outcome(input_df)


# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)
# reg = RandomForestRegressor(n_estimators=200, random_state=0)
# reg.fit(X_train, y_train)
# y_pred = reg.predict(X_test)

# print('MAE:', mean_absolute_error(y_test, y_pred))
# print('MSE:', mean_squared_error(y_test, y_pred))
# print('RMSE:', np.sqrt(mean_squared_error(y_test, y_pred)))
