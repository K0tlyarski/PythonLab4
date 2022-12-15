import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import cv2


def create_DataFrame() -> pd.DataFrame:
    """This function takes data from 2 csv files and create dataframe with 2 columns"""
    df1 = pd.read_csv(os.path.join("/Users", "vadimkotlarskij", "Desktop", "Python", "Lab4TEST", "annotationtiger.csv"),
                      sep=',',
                      header=None)
    df2 = pd.read_csv(
        os.path.join("/Users", "vadimkotlarskij", "Desktop", "Python", "Lab4TEST", "annotationleopard.csv"), sep=',',
        header=None)
    df = pd.concat([df1, df2], ignore_index=True)
    df.drop(1, axis=1, inplace=True)
    df.rename(columns={0: 'AbsolutePath', 2: 'DatasetClass'}, inplace=True)
    return df

