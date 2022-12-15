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


def add_mark(df: pd.DataFrame) -> None:
    """This function adds third column in dataframe - mark of image(1 or 0)"""
    value = []
    for item in df['DatasetClass']:
        if item == 'tiger':
            value.append(0)
        else:
            value.append(1)
    df['mark'] = value


def add_hwcColumns(df: pd.DataFrame) -> None:
    """This function adds to dataframe 3 columns: height, width and channels of the image"""
    img_width = []
    img_height = []
    img_channel = []
    for item in df['AbsolutePath']:
        img = cv2.imread(item)
        img_height.append(img.shape[0])
        img_width.append(img.shape[1])
        img_channel.append(img.shape[2])
    df['height'] = img_height
    df['width'] = img_width
    df['channel'] = img_channel


def mark_filter(df: pd.DataFrame, class_mark: int) -> pd.DataFrame:
    """This function selects all images with mark and returns a DataFrame filtered by mark"""
    return df[df['mark'] == class_mark]