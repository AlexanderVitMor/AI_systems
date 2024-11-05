import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OrdinalEncoder

#%%

def kill_0GB(data: pd.DataFrame, labels: list[str]) -> pd.DataFrame:
    data: pd.DataFrame = data.copy()
    for label in labels:
        data.loc[data[label] == '0 GB', label] = np.nan

    full_data: pd.DataFrame = data.fillna(data.mode().iloc[0])
    return full_data


def made_all_to_categorical(data: pd.DataFrame) -> pd.DataFrame:
    data: pd.DataFrame = data.copy()

    data_obj: pd.DataFrame = data.select_dtypes(include='object').copy()
    labels_cat: list[str] = data_obj.columns.tolist()

    ordinal_encoder: OrdinalEncoder = OrdinalEncoder()

    for label in labels_cat:
        data[label] = ordinal_encoder.fit_transform(data[[label]])

    return data
