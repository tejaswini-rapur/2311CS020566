# -*- coding: utf-8 -*-
"""28-1-25(1)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZnPkN3SLELu5yL6mxk0LX5zzFitvOei6
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

data = {
    'Customer_ID': [1,2,3,4,5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'color': ['red', 'green', 'blue', 'green', 'red'],
    'gender': ['female', 'male', 'male', 'female', 'female'],
}

df = pd.DataFrame(data)
print("Original dataframe: ")
print(df)

one_hot_encoder = OneHotEncoder(sparse_output=False)
encoded_columns = ["Name","Age","color","Customer_ID","gender"]
encoded_data = one_hot_encoder.fit_transform(df[encoded_columns])
encoded_df = pd.DataFrame(encoded_data, columns=one_hot_encoder.get_feature_names_out(encoded_columns))
df = pd.concat([df, encoded_df], axis=1)
df.drop(columns=encoded_columns, inplace=True)

print("\nEncoded dataframe: ")
print(df)