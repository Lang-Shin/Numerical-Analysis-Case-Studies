import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def growth_rate(df, year):
    """
        Gets the growth rate for the year 2021-2023

                            P(t+1) - P(t-1)
        FORMULA : P'(t) = ---------------------
                                   2
    """

    y1 = df.loc[df['year'] == year+1, 'population'].iloc[0]
    y2 = df.loc[df['year'] == year-1, 'population'].iloc[0]

    p = (y1 - y2 ) / 2

    return p


def total_change(df):
    """Get the total population change as year goes on"""

    return (
        np.trapz(df['population'], df['year'])
    )



df = pd.read_csv("Population-Growth-Analysis/population_data.csv")

grate2021 = growth_rate(df, 2021)
grate2022 = growth_rate(df, 2022)
grate2023 = growth_rate(df, 2023)

print(df)


# VISUALIZATION
