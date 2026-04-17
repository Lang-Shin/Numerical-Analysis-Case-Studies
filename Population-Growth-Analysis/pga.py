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
fig, axes = plt.subplots(1, 2, figsize=(13, 6))
axes[0].plot(df['year'], df['population'], marker='o', color="#2C7B0A")
axes[0].set_xticks(df['year'])
axes[0].grid(True, alpha=0.6, linestyle='-', animated=True)
axes[0].set_title("Population vs Time", fontweight="bold")
axes[0].set_xlabel("Year", fontweight="bold")
axes[0].set_ylabel("Population", fontweight="bold")

years = np.array([2021, 2022, 2023])
grates = np.array([grate2021, grate2022, grate2023])
axes[1].plot(years, grates, marker='o', color="#2C7B0A")
axes[1].set_xticks(years)
axes[1].grid(True, alpha=0.6, linestyle='-')
axes[1].set_title("Growth Rate vs Time", fontweight="bold")
axes[1].set_xlabel("Year", fontweight="bold")
axes[1].set_ylabel("Growth Rate", fontweight="bold")

plt.tight_layout()
plt.show()